import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.factory import Factory
from kivy.core.window import Window
from kivy.config import Config
from pdfActions import process_input
import threading, logging

class PopupBox(Popup):
    pop_up_text = ObjectProperty(None)
    def update_popup_text(self, message):
        self.pop_up_text.text = message

class MyGridLayout(Widget):
    Window.size = (1300, 600)
    path = ObjectProperty(None)
    search_string = ObjectProperty(None)
    output_file_name = ObjectProperty(None)

    def press(self):
        path = self.path.text.strip()
        search_string = self.search_string.text.strip()
        output_file_name = self.output_file_name.text.strip()
        
        if path == "" and (search_string == "" or output_file_name == ""):
            pop_message = "Please enter details..."
            self.show_popup(pop_message)
            return

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
        pop_message = "Loading..."
        self.show_popup(pop_message)

        result = process_input(path, output_file_name, search_string)
        self.dismiss_popup()

        self.show_popup(result)


    def show_popup(self, pop_message):
        self.pop_up = Factory.PopupBox()
        self.pop_up.update_popup_text(pop_message)
        self.pop_up.open()

    def dismiss_popup(self):
        self.pop_up.dismiss()

    
class kivyGui(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    kivyGui().run()