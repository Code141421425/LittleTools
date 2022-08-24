from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty, AliasProperty


class TargetPanel(BoxLayout):

    targetPosDict = {}
    targetPosDict = {
        "t3": r"C:\Users\Shang\Desktop\t3",
        "t2": r"C:\Users\Shang\Desktop\t2"
    }

    data = ListProperty()

    def __init__(self, *args, **kwargs):
        super(TargetPanel, self).__init__(*args, **kwargs)

        self.data = [
            {"posTitle": "t2",
             "targetPath": r"C:\Users\Shang\Desktop\t2"},
            {"posTitle": "3",
             "targetPath": r"C:\Users\Shang\Desktop\t3"}]

    def SetTargetPosDict(self, dict):
        self.targetPosDict = dict

    def get_data_for_loadConfigList(self):
        reslut = ["1","2"]

        return self.data

    data_for_loadConfigList = AliasProperty(get_data_for_loadConfigList, bind=["data"])


class RecycleViewUnit(BoxLayout):
    posTitle = StringProperty()
    targetPath = ""

