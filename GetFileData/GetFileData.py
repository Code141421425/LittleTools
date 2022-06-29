import os


class GetFileData:
    bu = 1024
    targetTxtPath = r"C:\Users\Shang\Desktop\\"
    fileName = []

    def __init__(self, filePathRoot, getDataType=None):
        self.filePathRoot = filePathRoot
        # GetSize 相关
        self.resultList = []
        self.rankKB = self.bu ** 1
        self.rankMB = self.bu ** 2
        self.rankGB = self.bu ** 3

        # 0-getDataSize 1-getDataName
        if not getDataType:
            self.typeCode = 0
        else:
            self.typeCode = getDataType

    def __getFileSize(self, filepath):
        fileSize = os.path.getsize(filepath)
        return self.__ToGBExpress(fileSize)

    def __ToGBExpress(self, size):
        return round(size/self.rankGB, 2)

    def getDataResultList(self):
        for file in os.listdir(self.filePathRoot):
            if self.typeCode == 0:
                self.resultList.append(self.__getFileSize(self.filePathRoot + file))
            elif self.typeCode == 1:
                self.resultList.append(self.__getFileName(self.filePathRoot+file))

    @staticmethod
    def __getFileName(filePath):
        fileName = os.path.basename(filePath).split(".")
        return fileName[0]

    def getSizeByPrint(self):
        self.getDataResultList()
        for result in self.resultList:
            print(result)

    def getResultInTxt(self):
        self.getDataResultList()
        txt = open(self.targetTxtPath+"GetSizeResult.txt", mode="w",encoding="utf-8")
        for result in self.resultList:
            if self.typeCode == 0:
                t = "%.2f" % result + "\n"
            else:
                t = "%s" % result + "\n"
            txt.writelines(t)
        txt.close()
        print("Write txt Finish")



if __name__ == "__main__":
    TargetPathRoot = "C:\TempDL\AVG\\"
    GetFileData(TargetPathRoot,1).getSizeByPrint()









