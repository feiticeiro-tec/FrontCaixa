import contextlib

def string_to_int(string) -> int or None:
    """Converte Uma String Para Int"""
    with contextlib.suppress():
        return int(string)