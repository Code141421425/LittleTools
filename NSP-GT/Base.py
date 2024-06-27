from Writer import FileWriter
import  time


class User:
    userName = ""
    point = -1.0
    totalPoint = 0.0
    nowPT = -1
    executedTime = -1
    todayPoint = 0
    logTimeStamp = 0.0

    def __init__(self, userName):
        data = FileWriter().GetUserData(userName)
        self.userName = userName
        self.point = float(data["point"])
        self.totalPoint = float(data["totalPoint"])
        self.executedTime = int(data["executedTime"])
        self.nowPT = int(data["nowPT"])
        self.todayPoint = int(data["todayPoint"])
        self.logTimeStamp = float(data["logTimeStamp"])

    def AddPoint(self, addAmount, isToday=True):
        self.point += float(addAmount)
        self.totalPoint += float(addAmount)

        if not isToday:
            self.logTimeStamp = time.time()
            self.todayPoint = 0

        self.todayPoint += int(addAmount)

    def CostPoint(self, costAmount, isToday=True):
        # 区别在于，不会减历史总计的分数
        self.point -= float(costAmount)

        if not isToday:
            self.logTimeStamp = time.time()
            self.todayPoint = 0

        self.todayPoint -= int(costAmount)


    def AddOnceExecutedTimes(self):
        self.executedTime += 1

    def AddPT(self, amount):
        self.nowPT += amount

    def ReducePT(self, amount):
        self.nowPT -= amount

    def ReSetPT(self):
        self.nowPT = 0
        self.executedTime += 1


def singleton(cls):
    instances = {}

    def _singleton(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return _singleton