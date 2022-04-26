from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from FrontCaixa.utils import match_string,string_strip,generate_hash,Message
from FrontCaixa.models import Caixa
import json

class ContaPessoal(MDScreen):
    def __init__(self,*args,**kw):
        super().__init__(*args,**kw)
        MDApp.get_running_app().bind(USUARIO=self.update_labels)

    def update_labels(self,obj,caixa):
        self.ids.menu_conta.text = f'Conta: {caixa.nome}'
        self.ids.menu_email.text = f'Email: {caixa.email}'
        self.ids.menu_data.text = f'Criado: {str(caixa.date_create).split()[0]}'


    async def atualizar_senha(self,nova_senha,cnova_senha,senha_atual):
        app = MDApp.get_running_app()
        validate, nova_senha = match_string(nova_senha, cnova_senha)
        senha_atual = string_strip(senha_atual)
        if validate:
            if senha_atual:
                if app.USUARIO and app.USUARIO.check_password(senha_atual):
                    await Caixa.filter(id=app.USUARIO.id).update(senha = generate_hash(nova_senha))
                    app.USUARIO = Caixa.filter(id=app.USUARIO.id).first()
                    app.pop(Message.senha_atualizada())
                else:
                    app.pop(Message.senha_incorreta())
            else:
                app.pop(Message.senha_invalida())
        else:
            app.pop(Message.senha_nao_comina())

    def clean_inputs(self):
        self.ids.novasenha.text = ''
        self.ids.cnovasenha.text = ''
        self.ids.senhaatual.text = ''
    def save_theme(self):
        app = MDApp.get_running_app()
        theme = {
        "color_lite":self.ids.cor_fundo_claro.color,
        "color_dark":self.ids.cor_fundo_escuro.color,
        "button_negativo":self.ids.cor_button_negativo.color,
        "button_positivo":self.ids.cor_button_positivo.color,
        "texto_lite":self.ids.cor_texto_claro.color,
        "texto_dark":self.ids.cor_texto_escuro.color
        }
        with open('theme_app.json','w') as file:
            file.write(json.dumps(theme))
        app.pop(Message.theme_sera_aplicado())
        
    def on_leave(self):
        self.clean_inputs()
        super().on_leave()

    def set_colors(self):
        app = MDApp.get_running_app()
        self.ids.cor_fundo_claro.color = app.color_lite
        self.ids.cor_fundo_escuro.color = app.color_dark
        self.ids.cor_texto_claro.color = app.texto_lite
        self.ids.cor_texto_escuro.color = app.texto_dark
        self.ids.cor_button_positivo.color = app.button_positivo
        self.ids.cor_button_negativo.color = app.button_negativo

    def on_enter(self):
        self.set_colors()
        return super().on_enter()
