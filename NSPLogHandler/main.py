import os
from ZcwPyUtility import DataHandler

'''
需求：从复数log中，计算每个人的得分
'''


class NSPLogHandler:
    nspLogPath = r"H:\WorkSpace\PycharmProject\LittleTools\NSPoint\Log\\"

    def __init__(self):
        self.wptLog = []
        self.rptLog = []
        self.wpt = 0
        self.rpt = 0

    def CalculateWRPt(self):
        self.__GetUserLog()
        self.__ScanAndAddPoint()

    def __GetUserLog(self):
        for file in os.listdir(self.nspLogPath):
            # 读取所有的log文件
            self.__HandleLog(file)

    def __HandleLog(self, file):
        f = open(self.nspLogPath + file, "r")

        for line in f.readlines():
            """
            log示例：
            [INFO    ]2022-08-12 22:19:32 | R get 1.17 Pt(2,35) by C done
            截取]的后半段，的截取|的前半段，含空格
            """
            data = DataHandler.SplitStr(line, "| ", " Pt")
            if data[0] == "R":
                self.__AddToUserLog("R", data)
            elif data[0] == "W":
                self.__AddToUserLog("W", data)

        f.close()

    def __AddToUserLog(self, user, data):
        """
        传入数据示例：R get 3.50
        """
        if user == "R":
            if str(data).find("get ") != -1:
                self.rptLog.append(float(data.split("get ")[1]))
            # else:
            #     self.rptLog.append(-float(data.split("cost ")[1]))
        elif user == "W":
            if str(data).find("get ") != -1:
                self.wptLog.append(float(data.split("get ")[1]))
            # else:
            #     self.wptLog.append(-float(data.split("cost ")[1]))

    def __ScanAndAddPoint(self):
        for pt in self.rptLog:
            self.rpt += pt

        for pt in self.wptLog:
            self.wpt += pt

        print("R(%d)total: %f" % (len(self.rptLog), self.rpt))
        print("W(%d)total: %f" % (len(self.wptLog), self.wpt))


if __name__ == "__main__":
    NSPLogHandler().CalculateWRPt()

