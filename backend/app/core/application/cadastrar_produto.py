from app.core.domain.produto import Produto
from app.core.ports.i_produto_repository import IProdutoRepository

def cadastrar_produto(repo: IProdutoRepository, nome: str, preco: float, descricao: str = ""):
    produto = Produto(id=0, nome=nome, preco=preco, descricao=descricao)
    return repo.salvar(produto)
