from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
import os


class PicShow(BoxLayout):
    sourcePicPath = r"C:\Users\Shang\Desktop\t1\\"
    nowPicPath = StringProperty()
    nowPicName = StringProperty()
    indexProcess = StringProperty()
    nowPicNo = -1
    exceptPath = ""
    indexList = []
    picDict = {}

    def __init__(self, *args, **kwargs):
        super(PicShow, self).__init__(*args, **kwargs)
        self.__initPicData()

    def __initPicData(self):
        files = os.listdir(self.sourcePicPath)
        for i in range(len(files)):
            self.indexList.append(i)
            self.picDict[i] = files[i]

        self.__refreshPic(0)

    def __refreshPic(self, index):
        self.nowPicNo = index
        self.nowPicPath = self.sourcePicPath + self.picDict[self.nowPicNo]
        # print(self.nowPicName)
        self.__refreshIndex()

    def __refreshIndex(self):
        self.indexProcess = str(self.indexList.index(self.nowPicNo)+1) + " / " + str(len(self.indexList))
        self.nowPicName = str(self.picDict[self.nowPicNo])

    def NextPic(self):
        self.__refreshPic(self.__GetRealIndexAfterIncrease(1))

    def PrePic(self):
        self.__refreshPic(self.__GetRealIndexAfterIncrease(-1))

    def __GetRealIndexAfterIncrease(self, indexIncrease):
        # 输入参数：增加的目录值，比如下一个,indexIncrease就是1，上一个是-1
        # 作用：返回在indexList中，增加目录值对应的序号，比如[1,3,5]，3的下一个就是5
        order = self.indexList.index(self.nowPicNo) + indexIncrease
        if order > len(self.indexList)-1:
            order = 0
        elif order < 0:
            order = len(self.indexList)-1

        print(order)

        return self.indexList[order]

    def Handle_AfterMoveFile(self):
        self.exceptPath = self.nowPicPath
        exceptIndex = self.nowPicNo

        self.NextPic()

        self.indexList.remove(exceptIndex)
        self.picDict.pop(exceptIndex)

