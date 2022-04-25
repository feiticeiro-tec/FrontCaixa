from kivymd.app import MDApp
from kivy.properties import ListProperty
from tortoise import Tortoise,run_async
from FrontCaixa.uix.object.macro import ManagerPage
from FrontCaixa.models import *
import os
import json

class FrontCaixa(MDApp):
    primary_color_back = ListProperty([35/255,35/255,35/255,1])
    primary_color_red_button = ListProperty([0.9,0.6,0.6,1])
    primary_color_green_button = ListProperty([0.6,0.9,0.6,1])
    def __init__(self):
        super().__init__()
        run_async(self.start_tortoise())
        self.load_env()
        self.load_theme()
        self.load_kvs()
        self.mp = ManagerPage()

    def load_kvs(self):
        path = './FrontCaixa/uix/kv'
        for pasta in os.listdir(path):
            for file in os.listdir(f'{path}/{pasta}'):
                print(file)
                self.load_kv(f'{path}/{pasta}/{file}')
    
    def load_env(self):
        with open('config_app.json') as env:
            data = json.loads(env.read())
        for key,value in data.items():
            os.environ[key] = value

    def load_theme(self):
        with open('theme_app.json') as theme:
            data = json.loads(theme.read())
        for key,value in data.items():
            if key in ('primary_color_back','primary_color_red_button','primary_color_green_button') and type(value) == list:
                exec(f'self.{key} = {value}')
    
    def goto(self,name,direction):
        self.mp.transition.direction = direction
        self.mp.current = name

    def build(self):
        return self.mp

    async def start_tortoise(self):
        await Tortoise.init(
            db_url='sqlite://database.db',
            modules={'models':['FrontCaixa.models']}
        )
        await Tortoise.generate_schemas()
        """
        produto = await Produto.create('007','agente','agente fbi',1.50)
        caixa = await Caixa.create('silvio@gmail.com','silvio','senha123')
        venda = await Venda.create(produto,caixa)
        """