from kivymd.app import MDApp
from kivymd.uix.dialog import BaseDialog
from kivy.metrics import dp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.list import OneLineIconListItem

class AddProduto(BaseDialog):
    def __init__(self,*args,**kw):
        super().__init__(*args,**kw)
        menu_items = [
            {
                "viewclass": "OneLineIconListItem",
                "icon": "git",
                "text": f"Item {i}",
                "height": dp(56),
                "on_release": lambda x=f"Item {i}": self.set_item(x),
            } for i in range(5)]

        self.menu = MDDropdownMenu(
            caller=self.ids.drop_item,
            items=menu_items,
            position="center",
            width_mult=4)
            
        self.menu.bind()
        

    def set_item(self, text_item):
        self.ids.drop_item.set_item(text_item)
        self.menu.dismiss()