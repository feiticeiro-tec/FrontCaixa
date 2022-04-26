from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty,ColorProperty
class SWInputWithTitle(MDBoxLayout):
    title = StringProperty('')
    text = StringProperty('')
    color = ColorProperty([24/255,24/255,35/255,1])
    text_color = ColorProperty([1,1,1,1])
    def set_text(self,text):
        self.text = text