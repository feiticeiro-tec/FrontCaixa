from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty,ColorProperty
from FrontCaixa.uix.object.macro.sw_color_picker import SWColorPicker

class SWPickerWithLabel(MDBoxLayout):
    text = StringProperty('')
    color = ColorProperty()

    def open_color(self,button):
        picker_color = SWColorPicker(self.color,self.set_color)
        picker_color.open()

    def set_color(self,action,color):
        self.color = color