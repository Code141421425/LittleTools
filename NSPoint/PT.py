from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from Writer import LogLoader


class PT(BoxLayout):
    nowPT = StringProperty()
    executedTime = StringProperty()
    userName = ""

    def __init__(self, *args, **kwargs):
        super(PT, self).__init__(*args, **kwargs)

    def PtInit(self, user):
        self.nowPT = str(user.nowPT)
        self.executedTime = str(user.executedTime)
        self.userName = user.userName

    def SetPT(self, nowPT, executedTime):
        print(nowPT)
        print(executedTime)
        self.nowPT = str(nowPT)
        self.executedTime = str(executedTime)

