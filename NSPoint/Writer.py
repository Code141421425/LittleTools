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

    def SavePoint(self, userName, point):
        self.conf.set(userName, "point", point)
        self.conf.write(open(self.rootPath + self.SAVED_DATA_NAME, "w", encoding="utf-8"))
        print("Data Saved")

    def LoadPoint(self):
        pass

    def GetUserData(self, userName):
        result = {}
        result["userName"] = userName
        result["point"] = self.conf.get(userName, "point")
        result["totalPoint"] = self.conf.get(userName, "totalPoint")

        return result


if __name__ == '__main__':
    print(FileWriter().GetUserData("W"))
