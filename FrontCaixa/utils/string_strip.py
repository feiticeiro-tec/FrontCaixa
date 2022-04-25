import contextlib

def string_strip(string) -> str or None:
    """Remove Os Espaços Iniciais e Finais De Uma String"""
    with contextlib.suppress():
        string = string.strip()
        if string:
            return string
