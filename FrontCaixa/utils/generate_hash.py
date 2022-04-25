import hashlib
def generate_hash(string) -> str:
    """Gera Uma Hash"""
    return hashlib.md5(f'frontcaixa{string}'.encode()).hexdigest()