from app.core.ports.i_produto_repository import IProdutoRepository
from app.core.domain.produto import Produto
from typing import List

class ProdutoRepositoryMemory(IProdutoRepository):
    def __init__(self):
        self._db = []
        self._id_counter = 1

    def salvar(self, produto: Produto) -> Produto:
        produto.id = self._id_counter
        self._id_counter += 1
        self._db.append(produto)
        return produto

    def listar(self) -> List[Produto]:
        return self._db
