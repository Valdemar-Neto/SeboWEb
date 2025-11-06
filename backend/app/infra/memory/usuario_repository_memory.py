from app.core.ports.i_usuario_repository import IUsuarioRepository
from app.core.domain.usuario import Usuario
from typing import List

class UsuarioRepositoryMemory(IUsuarioRepository):
    def __init__(self):
        self._db = []
        self._id_counter = 1

    def salvar(self, usuario: Usuario) -> Usuario:
        usuario.id = self._id_counter
        self._id_counter += 1
        self._db.append(usuario)
        return usuario
    
    def listar(self) -> List[Usuario]:
        return self._db