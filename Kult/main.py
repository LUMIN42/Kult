import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager


class HomeScreen(Screen):
    pass


class RoundButton(Button):
    pass

GUI = Builder.load_file("main.kv")


class MainApp(App):
    def Build(self):
        return GUI


MainApp().run()