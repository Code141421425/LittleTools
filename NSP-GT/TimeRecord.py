from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from Common import TimeCounter


class TimeRecord(BoxLayout):
    user_name = "",
    time_type = StringProperty(),
    time_unit_price = -1,
    is_overtime = False,
    overtime_rate = 0.5,
    remaining_time = 0,
    time_counter = TimeCounter()

    def __init__(self,*args, **kwargs):
        super(TimeRecord, self).__init__(*args, **kwargs)

    def TimeRecordInit(self,
                       user_name,
                       time_type,
                       time_unit_price,
                       is_overtime=False,
                       overtime_rate=0.5,
                       remaining_time=0):

        self.user_name = user_name
        self.time_type = time_type
        self.time_unit_price = time_unit_price
        self.is_overtime = is_overtime
        self.overtime_rate = overtime_rate
        self.remaining_time = remaining_time
        self.time_counter = TimeCounter()

    def Start(self):
        self.time_counter.Start()

    def Pause(self):
        self.time_counter.Pause()

    def Reset(self):
        self.time_counter.Reset()
        self.remaining_time = 0

    def GetRemainingTime(self):
        elapsed_time = self.time_counter.GetElapsedTime()
        if elapsed_time > 0:
            self.remaining_time -= elapsed_time
            if self.remaining_time < 0:
                self.remaining_time = 0
        return self.remaining_time * self.overtime_rate * self.time_unit_price  # Convert to time cost
