from .string_strip import string_strip

def match_string(string_1:str,string_2:str) -> [bool,str]:
    """Verifica Se Duas String Deu Match e Da Um Strip Nela"""
    string_1 = string_strip(string_1)
    string_2 = string_strip(string_2)
    if string_1:
        if string_2:
            if string_1 == string_2:
                return True,string_1
            else:
                return False,string_1
        else:
            return None,''
    else:
        return None,''
        
    