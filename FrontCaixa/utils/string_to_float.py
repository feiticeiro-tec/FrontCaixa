import contextlib

def string_to_float(string) -> float or None:
    """Converte Uma String Para Flaot"""
    with contextlib.suppress():
        return float(string)