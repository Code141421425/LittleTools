import os

from kivy.app import App
from kivy.config import Config
from kivy.lang import Builder
from kivy.clock import mainthread
from kivy.clock import Clock

from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

from ZcwPyUtility.kivy.TimeCounter import TimeCounter


class UIController(BoxLayout):
    def __init__(self, *args, **kwargs):
        super(UIController, self).__init__(*args, **kwargs)


class GTR(App):
    timeCounter = None
    uiController = None
    timeLock = False
    passTime = StringProperty()

    def build(self):
        self.uiController = UIController()
        self.timeLock = True

        self.passTime = "0:0:0"
        self.timeCounter = TimeCounter()
        Clock.schedule_interval(self._update_clock, 1)

        return self.uiController

    def _update_clock(self, dt):
        if not self.timeLock:
            self.passTime = self.timeCounter.return_pass_time()

    def TimeStart(self):
        self.timeLock = False
        self.timeCounter.Start()

    def TimePause(self):
        self.timeLock = True
        self.timeCounter.Pause()

    def TimeReSet(self):
        self.timeCounter.ResetTime()
        self.timeLock = True
        self.passTime = "0:0:0"


if __name__ == '__main__':
    Config.set('graphics', 'width', '400')
    Config.set('graphics', 'height', '180')

    GTR().run()

