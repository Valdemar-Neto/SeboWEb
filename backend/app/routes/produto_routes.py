from fastapi import APIRouter, Depends, HTTPException
from fastapi import APIRouter
from app.core.application.cadastrar_produto import CadastrarProdutoUseCase
from app.core.application.listar_produtos import ListarProdutosUseCase
from app.infra.memory.produto_repository_memory import ProdutoRepositoryMemory
from app.core.schemas.produto_schema import ProdutoCreate, ProdutoResponse

router_produto = APIRouter(prefix="/produtos", tags=["Produtos"])


repo_memory = ProdutoRepositoryMemory()  # instância única
def get_repo():
    return repo_memory

@router_produto.post("/", response_model=ProdutoResponse, summary="Cadastrar um novo produto", status_code=201)
def cadastrar(produto: ProdutoCreate, repo: ProdutoRepositoryMemory = Depends(get_repo)):
    """
    Cria um novo produto no sistema do Sebo Online.
    - **nome**: nome do produto
    - **preco**: valor em reais
    - **descricao**: informações adicionais sobre o produto
    """
    try:
        use_case = CadastrarProdutoUseCase(repo)
        novo_produto = use_case.execute(produto)
        return novo_produto
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
        

@router_produto.get("/", response_model=list[ProdutoResponse], summary="Listar todos os produtos", status_code=200)
def listar(repo: ProdutoRepositoryMemory = Depends(get_repo)):
    use_case = ListarProdutosUseCase(repo)
    produtos = use_case.execute()
    return produtos