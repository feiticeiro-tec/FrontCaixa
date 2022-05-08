from kivymd.uix.dialog import BaseDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.button import ButtonBehavior
from kivy.uix.colorpicker import ColorPicker
from kivy.properties import ListProperty, ColorProperty, ObjectProperty


class SWColorPicker(BaseDialog):
    color = ColorProperty()

    def __init__(self, default, call):
        super().__init__()
        self.ids.color_picker.bind(color=self.set_color)
        r, g, b, a = default
        self.ids.color_picker.color = [r, g, b, 1]
        self.default = [r, g, b, 1]
        self.call = call

    def set_color(self, obj, color):
        r, g, b, a = color
        self.color = [r, g, b, 1]

    def action_pronto(self):
        self.dismiss()
        self.call(True, self.color)

    def action_cancelar(self):
        self.dismiss()
        self.call(False, self.default)
