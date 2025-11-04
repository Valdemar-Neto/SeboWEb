from app.core.ports.i_produto_repository import IProdutoRepository
from app.core.domain.produto import Produto
from typing import List

class ListarProdutosUseCase:
    def __init__(self, repo: IProdutoRepository):
        self.repo = repo

    def execute(self) -> List[Produto]:
        # Aqui você poderia adicionar regras de negócio antes de retornar os produtos
        return self.repo.listar()
