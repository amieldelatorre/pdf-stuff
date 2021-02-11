import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.config import Config

from pdfActions import process_input

import threading

class MyGridLayout(Widget):
    Window.size = (680, 175)

    path = ObjectProperty(None)
    search_string = ObjectProperty(None)
    output_file_name = ObjectProperty(None)

    def press(self):
        path = self.path.text.strip()
        search_string = self.search_string.text.strip()
        output_file_name = self.output_file_name.text.strip()

        process_input_thread = threading.Thread(target=process_input(path, output_file_name, search_string))
        process_input_thread.start()
        
        self.path.text = ""
        self.search_string.text = ""
        self.output_file_name.text = ""


class kivyGui(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    kivyGui().run()