from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from FrontCaixa.utils import string_strip,Message,match_email
from FrontCaixa.models import Caixa

class Login(MDScreen):
    """Pagina Principal Login"""
    def action_register(self) -> None:
        """Ação Ao Apertar o Botão De Registrar"""
        MDApp.get_running_app().goto('Register','right')
    
    async def action_login(self,email:str,senha:str) -> None:
        """Ação Ao Apertar o Botão De Login"""
        validate_email, email = match_email(email)
        senha = string_strip(senha)
        if validate_email:
            if senha:
                caixa = await Caixa.filter(email = email).first()#Filtra Caixa Por Email
                if caixa and caixa.check_password(senha):#Verifica Se o Caixa Existe e Verifica Se a Senha Esta Correta
                    MDApp.get_running_app().goto('Index','up')#Troca De Tela Pra o Index
                else:
                    print(Message.email_ou_senha_invalida())
            else:
                print(Message.senha_invalida())
        else:
            if validate_email == False:
                print(Message.email_invalido(email))
            else:
                print(Message.email_nao_informado())
    
    def on_leave(self) -> None:
        """Reseta Os Inputs Ao Sair Da Tela"""
        self.ids.email.text = ''
        self.ids.senha.text = ''
        return super().on_leave()

        