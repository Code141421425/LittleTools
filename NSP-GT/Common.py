import time


class TimeCounter:
        startTime = None
        interruptTimePoint = 0
        interruptTime = 0

        totalTime = 0
        lastTime = 0

        def __init__(self, startTime=None):
            if startTime:
                self.startTime = startTime
            else:
                self.startTime = time.time()
            self.stop = False

            self.totalTime = 0

            self.now_time = None

        def Start(self):
            self.stop = False
            self.lastTime = time.time()

        def ResetTime(self):
            self.totalTime = 0
            self.stop = True

        def Pause(self):
            self.stop = True

        def Continue(self):
            self.stop = False

        def return_pass_time(self):
            if not self.stop:
                self.totalTime += time.time() - self.lastTime
                self.lastTime = time.time()
            else:
                pass

            if not self.startTime:
                return "0:0:0"
            else:
                return "{}:{}:{}".format(
                    int(self.totalTime / 3600),
                    int((self.totalTime % 3600) / 60),
                    int(self.totalTime % 60)
                )

