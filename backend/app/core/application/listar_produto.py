from app.core.ports.i_produto_repository import IProdutoRepository

def listar_produtos(repo: IProdutoRepository):
    return repo.listar()
