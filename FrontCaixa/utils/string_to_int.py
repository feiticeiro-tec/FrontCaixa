import contextlib

def string_to_int(string):
    with contextlib.suppress():
        return int(string)