from kivymd.uix.screen import MDScreen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.clock import Clock
from kivy.properties import NumericProperty

class Index(MDScreen):
    """Pagina Principal Index"""
    sub_total = NumericProperty()
    def on_enter(self):
        self.add_item_table([
            ["1","077","Cocacola","5.60","3",str(5*3)],
            ["1","077","Cocacola","5.60","3",str(5*3)],
            ["1","077","Cocacola","5.60","3",str(5*3)],
            ["1","077","Cocacola","5.60","3",str(5*3)],
            ["1","077","Cocacola","5.60","3",str(5*3)],
            ["1","077","Cocacola","5.60","3",str(5*3)],
        ],True)
        return super().on_enter()

    def add_item_table(self,item, lista=False):
        def editar(self,item, lista=False):
            if len(self.ids.table.children) == 1:
                self.ids.table.children[0].add_row(item)
                self.sub_total += float(item[5])
            else:
                data_tables = MDDataTable(
                    check=True,
                    column_data=[
                        ("No.", dp(30)),
                        ("Codigo", dp(20)),
                        ("Nome", dp(20)),
                        ("U. Valor", dp(20)),
                        ("Unidades", dp(20)),
                        ("Total", dp(20))
                    ],
                    row_data=item if lista else [item],
                    pos_hint={'center_x':0.5}
                )
                self.ids.table.add_widget(data_tables)
            self.sub_total = sum(float(item[5]) for item in self.ids.table.children[0].row_data)
        Clock.schedule_once(lambda *args:editar(self,item,lista))
