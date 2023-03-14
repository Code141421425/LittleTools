import os

from kivy.app import App
from kivy.config import Config
from kivy.lang import Builder
from kivy.clock import mainthread
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

from Calendar import Calendar


class UIController(BoxLayout):
    def __init__(self, *args, **kwargs):
        super(UIController, self).__init__(*args, **kwargs)


class RL(App):
    uiController = None

    def build(self):
        self.uiController = UIController()

        return self.uiController


RL().run()

