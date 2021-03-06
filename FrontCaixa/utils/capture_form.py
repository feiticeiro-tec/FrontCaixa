from .string_to_float import string_to_float
from .string_strip import string_strip
from .string_to_int import string_to_int

def capture_form(form:dict,mapa:dict={}) -> dict:
    """Recebe Um Dict e Um Mapa e Faz A Validação
    :form: {'key':valor}
    :map: {'key':'flaot','key':'strip','key':'int'}
    :return: dict
    """
    data = {}
    for key,valor in mapa.items():
        value = form.get(key)
        if value:
            if valor == 'float':
                data[key] = string_to_float(value)
            elif valor == 'strip':
                data[key] = string_strip(value)
            elif valor == 'int':
                data[key] = string_to_int(value)
    return data

