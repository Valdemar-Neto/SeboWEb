from dataclasses import dataclass, field
from typing import List


@dataclass
class Sebo:
    id: int
    nome: str
    descricao: str
    dono_id: int
    produtos: List = field(default_factory=list)