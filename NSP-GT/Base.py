from Writer import FileWriter
import  time


class User:
    userName = ""
    point = -1.0
    totalPoint = 0.0
    nowPT = -1
    executedTime = -1

    todayPoint = -1
    todayLogMinute = -1
    todayLogPercent = -1
    todayOfferHours = -1
    todayLogWorkMinute = -1
    logTimeStamp = 0.0

    ALL_DAY_MINUTE = 14.40

    def __init__(self, userName):
        data = FileWriter().GetUserData(userName)
        self.userName = userName
        self.point = float(data["point"])
        self.totalPoint = float(data["totalPoint"])
        self.executedTime = int(data["executedTime"])
        self.nowPT = int(data["nowPT"])

        self.todayPoint = int(data["todayPoint"])
        self.todayLogMinute = int(data["todayLogMinute"])
        self.todayLogWorkMinute = int(data["todayLogWorkMinute"])
        self.todayOfferHours = int(data["todayOfferHours"])
        self.logTimeStamp = float(data["logTimeStamp"])

        self.todayLogPercent = self.todayLogMinute / self.ALL_DAY_MINUTE

    def AddPoint(self, addAmount, useMinute, isWork=False, isToday=True, logger=None):
        self.point += float(addAmount)
        self.totalPoint += float(addAmount)

        if isWork:
            self.todayLogWorkMinute += int(useMinute)
            print(self.todayLogWorkMinute)

        self.__PassToday(useMinute, isToday, logger)

        self.todayPoint += int(addAmount)

    def CostPoint(self, costAmount, useMinute,  isToday=True, logger=None):
        # 区别在于，不会减历史总计的分数
        self.point -= float(costAmount)

        self.__PassToday(useMinute, isToday, logger)

        self.todayPoint -= int(costAmount)

    def __PassToday(self, useMinute, isToday, logger=None):
        if not isToday:
            self.logTimeStamp = time.time()

            if self.todayOfferHours != 0:
                # 使用 f-string（Python 3.6+）
                offerFinishTxt = f"finished {self.todayLogWorkMinute * 100 / (self.todayOfferHours * 60):.2f}% Today"
            else:
                offerFinishTxt = "and do not offer work Today"

            logger.info(msg="[Summary] %s get %.1f min,log %.1f %%," %
                            (self.userName, self.todayPoint, self.todayLogPercent)+offerFinishTxt)
            self.todayPoint = 0
            self.todayLogMinute = 0
            self.todayLogPercent = 0
            self.todayLogWorkMinute = 0
            self.todayOfferHours = 0

        # 计算本日log百分比
        self.todayLogMinute += float(useMinute)
        self.todayLogPercent = self.todayLogMinute / self.ALL_DAY_MINUTE


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

