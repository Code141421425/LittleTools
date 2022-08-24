import os,sys
from kivy.config import Config
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.core.window import Window
from FileMove import FileMove
from PicShow import PicShow
from TargetPanel import TargetPanel


class UIController(BoxLayout):

    picPath = StringProperty()

    def __init__(self, *args, **kwargs):
        super(UIController, self).__init__(*args, **kwargs)

        self.picPath = "1.jpg"

    def setPic(self, msg):
        self.picPath = msg;


class PA(App):
    UIController = None
    FileMove = None
    SourcePicPath = r"C:\Users\Shang\Desktop\t1"

    def build(self):
        self.UIController = UIController()
        self.FileMove = FileMove()

        self.__initApp()

        Window.bind(on_keyboard=self.on_keyboard)

        return self.UIController

    def __initApp(self):
        # self.UIController.ids.picShow.initPicData()
        pass

    def on_keyboard(self,window, key,scancode,codepoint,modified):
        # 负责相应快捷键
        if codepoint == "d":
            self.on_button_NextPic()
        elif codepoint == "a":
            self.on_button_PrePic()

    def on_button_NextPic(self):
        self.UIController.ids.picShow.NextPic()

    def on_button_PrePic(self):
        self.UIController.ids.picShow.PrePic()

    def on_button_MoveFile(self, root):
        # 先处理图像显示部分，在处理移动图片
        self.UIController.ids.picShow.Handle_AfterMoveFile()
        self.FileMove.moveFile(file=self.UIController.ids.picShow.exceptPath,
                               targetPath=root.targetPath)

    def on_button_AddNewPath(self, root):
        # 添加到列表中
        self.UIController.ids.targetPanel.AddNewPath(root.ids.input_key.text,
                                                     root.ids.input_path.text)


if __name__ == '__main__':
    sys.path.append(os.path.dirname(__file__))

    Config.set('graphics', 'width', '1000')
    Config.set('graphics', 'height', '800')

    PA().run()