import configparser
import os


class FileWriter:
    SAVED_DATA_NAME = "\\SavedData.ini"
    conf = None

    def __init__(self, *args, **kwargs):
        super(FileWriter, self).__init__(*args, **kwargs)

        self.rootPath = os.path.abspath(__file__ + "..\\..\\")
        self.conf = configparser.RawConfigParser()
        self.conf.read(self.rootPath + self.SAVED_DATA_NAME, encoding="utf-8")

    def AddPath(self, title, path):
        self.conf.set("Path", title, path)
        self.conf.write(open(self.rootPath + self.SAVED_DATA_NAME, "w", encoding="utf-8"))
        print("Data Saved")

    def LoadPath(self):
        pass

    def GetPathDataList(self):
        result = []

        for key in self.conf.options("Path"):
            result.append({
                "posTitle": key,
                "targetPath": self.conf.get("Path", key)
            })

        return result


if __name__ == "__main__":
    print(FileWriter().GetPathDataList())