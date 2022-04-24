from kivymd.app import MDApp
from FrontCaixa.utils import string_strip,match_email,match_password,Message
from kivymd.uix.screen import MDScreen
from FrontCaixa.models import Caixa
from tortoise import run_async
from tortoise.exceptions import IntegrityError
import os
import hashlib


class Register(MDScreen):
    
    async def action_register(self,usuario,email,senha,csenha,senha_master):
        usuario = string_strip(usuario)
        validate_email, email = match_email(email)
        validate_senha, senha = match_password(senha, csenha)
        validate_master, master = match_password(hashlib.md5(f'frontcaixa{senha_master}'.encode()).hexdigest(), os.environ.get('MasterPassword'))
        if usuario:
            if validate_email:
                if validate_senha:
                    if validate_master:
                        try:
                            await Caixa.create(email,usuario,senha)
                            MDApp.get_running_app().goto('Login','left')
                        except IntegrityError as error:
                            error = str(error)
                            if 'UNIQUE' in error:
                                error = error[error.rfind('.')+1:]
                                if error == 'email':
                                    print(Message.email_ja_existe(email))
                    else:
                        print(Message.senha_master_invalida())
                else:
                    if validate_senha == False:
                        print(Message.senha_nao_comina())
                    else:
                        print(Message.senha_invalida())
            else:
                if validate_email == False:
                    print(Message.email_invalido(email))
                else:
                    print(Message.email_nao_informado())
        else:
            print(Message.usuario_invalido())

    def action_cancel(self):
        MDApp.get_running_app().goto('Login','left')

    def on_leave(self,*args):
        self.ids.usuario.text = ''
        self.ids.email.text = ''
        self.ids.senha.text = ''
        self.ids.csenha.text = ''
        self.ids.senha_master.text = ''
        super().on_leave(*args)