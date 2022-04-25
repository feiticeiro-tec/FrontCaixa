from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty
class SWInputWithTitle(MDBoxLayout):
    title = StringProperty('')
    text = StringProperty('')
    def set_text(self,text):
        self.text = text