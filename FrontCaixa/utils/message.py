class Message:
    
    @staticmethod
    def usuario_invalido():
        return 'Usuario Invalida!'

    @staticmethod
    def email_invalido(email):
        return f'Email {email} não é valido!'

    @staticmethod
    def email_nao_informado():
        return 'Email não informado!'
    
    @staticmethod
    def email_ja_existe(email):
        return f'Email "{email}" ja existe!'
    
    @staticmethod
    def senha_nao_comina():
        return 'Senha não cominou!'
    
    
    @staticmethod
    def senha_invalida():
        return 'Senha Invalida!'
    
    @staticmethod
    def senha_master_invalida():
        return 'Senha Master Invalida!'
    
    @staticmethod
    def email_ou_senha_invalida():
        return 'Email ou Senha Invalida!'