from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.clock import Clock
from kivy.properties import NumericProperty,ColorProperty,ListProperty

class MDDataTable(MDDataTable):
    def set_default_first_row(self, interval: int or float) -> None:
        try:
            super().set_default_first_row(interval)
        except IndexError:
            ...

class SWTableWithTitle(MDBoxLayout):
    sub_total = NumericProperty()
    color=ColorProperty([35/255,35/255,45/255,1])
    text_color=ColorProperty([1,1,1,1])
    data = ListProperty()
    def on_data(self,obj,valor):
        def editar(self,valor):
            self.ids.table.clear_widgets()
            self.ids.table.add_widget(
                MDDataTable(
                check=True,
                column_data=[
                        ("No.", dp(30)),
                        ("Codigo", dp(20)),
                        ("Nome", dp(20)),
                        ("U. Valor", dp(20)),
                        ("Unidades", dp(20)),
                        ("Total", dp(20))
                    ],
                row_data=valor,
                pos_hint={'center_x':0.5})
            )
            self.sub_total = sum(float(item[5]) for item in self.ids.table.children[0].row_data)
        Clock.schedule_once(lambda *args:editar(self,valor))