import os
# import kivy.config as Config


class ReFileName:

    filePath = ""
    prefix = ""
    suffix = ""

    def __init__(self, filePath, prefix=""):
        self.filePath = filePath
        self.prefix = prefix
        self.suffix = ".jpg"

    def __ReadFile(self):
        return os.listdir(self.filePath)

    def ReNameFile(self):
        files = self.__ReadFile()
        print(files)

        for i in range(len(files)):
            oldName = os.path.join(self.filePath, files[i])
            if i==0:
                nemName = os.path.join(self.filePath, self.prefix + self.suffix)
            else:
                nemName = os.path.join(self.filePath, self.prefix+"-" + i.__str__() + self.suffix)
            os.rename(oldName,nemName)


    def Run(self):
        self.ReNameFile()
        pass



if __name__ == '__main__':
    # Config.set('graphics', 'width', '350')
    # Config.set('graphics', 'height', '200')

    ReFileName(filePath=r"C:\Users\Shang\Desktop\test", prefix="115").Run()



