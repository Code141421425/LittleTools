import os


class GetFileSize:
    bu = 1024
    targetTxtPath = r"C:\Users\Shang\Desktop\\"
    fileName = []

    def __init__(self, filePathRoot):
        self.filePathRoot = filePathRoot
        self.resultList = []
        self.rankKB = self.bu ** 1
        self.rankMB = self.bu ** 2
        self.rankGB = self.bu ** 3

    def getFileSize(self, filepath):
        fileSize = -1.0
        fileSize = os.path.getsize(filepath)
        return self.ToGBExpress(fileSize)

    def ToGBExpress(self, size):
        return round(size/self.rankGB, 2)

    def getSizeResultList(self):
        for file in os.listdir(self.filePathRoot):
            self.resultList.append(self.getFileSize(self.filePathRoot + file))

    def getSizeByPrint(self):
        self.getSizeResultList()
        for result in self.resultList:
            print(result)

    def getSizeByTxt(self):
        self.getSizeResultList()
        txt = open(self.targetTxtPath+"GetSizeResult.txt", mode="w")
        for result in self.resultList:
            t = "%.2f" % result + "\n"
            txt.writelines(t)
        txt.close()
        print("Write txt Finish")



if __name__ == "__main__":
    TargetPathRoot = "C:\TempDL\AVG\\"
    GetFileSize(TargetPathRoot).getSizeByTxt()









