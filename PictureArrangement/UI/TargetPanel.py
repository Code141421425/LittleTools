from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty, AliasProperty
import os
from FileWriter import FileWriter


class TargetPanel(BoxLayout):

    targetPosDict = {}

    data = ListProperty()
    fileWriter = None

    def __init__(self, *args, **kwargs):
        super(TargetPanel, self).__init__(*args, **kwargs)

        self.fileWriter = FileWriter()
        self.data = self.fileWriter.GetPathDataList()

    def SetTargetPosDict(self, dict):
        self.targetPosDict = dict

    def get_data_for_loadConfigList(self):
        return self.data

    data_for_loadConfigList = AliasProperty(get_data_for_loadConfigList, bind=["data"])

    def AddNewPath(self, key, path):
        # 用key和path 作为kv，加入字典，并刷新。
        # 之后可能会调用文件的写入方法
        newDict = {
            "posTitle": key,
            "targetPath": path
        }

        # 如果没有路径，就创建路径
        if not os.path.exists(path):
            print("create new path: " + path)
            os.mkdir(path)

        # 持久化,只新增
        self.fileWriter.AddPath(key, path)

        self.data.append(newDict)


class RecycleViewUnit(BoxLayout):
    posTitle = StringProperty()
    targetPath = ""


class AddNewPath(BoxLayout):
    pathInputStr = StringProperty()
    keyInputStr = StringProperty()

    def __init__(self, *args, **kwargs):
        super(AddNewPath, self).__init__(*args, **kwargs)

    def ClearTextInput(self):
        pass

