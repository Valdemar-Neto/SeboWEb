from app.core.domain.produto import Produto
from app.core.ports.i_sebo_repository import ISeboRepository

class AdicionarProdutoSeboUseCase:
    def __init__(self, sebo_repo: ISeboRepository):
        self.sebo_repo = sebo_repo
        self.produto_counter = 1  # contador interno para IDs de produtos

    def execute(self, sebo_id: int, produto_data: dict):
        sebo = self.sebo_repo.get_by_id(sebo_id)
        if not sebo:
            raise ValueError("Sebo não encontrado")

        # Adiciona o id ao produto
        produto_data['id'] = self.produto_counter
        self.produto_counter += 1

        produto = Produto(**produto_data)
        sebo.produtos.append(produto)
        return produto

