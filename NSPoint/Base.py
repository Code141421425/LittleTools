from Writer import FileWriter


class User:
    userName = ""
    point = -1.0
    totalPoint = 0.0

    def __init__(self, userName):
        data = FileWriter().GetUserData(userName)
        self.userName = userName
        self.point = float(data["point"])
        self.totalPoint = data["totalPoint"]

    def AddPoint(self, addAmount):
        print(type(float(addAmount)))
        self.point += float(addAmount)


def singleton(cls):
    instances = {}

    def _singleton(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return _singleton