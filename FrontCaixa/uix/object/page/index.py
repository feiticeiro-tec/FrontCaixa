from kivymd.uix.screen import MDScreen
from kivy.metrics import dp


class Index(MDScreen):
    """Pagina Principal Index"""
    def on_enter(self):
        self.ids.table.add_item_table([
            ["1","077","Cocacola","5.60","3",str(5*3)],
            ["1","077","Cocacola","5.60","3",str(5*3)],
            ["1","077","Cocacola","5.60","3",str(5*3)],
            ["1","077","Cocacola","5.60","3",str(5*3)],
            ["1","077","Cocacola","5.60","3",str(5*3)],
            ["1","077","Cocacola","5.60","3",str(5*3)],
        ],True)
        return super().on_enter()

    
