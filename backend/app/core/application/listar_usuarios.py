from app.core.ports.i_usuario_repository import IUsuarioRepository
from app.core.domain.usuario import Usuario
from typing import List

class ListarUsuarioUseCase:
    def __init__(self, repo = IUsuarioRepository):
        self.repo = repo
    def execute(self) -> List[Usuario]:
        return self.repo.listar()