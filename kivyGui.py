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
import threading, logging

class MyGridLayout(Widget):
    Window.size = (680, 175)
    path = ObjectProperty(None)
    search_string = ObjectProperty(None)
    output_file_name = ObjectProperty(None)

    def press(self):
        path = self.path.text.strip()
        search_string = self.search_string.text.strip()
        output_file_name = self.output_file_name.text.strip()

        if output_file_name.endswith(".pdf") == False:
            output_file_name += ".pdf"

        logging.info("Main:     Creating thread")
        process_input_thread = threading.Thread(target=self.handle_input, args=(path, output_file_name, search_string), daemon=True)
        logging.info("Main:     Starting thread")
        process_input_thread.start()

        logging.info("Main:     While waiting for thread")
        self.search_string.text = "" 
        self.output_file_name.text = ""
        self.path.text = ""

    def handle_input(self, path, output_file_name, search_string):
        logging.info("Worker:     Arrived at handle input")

        process_input(path, output_file_name, search_string)

    
class kivyGui(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    kivyGui().run()