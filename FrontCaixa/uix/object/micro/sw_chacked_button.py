from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.behaviors import CircularRippleBehavior
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import BooleanProperty, StringProperty


class SWCheckedButton(CircularRippleBehavior, ButtonBehavior, MDBoxLayout):
    checked = BooleanProperty(False)
    icon = StringProperty('checkbox-blank-outline')

    def __init__(self, checked, *args, **kw):
        super().__init__(*args, **kw)
        self.checked = checked

    def on_checked(self, obj, checked):
        self.icon = 'checkbox-intermediate' if checked else 'checkbox-blank-outline'

    def on_release(self):
        self.checked = not self.checked
        return super().on_release()
