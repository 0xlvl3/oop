from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

from file_stack import file_link

Builder.load_file("frontend.kv")


class CameraScreen(Screen):
    def start(self):
        self.ids.camera.text = "Took a screenshot"
        self.ids.start_btn.text = "UHHHHHH"

    def stop(self):
        self.ids.camera.text = "Capture what? WSL doesn't have access to a camera"
        self.ids.start_btn.text = "Lol why is this changing now"

    def capture(self):
        self.manager.current = "image_screen"


class ImageScreen(Screen):
    def switch(self):
        self.manager.current = "camera_screen"


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()
