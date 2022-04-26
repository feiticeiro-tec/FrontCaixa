from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from FrontCaixa.utils import match_string,string_strip,generate_hash,Message
from FrontCaixa.models import Caixa

class ContaPessoal(MDScreen):
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
    
    def on_leave(self):
        self.clean_inputs()
        super().on_leave()

                    
            

