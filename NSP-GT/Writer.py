import configparser
import os
# from Logger import MyLogger


class FileWriter:
    SAVED_DATA_NAME = "\\SavedData.ini"
    conf = None

    def __init__(self, *args, **kwargs):
        super(FileWriter, self).__init__(*args, **kwargs)

        self.rootPath = os.path.abspath(__file__ + "..\\..\\")
        self.conf = configparser.RawConfigParser()
        self.conf.read(self.rootPath + self.SAVED_DATA_NAME, encoding="utf-8")

    def SavePoint(self, user):
        self.conf.set(user.userName, "point", user.point)
        self.conf.set(user.userName, "totalPoint", user.totalPoint)
        self.conf.set(user.userName, "todayPoint", user.todayPoint)
        self.conf.set(user.userName, "todayLogMinute", user.todayPoint)
        self.conf.set(user.userName, "todayLogWorkMinute", user.todayLogWorkMinute)
        self.conf.set(user.userName, "todayOfferHours", user.todayOfferHours)
        self.conf.set(user.userName, "logTimeStamp", user.logTimeStamp)
        self.conf.write(open(self.rootPath + self.SAVED_DATA_NAME, "w", encoding="utf-8"))
        print("Data Saved")

    def SetPTExecutedTimes(self, user):
        self.conf.set(user.userName, "executedTime", user.executedTime)
        self.conf.write(open(self.rootPath + self.SAVED_DATA_NAME, "w", encoding="utf-8"))
        print("Data Saved")

    def SetNowPt(self, user):
        self.conf.set(user.userName, "nowPT", user.nowPT)
        self.conf.write(open(self.rootPath + self.SAVED_DATA_NAME, "w", encoding="utf-8"))
        print("Data Saved")

    def LoadPoint(self):
        pass

    def GetUserData(self, userName):
        result = {}
        result["userName"] = userName
        result["point"] = self.conf.get(userName, "point")
        result["totalPoint"] = self.conf.get(userName, "totalPoint")
        result["todayPoint"] = self.conf.get(userName, "todayPoint")
        result["todayLogMinute"] = self.conf.get(userName, "todayLogMinute")
        result["todayLogWorkMinute"] = self.conf.get(userName, "todayLogWorkMinute")
        result["todayOfferHours"] = self.conf.get(userName, "todayOfferHours")
        result["logTimeStamp"] = self.conf.get(userName, "logTimeStamp")
        result["nowPT"] = self.conf.get(userName, "nowPT")
        result["executedTime"] = self.conf.get(userName, "executedTime")


        return result


class LogLoader:
    LOG_DATA_NAME = "\\Log\\NSP_Report"
    readLineAmount = 0

    def __init__(self, readLineAmount=15):
        self.readLineAmount = readLineAmount

    def GetLogData(self):
        file = open(os.path.abspath(__file__ + "..\\..\\") + self.LOG_DATA_NAME, 'r')

        count = 0
        data = []
        for line in file.readlines():
            if count < self.readLineAmount:
                line = line.strip()
                data.append(line)
            else:
                break

        return data


if __name__ == '__main__':
    # print(FileWriter().GetUserData("W"))
    LogLoader()
