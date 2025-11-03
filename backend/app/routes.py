from fastapi import APIRouter
from app.core.application.cadastrar_produto import cadastrar_produto
from app.core.application.listar_produto import listar_produtos
from app.infra.memory.produto_repository_memory import ProdutoRepositoryMemory

router = APIRouter(prefix="/produtos", tags=["Produtos"])

repo = ProdutoRepositoryMemory()

@router.post("/")
def cadastrar(nome: str, preco: float, descricao: str = ""):
    return cadastrar_produto(repo, nome, preco, descricao)

@router.get("/")
def listar():
    return listar_produtos(repo)
