from app.core.domain.usuario import Usuario
from app.core.ports.i_usuario_repository import IUsuarioRepository

def cadastrar_usuario(repo: IUsuarioRepository, nome: str, email: str, senha: str):
    usuario = Usuario(id=0, nome=nome, email=email, senha=senha)
    return repo.salvar(usuario)