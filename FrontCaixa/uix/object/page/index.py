from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.core.window import Window
from kivy.metrics import dp


class Index(MDScreen):
    """Pagina Principal Index"""
    def __init__(self,*args,**kw):
        super().__init__(*args,**kw)
        self._keyboard = Window.request_keyboard(self._keyborad_close,self)
    
    def on_enter(self):
        self.ids.table.add_item_table([
            ["1","077","Cocacola","5.60","3",str(5*3)],
            ["1","077","Cocacola","5.60","3",str(5*3)],
            ["1","077","Cocacola","5.60","3",str(5*3)],
            ["1","077","Cocacola","5.60","3",str(5*3)],
            ["1","077","Cocacola","5.60","3",str(5*3)],
            ["1","077","Cocacola","5.60","3",str(5*3)],
        ],True)
        self._keyboard.bind(on_key_down = self._on_keyboard_down)
        return super().on_enter()
    def on_leave(self):
        self._keyboard.unbind(on_key_down = self._on_keyboard_down)
        super().on_leave()
    def _keyborad_close(self,*args):
        print('>>',args)
    def _on_keyboard_down(self,keyboard,press,*args):
        print(press[1])
        if press[1] == 'f1':
            print(True)
        elif press[1] == 'f2':
            print(True)
        elif press[1] == 'f3':
            print(True)
        elif press[1] == 'f4':
            print(True)
        elif press[1] == 'f5':
            print(True)
        elif press[1] == 'f6':
            print(True)
        elif press[1] == 'f7':
            print(True)
        elif press[1] == 'f8':
            print(True)
        elif press[1] == 'f9':
            MDApp.get_running_app().goto('Atualizar Produtos','down')
            
        elif press[1] == 'f10':
            print(True)
        
