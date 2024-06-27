from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from Writer import LogLoader


class LogUI(BoxLayout):
    logPath = ""
    logData = StringProperty()
    logLoader = None

    def __init__(self, *args, **kwargs):
        super(LogUI, self).__init__(*args, **kwargs)

        self.logLoader = LogLoader()
        self.InitData()

    def InitData(self):
        self.logData = ""

        for line in self.logLoader.GetLogData():
            self.logData += "\n" + line

    def AddLog(self, msg):
        self.logData += "\n" + msg

