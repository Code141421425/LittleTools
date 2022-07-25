import os


class ReFileName:

    filePath = ""
    prefix = ""
    suffix = ""

    def __init__(self, filePath, prefix="", suffix=".jpg"):
        self.filePath = filePath
        self.prefix = prefix
        self.suffix = suffix

    def __ReadFile(self):
        return os.listdir(self.filePath)

    def ReNameFile(self):
        files = self.__ReadFile()
        files.sort(key=self.test, reverse=False)
        print(files)

        for i in range(len(files)):
            oldName = os.path.join(self.filePath, files[i])
            if i==0:
                nemName = os.path.join(self.filePath, self.prefix + self.suffix)
            else:
                nemName = os.path.join(self.filePath, self.prefix+"-" + i.__str__() + self.suffix)
            os.rename(oldName,nemName)

    def test(self, e):
        return os.path.getctime(self.filePath+e)

    def SetReNameFilePath(self, filePath):
        self.filePath = filePath

    def SetPrefix(self, prefix):
        self.prefix = prefix

    def SetSuffix(self, suffix):
        self.suffix = suffix

    def Run(self):
        self.ReNameFile()
        pass



if __name__ == '__main__':
    # Config.set('graphics', 'width', '400')
    # Config.set('graphics', 'height', '200')

    ReFileName(filePath=r"C:\Users\Shang\Desktop\test\\", prefix="2_三大主流编程语言").Run()



