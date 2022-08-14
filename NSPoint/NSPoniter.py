import Logger
from Base import User
from Writer import FileWriter
from Logger import MyLogger


class NSPointer:
    userList = []
    addPointDict = None
    subPointDict = None

    def __init__(self, app, addPointDict=None, subPointDict=None):
        # 基础组件的初始化
        self.addPointDict = addPointDict
        self.subPointDict = subPointDict
        self.writer = FileWriter()
        self.logger = MyLogger().logger
        self.app = app

        # 当前写死用户就是W和R
        self.userList.append(User("W"))
        self.userList.append(User("R"))

    def GetUserData(self, userName):
        for user in self.userList:
            if user.userName == userName:
                return user

        return None

    def CalculateAndAddPoint(self, userName, ruleFactor, minute, ruleName=None):
        result = round((float(ruleFactor)/60) * float(minute), 3)
        self.AddPoint(userName, result)

        # 打印log
        self.logger.info(msg="%s get %.2f Pt(%s,%s) by %s done" % (userName, result, ruleFactor, minute, ruleName))

    def AddPoint(self, userName, amount):
        for user in self.userList:
            if user.userName == userName:
                user.AddPoint(amount)
                # 保存结果
                self.writer.SavePoint(user)
                break
        # 同步界面
        self.__syncToUI()

    def CostPoint(self, userName, case, amount):
        # 计算减少的数值
        amount = float(amount)

        for user in self.userList:
            if user.userName == userName:
                user.CostPoint(amount)
                # 保存结果
                self.writer.SavePoint(user)
                break
        self.logger.info(msg="%s cost %.2f Pt by %s" % (userName, amount, case))
        # 同步界面
        self.__syncToUI()

    def __syncToUI(self):
        # 进行一波UI通信时，所需要的数据格式的组装
        data = {}
        for user in self.userList:
            data[user.userName] = {
                "point": user.point,
                "totalPoint": user.totalPoint
            }
        # 同步到界面上
        self.app.RefreshUIData(data)





if __name__ == "__main__":
    NSPointer()



