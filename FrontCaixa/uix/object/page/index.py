from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivy.core.window import Window
from kivy.metrics import dp

from FrontCaixa.uix.object.macro.sw_pop import SWPop
from FrontCaixa.uix.object.macro.sw_pop_add_produto import SWPopAddProduto
from FrontCaixa.models import Venda
from tortoise import run_async
from functools import partial

class Index(MDScreen):
    """Pagina Principal Index"""
    pop = None
    def __init__(self,*args,**kw):
        super().__init__(*args,**kw)
        self._keyboard = Window.request_keyboard(self._keyborad_close,self)
        MDApp.get_running_app().bind(USUARIO=self.update_labels)

    def update_labels(self,obj,caixa):
        self.ids.info_conta.text = f'Conta: {caixa.nome}'
    
    def on_enter(self):
        self.update_table([
            ["1","077","Cocacola","5.60","3",str(5*3)],
            ["1","077","Cocacola","5.60","3",str(5*3)],
            ["1","077","Cocacola","5.60","3",str(5*3)],
            ["1","077","Cocacola","5.60","3",str(5*3)],
            ["1","077","Cocacola","5.60","3",str(5*3)],
            ["1","077","Cocacola","5.60","3",str(5*3)],
        ])
        
        self._keyboard.bind(on_key_down = self._on_keyboard_down)
        return super().on_enter()

    def update_table(self,data):
        #self.ids.table.data = data
        ...

    def on_leave(self):
        self._keyboard.unbind(on_key_down = self._on_keyboard_down)
        return super().on_leave()

    def _keyborad_close(self,*args):
        print('>>',args)
    def add_venda(self,produto):
        self.update_table([["1","077","Cocacola","5.60","3",str(5*3)]])
        
    def _on_keyboard_down(self,keyboard,press,*args):
        print(press[1])
        if not self.pop:
            if press[1] == 'f1':
                MDApp.get_running_app().goto('Conta Pessoal','down')
            elif press[1] == 'f2':
                print(True)
                self.pop = SWPop(SWPopAddProduto,'Adicionar Produto',_parent=self,auto_dismiss=False,args=[self.update_table])
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