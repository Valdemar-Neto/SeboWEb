from fastapi import APIRouter, Depends, HTTPException
from app.core.application.cadastrar_usuario import CadastrarUsuarioUseCase
from app.core.application.listar_usuarios import ListarUsuarioUseCase
from app.infra.memory.usuario_repository_memory import UsuarioRepositoryMemory
from app.core.schemas.usuario_schema import UsuarioCreate, UsuarioResponse

router_usuario = APIRouter(prefix="/usuarios", tags=["Usuários"])

repo_usuario = UsuarioRepositoryMemory()

def get_repo():
    return repo_usuario

@router_usuario.post("/", response_model=UsuarioResponse, summary="Cadastrar novo usuário", status_code=201)
def cadastrar(usuario: UsuarioCreate, repo: UsuarioRepositoryMemory = Depends(get_repo)):
    """
    Cadastra um novo usuário no sistema do Sebo Online.
    - **nome**: nome completo do usuário
    - **email**: endereço de e-mail válido
    - **senha**: senha de acesso (armazenar de forma segura no futuro)
    """
    try:

        use_case = CadastrarUsuarioUseCase(repo)
        novo_usuario = use_case.execute(usuario)
        return novo_usuario
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router_usuario.get("/", response_model=list[UsuarioResponse], summary="Listar todos os usuários cadastrados", status_code=200)
def listar(repo: UsuarioRepositoryMemory = Depends(get_repo)):
    """
    Retorna uma lista com todos os usuários cadastrados no sistema.
    """

    use_case = ListarUsuarioUseCase(repo)
    usuarios = use_case.execute()
    return usuarios
