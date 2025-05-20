from kivy.config import Config
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty
from kivy.lang import Builder
from NSPoniter import NSPointer
from Rule import PointRule,CostRule

from LogUI import LogUI
from PT import PT
from TimeRecord import TimeRecord


class UIController(BoxLayout):
    nsPoint = None

    def __init__(self, nsPoint, *args, **kwargs):
        super(UIController, self).__init__(*args, **kwargs)

        # 【优化】配置两个角色的数据
        self.nsPoint = nsPoint
        self.__UserDataInit("W")
        # self.__UserDataInit("R")

    def __UserDataInit(self, userName):
        # 【修改】 需要改成从
        user = self.nsPoint.GetUserData(userName)
        if userName == 'W':
            self.ids.user1.UnitInit(user, [.6, .3, .3, 1])
        # elif userName == 'R':
        #     self.ids.user2.UnitInit(user, [.3, .3, .6, 1])

    def RefreshData(self, dataList):
        # 刷新显示的Point数据
        print(dataList)
        for data in dataList:
            if data == "W":
                self.ids.user1.SetData(dataList[data]["point"],
                                       dataList[data]["totalPoint"],
                                       dataList[data]["todayPoint"],
                                       dataList[data]["todayLogPercent"],
                                       todayWorkMinute=dataList[data]["todayLogWorkMinute"],
                                       todayOfferHours=dataList[data]["todayOfferHours"],
                                       )
                # self.ids.user1.ids.pt.SetPT(dataList[data]["nowPT"], dataList[data]["executedTime"])
            # elif data == "R":
            #     self.ids.user2.SetData(dataList[data]["point"], dataList[data]["totalPoint"])
            #     self.ids.user2.ids.pt.SetPT(dataList[data]["nowPT"], dataList[data]["executedTime"])


class PointUnit(BoxLayout):
    userName = StringProperty()
    point = StringProperty()
    totalPoint = StringProperty()
    logTimeStamp = StringProperty()
    factor = StringProperty()
    costCaseText = StringProperty()
    offerHours = StringProperty()
    workMinute = StringProperty()
    backColor = ListProperty()
    selectedRule = ""
    costRule = ""

    todayPoint = StringProperty()
    todayLogPercent = StringProperty()
    todayOfferHours = StringProperty()
    todayWorkHours = StringProperty()
    pt = None

    def __init__(self, userName="", *args, **kwargs):
        super(PointUnit, self).__init__(*args, **kwargs)

        # 初始化得分单元
        self.userName = str(userName)

    def UnitInit(self, user, backcolor=[1, 1, 1, 1]):
        self.userName = user.userName
        self.SetData(user.point, user.totalPoint, user.todayPoint,
                     user.todayLogPercent,
                     todayOfferHours=user.todayOfferHours,
                     todayWorkMinute=user.todayLogWorkMinute
                     )
        self.backColor = backcolor
        # self.pt = self.ids.pt
        # self.pt.PtInit(user)

    def SetData(self, point, totalPoint, todayPoint, todayLogPercent, todayOfferHours, todayWorkMinute):
        # 设置Point显示的值
        self.point = "%.2f Min" % (float(point))
        # self.totalPoint = "%.2f Min" % (float(totalPoint))
        self.todayPoint = "%.2f Min" % (float(todayPoint))
        self.todayLogPercent = "%.2f" % (float(todayLogPercent))
        self.todayOfferHours = "%.f" % (float(todayOfferHours))
        self.todayWorkHours = "%.1f" % (float(todayWorkMinute) / 60)

    def generate_DropDownList(self):
        for rule in PointRule:
            btn = Button(text=rule, size_hint_y=None, height=26)
            btn.bind(on_release=lambda btn: self.ids.dropdownAdd.select(btn.text))
            self.ids.dropdownAdd.bind(on_select=lambda instance, x: setattr(self.ids.dropdown_mainBtn, 'text', x))
            self.ids.dropdownAdd.add_widget(btn)

    def generate_DropDownCostList(self):
        for rule in CostRule:
            btn = Button(text=rule, size_hint_y=None, height=26)
            btn.bind(on_release=lambda btn: self.ids.dropdownCost.select(btn.text))
            self.ids.dropdownCost.bind(on_select=lambda instance, x: setattr(self.ids.dropdown_CostBtn, 'text', x))
            self.ids.dropdownCost.add_widget(btn)

    def refresh_DropDownList(self):
        self.ids.dropdownAdd.clear_widgets()
        self.generate_DropDownList()

    def refresh_DropDownCostList(self):
        self.ids.dropdownCost.clear_widgets()
        self.generate_DropDownCostList()

    def handle_DropDownSelect(self):
        # 处理选择下拉框内容之后
        self.selectedRule = self.ids.dropdown_mainBtn.text
        # 刷新数据
        self.__refreshFactor()

    def handle_CostDropDownSelect(self):
        # 处理选择下拉框内容之后
        self.costRule = self.ids.dropdown_CostBtn.text
        self.__refreshCostChoice()

    def __refreshFactor(self):
        self.factor = self.ids.dropdown_mainBtn.text

    def __refreshCostChoice(self):
        self.costCaseText = self.costRule

    def WorkTime_To(self, amount):
        self.ids.mintue_input.text = str(amount)


class NSP(App):
    nsPointer = None
    UIController = None

    def __init__(self, **kwargs):
        super(NSP, self).__init__(**kwargs)
        self.title = "NSP-GT"  # 设置应用名称

    def build(self):
        self.nsPointer = NSPointer(app=self)
        self.UIController = UIController(self.nsPointer)

        return self.UIController

    def AddPoint(self, addAmount, user):
        self.nsPointer.AddPoint(addAmount, user)

    def RefreshUIData(self, data):
        self.UIController.RefreshData(data)

    def RawDataToCalculate(self, root):
        self.nsPointer.CalculateAndAddPoint(userName=root.userName,
                                            # root.ids.factor_input.text,
                                            minute=root.ids.mintue_input.text,
                                            ruleName=root.ids.addChoice_input.text)

    def RawDataToCost(self, root):
        self.nsPointer.CostPoint(root.userName, root.ids.case_input.text, root.ids.costAmount_input.text)

    def AddLog(self, msg):
        self.UIController.ids.logUI.AddLog(msg)

    def Handle_Add_PT(self, root):
        self.nsPointer.AddPT(root.userName, root.ids.input_pt_value.text)

    def Handle_Reduce_PT(self, root):
        self.nsPointer.ReducePT(root.userName, root.ids.input_pt_value.text)

    def Handle_Execute(self, root):
        self.nsPointer.ExeCutePT(root.userName)

    def Handle_OfferHours(self, root):
        self.nsPointer.setOfferHours(root.userName, root.ids.offerhours_input.text)


if __name__ == '__main__':
    # Config.set('graphics', 'width', '850')
    Config.set('graphics', 'width', '720')
    Config.set('graphics', 'height', '600')

    NSP().run()
