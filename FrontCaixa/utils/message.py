class Message:
    
    @staticmethod
    def usuario_invalido() -> str:
        return 'Usuario Invalida!'

    @staticmethod
    def email_invalido(email) -> str:
        return f'Email {email} não é valido!'

    @staticmethod
    def email_nao_informado() ->str:
        return 'Email não informado!'
    
    @staticmethod
    def email_ja_existe(email) ->str:
        return f'Email "{email}" ja existe!'
    
    @staticmethod
    def senha_nao_comina() ->str:
        return 'Senha não cominou!'
    
    @staticmethod
    def senha_invalida() ->str:
        return 'Senha Invalida!'
    
    @staticmethod
    def senha_incorreta() ->str:
        return 'Senha Incorreta!'

    @staticmethod
    def senha_atualizada() -> str:
        return 'Senha Atualizada!'
    
    @staticmethod
    def senha_master_invalida() ->str:
        return 'Senha Master Invalida!'
    
    @staticmethod
    def email_ou_senha_invalida() ->str:
        return 'Email ou Senha Invalida!'

    @staticmethod
    def theme_sera_aplicado() -> str:
        return 'O Tema Será Aplicado Ao Reiniciar o Programa!'
