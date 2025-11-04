from fastapi import APIRouter, Depends, HTTPException
from app.core.application.cadastrar_sebo import CadastrarSeboUseCase
from app.core.application.listar_sebos import ListarSeboUseCase
from app.core.application.adicionar_produto import AdicionarProdutoSeboUseCase
from app.core.schemas.produto_schema import ProdutoCreate, ProdutoResponse
from app.infra.memory.sebo_repository_memory import SeboRepositoryMemory
from app.core.schemas.sebo_schema import SeboCreate, SeboResponse

router_sebo = APIRouter(prefix="/sebos", tags=["Sebos"])

repo_memory = SeboRepositoryMemory()

def get_repo():
    return repo_memory

@router_sebo.post("/", response_model=SeboResponse, summary="Cadastrar um novo sebo", status_code=201)
def cadastrar(sebo: SeboCreate, repo: SeboRepositoryMemory = Depends(get_repo)):
    """
    Cria um novo sebo (livraria de usados) dentro da plataforma Sebo Online.
    - **nome**: nome do sebo
    - **descricao**: breve descrição do sebo
    - **dono_id**: identificador do usuário dono do sebo
    """
    try:

        use_case = CadastrarSeboUseCase(repo)
        novo_sebo = use_case.execute(sebo)
        return novo_sebo
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router_sebo.post("/{sebo_id}/produtos", response_model=ProdutoResponse, summary="Cadastrar um novo produto", status_code=200)
def adicionar_produto(sebo_id: int, produto: ProdutoCreate, repo: SeboRepositoryMemory = Depends(get_repo)):
    try:
        use_case = AdicionarProdutoSeboUseCase(repo)
        produto_criado = use_case.execute(sebo_id, produto.model_dump())
        return produto_criado
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))



@router_sebo.get("/", response_model=list[SeboResponse], summary="Listar sebos cadastrados", status_code=200)
def listar(repo: SeboRepositoryMemory = Depends(get_repo)):
    """
    Retorna todos os sebos cadastrados na plataforma Sebo Online.
    """

    use_case = ListarSeboUseCase(repo)
    sebos = use_case.execute()
    return sebos
