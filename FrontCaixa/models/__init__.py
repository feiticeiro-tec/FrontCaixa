from tortoise.models import Model
from tortoise import fields
from hashlib import md5
from FrontCaixa.utils import generate_hash

class Produto(Model):
    id = fields.IntField(pk=True)
    codigo = fields.CharField(50,unique=True)
    nome = fields.CharField(50,unique=True)
    description = fields.TextField()
    valor = fields.FloatField()
    date_create = fields.DatetimeField(auto_now=True)
    date_update = fields.DatetimeField(auto_now=True)
    
    @staticmethod
    async def create(codigo:str,nome:str,description:str,valor:float):
        return await super(Produto,Produto).create(codigo=codigo,nome=nome,description=description,valor=valor)

class Caixa(Model):
    id = fields.IntField(pk=True)
    nome = fields.CharField(50)
    email = fields.CharField(50,unique=True)
    senha = fields.TextField()
    
    @staticmethod
    async def create(email:str, nome:str, senha:str):
        """Cria Um Objeto Caixa e Salva No Banco"""
        return await super(Caixa,Caixa).create(email = email, nome = nome, senha = generate_hash(senha))
    
    def check_password(self,senha:str) -> bool:
        """Verifica Se a Senha Etsa Correta
        :entry: str
        :return: bool
        """
        return True if md5(f'frontcaixa{senha}'.encode()).hexdigest() == self.senha else False

class Venda(Model):
    id = fields.IntField(pk=True)
    venda_id = fields.IntField()
    produto = fields.ForeignKeyField("models.Produto", related_name="vendas")
    caixa = fields.ForeignKeyField("models.Caixa", related_name="vendas")
    
    @staticmethod
    async def create(venda_id:int,produto:Produto,caixa:Caixa):
        return await super(Venda,Venda).create(venda_id=venda_id,produto= produto, caixa = caixa)

