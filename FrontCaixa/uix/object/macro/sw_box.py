from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty, ColorProperty


class SWBox(MDBoxLayout):
    text = StringProperty()
    text_color = ColorProperty([0, 0, 0, 1])
