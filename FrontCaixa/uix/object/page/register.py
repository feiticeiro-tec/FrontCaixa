from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from tortoise import run_async
from tortoise.exceptions import IntegrityError
from FrontCaixa.utils import string_strip,match_email,match_string,Message,generate_hash
from FrontCaixa.models import Caixa
import os
import hashlib

class Register(MDScreen):
    """Pagina Principal Register"""
    async def action_register(self,usuario:str,email:str,senha:str,csenha:str,senha_master:str) -> None:
        """Ação Ao Apertar o Botão Register"""
        app = MDApp.get_running_app()
        usuario = string_strip(usuario)
        validate_email, email = match_email(email)
        validate_senha, senha = match_string(senha, csenha)
        validate_master, master = match_string(generate_hash(senha_master), os.environ.get('MasterPassword'))
        if usuario:
            if validate_email:
                if validate_senha:
                    if validate_master:
                        try:
                            await Caixa.create(email,usuario,senha)
                            app.goto('Login','left')
                        except IntegrityError as error:
                            error = str(error)
                            if 'UNIQUE' in error:
                                error = error[error.rfind('.')+1:]
                                if error == 'email':
                                    app.pop(Message.email_ja_existe(email))
                    else:
                        app.pop(Message.senha_master_invalida())
                else:
                    if validate_senha == False:
                        app.pop(Message.senha_nao_comina())
                    else:
                        app.pop(Message.senha_invalida())
            else:
                if validate_email == False:
                    app.pop(Message.email_invalido(email))
                else:
                    app.pop(Message.email_nao_informado())
        else:
            app.pop(Message.usuario_invalido())

    def action_cancel(self) -> None:
        """Ação Ao Apertar o Botão Cancelar"""
        MDApp.get_running_app().goto('Login','left')

    def on_leave(self,*args) -> None:
        """Reseta Os Inputs Ao Sair Da Tela"""
        self.ids.usuario.text = ''
        self.ids.email.text = ''
        self.ids.senha.text = ''
        self.ids.csenha.text = ''
        self.ids.senha_master.text = ''
        super().on_leave(*args)