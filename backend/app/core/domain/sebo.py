from dataclasses import dataclass

@dataclass
class SEBO:
    id: int
    nome: str
    descricao: str
    dono_id: int