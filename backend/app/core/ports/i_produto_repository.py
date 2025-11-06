from abc import ABC, abstractmethod
from typing import List
from app.core.domain.produto import Produto

class IProdutoRepository(ABC):

    @abstractmethod
    def salvar(self, produto: Produto) -> Produto:
        pass

    @abstractmethod
    def listar(self) -> List[Produto]:
        pass
