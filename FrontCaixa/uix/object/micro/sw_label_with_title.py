from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty,ColorProperty
class SWLabelWithTitle(MDBoxLayout):
    title = StringProperty('')
    text = StringProperty('')
    text_start = StringProperty('')
    text_end = StringProperty('')
    color = ColorProperty([24/255,24/255,35/255,1])
    text_color = ColorProperty([1,1,1,1])
    