from kivymd.uix.screen import MDScreen
from FrontCaixa.uix.object.macro.sw_color_picker import SWColorPicker

class ContaPessoal(MDScreen):
    def open_color(self,button):
        self.picker_button = button
        picker_color = SWColorPicker(button.md_bg_color,self.set_color)
        picker_color.open()

    def set_color(self,action,color):
        self.picker_button.md_bg_color = color
        self.picker_button.text_color = color
