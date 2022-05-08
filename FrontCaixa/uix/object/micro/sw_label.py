from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty,ColorProperty
class SWLabel(MDBoxLayout):
    text = StringProperty('')
    text_start = StringProperty('')
    text_end = StringProperty('')