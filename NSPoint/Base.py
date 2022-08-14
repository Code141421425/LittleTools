from Writer import FileWriter


class User:
    userName = ""
    point = -1.0
    totalPoint = 0.0

    def __init__(self, userName):
        data = FileWriter().GetUserData(userName)
        self.userName = userName
        self.point = float(data["point"])
        self.totalPoint = float(data["totalPoint"])

    def AddPoint(self, addAmount):
        self.point += float(addAmount)
        self.totalPoint += float(addAmount)

    def CostPoint(self, costAmount):
        # 区别在于，不会减历史总计的分数
        self.point -= float(costAmount)


def singleton(cls):
    instances = {}

    def _singleton(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return _singleton