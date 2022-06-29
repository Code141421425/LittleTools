from kivy.config import Config
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class Controller(BoxLayout):
    count = 0

    def AddOne(self):
        self.count += 1
        self.SyncTextLabel()

    def Clear(self):
        self.count = 0
        self.SyncTextLabel()

    def SyncTextLabel(self):
        self.ids.count_Label.text = self.count.__str__()


class Counter(App):

    def build(self):
        return Controller()


if __name__ == '__main__':
    Config.set('graphics', 'width', '350')
    Config.set('graphics', 'height', '200')

    Counter().run()