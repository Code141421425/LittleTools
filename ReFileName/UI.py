import configparser
import os
from ReFileName import ReFileName
from kivy.config import Config
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty


class Controller(BoxLayout):
    renameFilePath = StringProperty()
    prefix = StringProperty()
    suffix = StringProperty()
    reFileName = None
    rootPath = ""
    CONFIG_FILE_NAME = "\\config.ini"
    SECTION_NAME = "Data"

    def __init__(self, *args, **kwargs):
        super(Controller, self).__init__(*args, **kwargs)

        # 获取数据
        self.rootPath = os.path.abspath(__file__+"..\\..\\")
        self.conf = configparser.RawConfigParser()
        self.conf.read(self.rootPath + self.CONFIG_FILE_NAME, encoding="utf-8")

        # UI数据初始化
        self.renameFilePath = self.conf.get("Data", "filePath")
        self.prefix = self.conf.get(self.SECTION_NAME, "prefix")
        self.suffix = self.conf.get(self.SECTION_NAME, "suffix")
        self.reFileName = ReFileName(filePath=self.renameFilePath, prefix=self.prefix, suffix=self.suffix)

    def WriteDataToINI(self):
        self.__SyncUIData()
        self.conf.set(self.SECTION_NAME, "filePath", self.renameFilePath)
        self.conf.set(self.SECTION_NAME, "prefix", self.prefix)
        self.conf.set(self.SECTION_NAME, "suffix", self.suffix)

        self.conf.write(open(self.rootPath + self.CONFIG_FILE_NAME, "w", encoding="utf-8"))
        print("Data Saved")

    def __SyncUIData(self):
        self.renameFilePath = self.ids.reFileNamePath_input.text
        self.reFileName.SetReNameFilePath(self.renameFilePath)

        self.prefix = self.ids.prefix_input.text
        self.reFileName.SetPrefix(self.prefix)

        self.suffix = self.ids.suffix_input.text
        self.reFileName.SetSuffix(self.suffix)

    def ShowPrefixOnCmd(self):
        self.__SyncUIData()
        print(self.prefix)

    def RunReName(self):
        self.__SyncUIData()
        self.reFileName.Run()
        print("ReName Finish")


class ReFileNameApp(App):
    def build(self):
        return Controller()


if __name__ == '__main__':
    Config.set('graphics', 'width', '420')
    Config.set('graphics', 'height', '220')

    ReFileNameApp().run()




