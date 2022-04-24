from .string_strip import string_strip

def match_password(senha,csenha):
    senha = string_strip(senha)
    csenha = string_strip(csenha)
    if senha:
        if csenha:
            if senha == csenha:
                return True,senha
            else:
                return False,senha
        else:
            return None,'csenha'
    else:
        return None,'senha'
        
    