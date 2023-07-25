from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty




class Moje_Przepisy(Screen):
    pass

class ChlebZytni(Screen):
    pass

class Pizza(Screen):
    pass

class ChlebZiarna(Screen):
    pass

class Drozdzowka(Screen):
    przygotowanie = ObjectProperty(None)
    skladniki = ObjectProperty(None)
    def press(self):
        przygotowanie = self.przygotowanie.text
        skladniki = self.skladniki.text
        self.add_widget(Label(text='-100 gram cukru\n-150 gram mąki\n-100 gram zimnego masła\n\n\n\n\n\n\n\n\n\nWymieszaj składniki tak aby powstały grudki. Posyp owoce.'))
        self.przygotowanie.text = ''
        self.skladniki.text = ''


class WindowManager(ScreenManager):
    pass





kv = Builder.load_file('layout.kv')

class MojaApkaApp(App):
    def build(self):
        return kv

if __name__ == '__main__':
    MojaApkaApp().run()