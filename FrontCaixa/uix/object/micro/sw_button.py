from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivy.properties import StringProperty,BooleanProperty,ListProperty,NumericProperty
from kivy.metrics import dp

class SWButton(RectangularRippleBehavior,ButtonBehavior,MDBoxLayout):
    pc_style = BooleanProperty(False)
    text = StringProperty('')
    font_style = StringProperty('OverLine')
    bold = BooleanProperty(True)
    font_size = NumericProperty(dp(16))
    text_color = ListProperty([0,0,0,1])
    def on_pc_style(self,obj,value):
        if value:
            self.font_size = dp(18)
            self.bold = False

            