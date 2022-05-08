from functools import partial

from tortoise import run_async
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.menu import MDDropdownMenu

from FrontCaixa.models import Produto, Venda


class SWPopAddProduto(MDBoxLayout):
    def __init__(self, call, _parent=None):
        super().__init__()
        self.call = call
        self._parent = _parent

    async def filter_by(self, text):
        self.text_filter = text
        produtos_codigo = await Produto.filter(codigo__icontains=text)
        produtos_nome = await Produto.filter(nome__icontains=text)
        produtos = list(set([*produtos_codigo, *produtos_nome]))
        items = [{
            "text": produto.nome,
            "viewclass": 'OneLineListItem',
            'on_release': partial(self.pre_call, produto)
        } for produto in produtos]

        self.menu = MDDropdownMenu(
            caller=self.ids.button,
            items=items,
            width_mult=4
        )
        self.menu.open()

    def pre_call(self, produto):
        app = MDApp.get_running_app()
        self.menu.dismiss()
        if app.VENDA != None:
            run_async(Venda.create(app.VENDA, produto, app.USUARIO))
            run_async(self.get_datas())

    async def get_datas(self):
        app = MDApp.get_running_app()
        vendas = await Venda.filter(venda_id=app.VENDA).values('produto__codigo', 'produto__nome', 'produto__valor', 'produto__id')
        data = [[f"{venda['produto__id']}", f"{venda['produto__codigo']}", f"{venda['produto__nome']}",
                 f"{venda['produto__valor']}", "1", f"{venda['produto__valor']}"] for index, venda in enumerate(vendas)]
        self.call(data)
        if self._parent:
            self._parent.auto_dismiss = True
            self._parent.dismiss()
