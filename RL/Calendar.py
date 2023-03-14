import os
import datetime
import calendar
from kivy.clock import mainthread
from kivy.lang import Builder

from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty, ColorProperty, NumericProperty

from ZcwPyUtility.FileWirter import FileWriter, Translator
from ZcwPyUtility.BaseDef import singleton

Builder.load_file(os.path.dirname(__file__) + "\\Calendar.kv")


@singleton
class SaveDataWriter:
    data = None

    def __init__(self):
        self.data = FileWriter(
            os.path.abspath(__file__) + "//..//SaveData.ini"
        )


class DateTranslator(Translator):
    def decode(self, rawData):
        # DO
        # Sample: {"20230314":"1"} -> 2023,3,14
        pass


class Calendar(BoxLayout):
    nowMonth = None

    def __init__(self, *args, **kwargs):
        super(Calendar, self).__init__(*args, **kwargs)

        print(SaveDataWriter().data.LoadData(
            str(datetime.date.today().year) + str(datetime.date.today().month)
        ))

        self.MonthInit()

    @mainthread
    def MonthInit(self):
        self.ids.month_Zone.SetMonth(datetime.date.today().year, datetime.date.today().month)

        self.LoadAccompanyData()

    def LoadAccompanyData(self):
        # 载入本月数据
        dataDict = SaveDataWriter().data.LoadData(
            str(datetime.date.today().year) + str(datetime.date.today().month)
        )
        self.ids.month_Zone.SetAccompanyState(dataDict)


class Day(Button):
    date = StringProperty()
    AccState = NumericProperty()
    nowColor = ColorProperty()
    month = None

    def __init__(self, date, month, *args, **kwargs):
        super(Day, self).__init__(*args, **kwargs)

        self.date = str(date)
        self.__selectColor = (.9,.4,.5)
        self.__unSelectColor = (1,1,1)
        self.nowColor = self.__unSelectColor
        self.month = month

    def ChangeAccompanyState(self):
        if self.AccState == 1:
            self.AccState = 0
        else:
            self.AccState = 1
        self.__RefreshBackColor()
        self.month.SaveToWriter(self.date, self.AccState)

    def SetAccompany(self, state):
        state = int(state)
        if state == self.AccState:
            pass
        else:
            self.AccState = state
            self.__RefreshBackColor()

    def __RefreshBackColor(self):
        if self.AccState == 1:
            self.background_color = self.__selectColor
        else:
            self.background_color = self.__unSelectColor



class Month(BoxLayout):
    weekTitle = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat","Sun"]
    monthTitle = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]

    monthText = StringProperty()
    dayDict = {}
    year = -1
    month = -1

    def __init__(self, *args, **kwargs):
        super(Month, self).__init__(*args, **kwargs)

        self.GenWeekTitle()

    @mainthread
    def GenWeekTitle(self):
        for wt in self.weekTitle:
            self.ids.week_title.add_widget(Label(text=wt))

    def SetMonth(self, year, month):
        if month > 0 & month < 13:
            self.monthText = self.monthTitle[month-1]
        else:
            print("Error month")

        self.year = year
        self.month = month

        # set day
        startDay = datetime.date(year, month, 1).weekday()

        # fill last month
        if startDay > 0:
            for i in range(0, startDay):
                self.ids.monthZone.add_widget(Label())
        # fill now
        for i in range(startDay-1, calendar.monthrange(year, month)[1]+1):
            self.dayDict[i] = Day(i, self)
            self.ids.monthZone.add_widget(self.dayDict[i])

    def SetAccompanyState(self, dataDict):
        for k in dataDict:
            self.dayDict[int(k)].SetAccompany(dataDict[k])

    def SaveToWriter(self, date, state):
        SaveDataWriter().data.SaveData(
            str(self.year) + str(self.month), date, state
        )
