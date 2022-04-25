from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty
class SWLabelWithTitle(MDBoxLayout):
    title = StringProperty('')
    text = StringProperty('')
    text_start = StringProperty('')
    text_end = StringProperty('')
    