from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class MainApp(MDApp):
     def build(self):
        return MDLabel(text="Hello, Ivan", halign="center")


MainApp().run()