from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from FrontCaixa.utils import string_strip,Message,match_email
from FrontCaixa.models import Caixa

class Login(MDScreen):
    def action_register(self):
        MDApp.get_running_app().goto('Register','right')
    
    async def action_login(self,email,senha):
        validate_email, email = match_email(email)
        senha = string_strip(senha)
        if validate_email:
            if senha:
                caixa = await Caixa.filter(email = email).first()
                if caixa and caixa.check_password(senha):
                    MDApp.get_running_app().goto('Index','up')
                else:
                    print(Message.email_ou_senha_invalida())
            else:
                print(Message.senha_invalida())
        else:
            if validate_email == False:
                print(Message.email_invalido(email))
            else:
                print(Message.email_nao_informado())
    
    def on_leave(self):
        self.ids.email.text = ''
        self.ids.senha.text = ''
        return super().on_leave()

        