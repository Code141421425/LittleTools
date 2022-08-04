from kivy.config import Config
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty,ListProperty
from NSPoniter import NSPointer
from Rule import PointRule


class UIController(BoxLayout):
    nsPoint = None

    def __init__(self, nsPoint, *args, **kwargs):
        super(UIController, self).__init__(*args, **kwargs)

        # 【优化】配置两个角色的数据
        self.nsPoint = nsPoint
        self.__UserDataInit("W")
        self.__UserDataInit("R")

    def __UserDataInit(self, userName):
        # 【修改】 需要改成从
        user = self.nsPoint.GetUserData(userName)
        if userName == 'W':
            self.ids.user1.UnitInit(user.userName, user.point, [.6, .6, .6, 1])
        elif userName == 'R':
            self.ids.user2.UnitInit(user.userName, user.point, [.4, .4, .4, 1])

    def RefreshData(self, dataList):
        # 刷新显示的Point数据
        for data in dataList:
            if data == "W":
                self.ids.user1.SetData(dataList[data]["point"])
            elif data == "R":
                self.ids.user2.SetData(dataList[data]["point"])


class PointUnit(BoxLayout):
    userName = StringProperty()
    point = StringProperty()
    factor = StringProperty()
    workMinute = StringProperty()
    backColor = ListProperty()
    selectedRule = ""

    def __init__(self, userName="", *args, **kwargs):
        super(PointUnit, self).__init__(*args, **kwargs)

        # 初始化得分单元
        self.userName = str(userName)

    def UnitInit(self, userName, point, backcolor=[1, 1, 1, 1]):
        self.userName = userName
        self.SetData(point)
        self.backColor = backcolor

    def SetData(self, point):
        # 设置Point显示的值
        self.point = "%.2f Pt" % (float(point))

    def generate_DropDownList(self):
        for rule in PointRule:
            btn = Button(text=rule, size_hint_y=None, height=26)
            btn.bind(on_release=lambda btn: self.ids.dropdown.select(btn.text))
            self.ids.dropdown.bind(on_select=lambda instance, x: setattr(self.ids.dropdown_mainBtn, 'text', x))
            self.ids.dropdown.add_widget(btn)

    def refresh_DropDownList(self):
        self.ids.dropdown.clear_widgets()
        self.generate_DropDownList()

    def handle_DropDownSelect(self):
        # 处理选择下拉框内容之后
        print(self.ids.dropdown_mainBtn.text)
        self.selectedRule = self.ids.dropdown_mainBtn.text
        # 刷新数据
        self.__refreshFactor()

    def __refreshFactor(self):
        self.factor = str(PointRule[self.selectedRule])
        print(self.factor)


class NSP(App):
    nsPointer = None
    UIController = None

    def build(self):
        self.nsPointer = NSPointer(app=self)
        self.UIController = UIController(self.nsPointer)

        return self.UIController

    def AddPoint(self, addAmount, user):
        self.nsPointer.AddPoint(addAmount, user)

    def RefreshUIData(self, data):
        self.UIController.RefreshData(data)

    def RawDataToCalculate(self, root):
        self.nsPointer.CalculateAndAddPoint(root.userName,
                                            root.ids.factor_input.text,
                                            root.ids.mintue_input.text,
                                            root.selectedRule)

    def test(self, root):
        self.AddPoint("1.2", root.userName)


if __name__ == '__main__':
    Config.set('graphics', 'width', '650')
    Config.set('graphics', 'height', '400')

    NSP().run()
