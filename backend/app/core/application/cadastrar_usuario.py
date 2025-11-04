# app/core/application/cadastrar_usuario.py

from app.core.domain.usuario import Usuario
from app.core.ports.i_usuario_repository import IUsuarioRepository
from app.core.schemas.usuario_schema import UsuarioCreate, UsuarioResponse


class CadastrarUsuarioUseCase:
    """
    Caso de uso: Cadastrar Usuário
    """

    def __init__(self, repo: IUsuarioRepository):
        self.repo = repo

    def execute(self, data: UsuarioCreate) -> UsuarioResponse:
        # --- Validações ---
        if not data.nome.strip():
            raise ValueError("O nome do usuário não pode estar vazio.")
        if not data.email.strip():
            raise ValueError("O email não pode estar vazio.")
        if not data.senha.strip():
            raise ValueError("A senha não pode estar vazia.")

        # --- Verifica duplicidade por e-mail ---
        usuarios_existentes = self.repo.listar()
        if any(u.email.lower() == data.email.lower() for u in usuarios_existentes):
            raise ValueError("Já existe um usuário cadastrado com este email.")

        # --- Cria e salva ---
        usuario = Usuario(id=0, nome=data.nome, email=data.email, senha=data.senha)
        salvo = self.repo.salvar(usuario)

        return UsuarioResponse(
            id=salvo.id,
            nome=salvo.nome,
            email=salvo.email,
        )
