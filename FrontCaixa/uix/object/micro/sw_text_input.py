from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty, BooleanProperty, NumericProperty, ListProperty
from kivy.metrics import dp


class SWTextInput(MDBoxLayout):
    pc_style = BooleanProperty(False)  # Usado Para Definir Style Para PC
    hint_text = StringProperty('')
    text = StringProperty('')
    bold = BooleanProperty(False)
    password = BooleanProperty(False)
    font_style = StringProperty('Overline')
    font_size = NumericProperty(dp(16))
    text_color = ListProperty([0, 0, 0, 1])

    def set_text(self, text):
        """Atualiza o Texto"""
        self.text = text

    def on_pc_style(self, obj, valor):
        """Aplica o Style Para Visualiza Em Computador"""
        if valor:
            self.font_size = dp(18)
            self.bold = False
