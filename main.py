# Importing required libraries
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label

# Defining the App class
class MyApp(App):

    # Function to build the layout
    def build(self):
        # Creating a layout
        layout = FloatLayout()

        # Creating a button to close the app
        close_btn = Button(text='Close App', size_hint=(.2, .1), pos=(50, 50))
        close_btn.bind(on_press=self.close_app)
        layout.add_widget(close_btn)

        # Creating a button to show introduction
        intro_btn = Button(text='Introduction', size_hint=(.2, .1), pos=(50, 150))
        intro_btn.bind(on_press=self.show_intro)
        layout.add_widget(intro_btn)

        # Returning the layout
        return layout

    # Function to close the app
    def close_app(self, instance):
        App.get_running_app().stop()

    # Function to show introduction
    def show_intro(self, instance):
        content = Label(text="Hello! Welcome to the Introduction section.")
        popup = Popup(title="Introduction", content=content, size_hint=(None, None), size=(400, 200))
        popup.open()

# Running the app
if __name__ == '__main__':
    MyApp().run()
