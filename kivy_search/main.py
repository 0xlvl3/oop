from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen

import wikipedia
import requests


# This import is how we connect our Python file to Kivy to build our App.
from kivy.lang import Builder

# Loading our Kivy file to Python.
Builder.load_file("frontend.kv")


class FirstScreen(Screen):
    def get_image_link(self):
        # Get user query from TextInput
        query = self.manager.current_screen.ids.user_query.text

        # Get wikipedia page and get first image link
        page = wikipedia.page(query)
        image_link = page.images[0]
        return image_link

    def download_image(self):
        # Download the image.
        req = requests.get(self.get_image_link())
        image_path = "files/image.jpg"
        with open(image_path, "wb") as file:
            file.write(req.content)
        return image_path

    def set_image(self):
        # Set image in the Image widget
        self.manager.current_screen.ids.img.source = self.download_image()


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()
