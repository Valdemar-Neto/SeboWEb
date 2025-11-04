# app/core/application/cadastrar_produto.py

from app.core.domain.produto import Produto
from app.core.ports.i_produto_repository import IProdutoRepository
from app.core.schemas.produto_schema import ProdutoCreate, ProdutoResponse


class CadastrarProdutoUseCase:
    """
    Caso de uso: Cadastrar Produto

    Responsável por validar e registrar um novo produto no sistema.
    """

    def __init__(self, repo: IProdutoRepository):
        self.repo = repo

    def execute(self, data: ProdutoCreate) -> ProdutoResponse:
        # --- Validações ---
        if not data.nome.strip():
            raise ValueError("O nome do produto não pode estar vazio.")
        if data.preco <= 0:
            raise ValueError("O preço do produto deve ser maior que zero.")

        # --- Verifica duplicidade ---
        produtos_existentes = self.repo.listar()
        if any(p.nome.lower() == data.nome.lower() for p in produtos_existentes):
            raise ValueError("Já existe um produto com esse nome cadastrado.")

        # --- Cria a entidade ---
        produto = Produto(
            id=0,
            nome=data.nome.strip(),
            preco=data.preco,
            descricao=data.descricao.strip()
        )

        salvo = self.repo.salvar(produto)

        # --- Retorna schema de resposta ---
        return ProdutoResponse(
            id=salvo.id,
            nome=salvo.nome,
            preco=salvo.preco,
            descricao=salvo.descricao
        )
