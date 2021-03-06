from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.behaviors import RectangularRippleBehavior
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import StringProperty,BooleanProperty,ListProperty,NumericProperty
from kivy.metrics import dp

class SWButton(RectangularRippleBehavior,ButtonBehavior,MDBoxLayout):
    pc_style = BooleanProperty(False) #Usado Para Definir Style Para PC
    text = StringProperty('')
    font_style = StringProperty('OverLine')
    bold = BooleanProperty(True)
    font_size = NumericProperty(dp(16))
    text_color = ListProperty([0,0,0,1])
    def on_pc_style(self,obj,value):
        """Aplica o Style Para Visualiza Em Computador"""
        if value:
            self.font_size = dp(18)
            self.bold = False

            