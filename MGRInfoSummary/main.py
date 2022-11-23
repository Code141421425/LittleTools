import os,sys,time


class LogData:
    startTime = 0
    endTime = -1
    duration = 0
    dataNo = -1

    def __init__(self, dataNo, startTime):
        self.dataNo = dataNo
        self.startTime = startTime

    def PrintData(self):
        print("|%d|%s|%s|%s|" %
              (self.dataNo,
               self.HandleDuration(self.duration),
               time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.startTime)),
               time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.endTime))
              ))

    def HandleDuration(self,durationTime):\
        return "%.2d:%.2d" % (
            durationTime/60,
            durationTime%60
        )

    def SetEndTime(self, endTime):
        self.endTime = endTime
        self.duration = self.endTime - self.startTime


class MGRInfoSummary:
    totalUseTime = 0
    logDataDict = {}
    logDataList = []
    __nowLogDataNo = 0
    __nowLogData = None
    __nowLogDataEndTime = 0
    logDataLimitTime = 300
    logPath = r"H:\WorkSpace\PycharmProject\MGR\Log\\"

    def __init__(self):
        pass

    @staticmethod
    def __ToTimeStamp(timeStr):
        return time.mktime(time.strptime(timeStr, "%Y-%m-%d %H:%M:%S "))

    def ShowData(self):
        for logData in self.logDataList:
            logData.PrintData()

    def ShowTotalUseTime(self):
        m, s = divmod(self.totalUseTime, 60)
        h, m = divmod(m, 60)
        print("总用时：" + "%d:%d:%d" % (h, m, s))

    def HandleLog(self):
        files = os.listdir(self.logPath)

        for file in files:
            # 遍历目标文件夹
            if file != "MGR Report":
                # print("Handling " + file)
                self.__HandleSingleLog(file)

    def __HandleSingleLog(self, file):
        f = open(self.logPath + file, 'r')

        for line in f.readlines():
            '''
            log示例：
            [INFO    ]2022-03-11 00:17:21 |GameManager.py: scriptsStart (49) | ==========ArkNights's Script Start==========
            截取]的后半段，的截取|的前半段，含空格
            '''
            logLineTime = self.__ToTimeStamp(line.split("]")[1].split("|")[0])

            if not self.__nowLogData:
                # 没有当前数据，第一次进入，创建新的数据
                self.__nowLogData = LogData(self.__nowLogDataNo, logLineTime)
                self.__nowLogDataEndTime = logLineTime
                self.__nowLogDataNo += 1
            else:
                # 有数据，对比是否超过了限制
                if logLineTime - self.__nowLogDataEndTime < self.logDataLimitTime:
                    self.__nowLogDataEndTime = logLineTime
                else:
                    self.__EndNewDataLog(self.__nowLogDataEndTime)
                    self.__nowLogData = LogData(self.__nowLogDataNo, logLineTime)
                    self.__nowLogDataEndTime = logLineTime
                    self.__nowLogDataNo += 1
        f.close()

    # def __AddNewDataLog(self,startTime):
    #     self.logDataList.append(LogData(self.__nowLogDataNo, startTime))
    #     self.__nowLogDataNo += 1

    def __EndNewDataLog(self, endTime):
        # 将当前数据封装，加入列表，并将当前数据置为空
        self.__nowLogData.SetEndTime(endTime)

        if self.__nowLogData.duration > 0:
            self.logDataList.append(self.__nowLogData)
            self.totalUseTime += self.__nowLogData.duration

        self.__nowLogData = None


mis = MGRInfoSummary()
mis.HandleLog()
mis.ShowData()
mis.ShowTotalUseTime()
