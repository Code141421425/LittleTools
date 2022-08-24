import os
import shutil

class FileMove:
    path1 = r"C:\Users\Shang\Desktop\t1"
    path2 = r"C:\Users\Shang\Desktop\t2\tf.txt"

    def __init__(self):
        pass

    def moveFile(self, file, targetPath):
        fpath, fname = os.path.split(file)  # 分离文件名和路径
        if not os.path.exists(targetPath):
            os.makedirs(targetPath)  # 创建路径
        shutil.move(file, targetPath+"\\"+fname)  # 移动文件
        # print("move %s -> %s" % (self.path1, self.path2 + fname))


if __name__ == "__main__":
    FileMove().moveFile(1)