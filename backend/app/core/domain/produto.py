from dataclasses import dataclass

@dataclass
class Produto:
    id: int
    nome: str
    preco: float
    descricao: str = ""