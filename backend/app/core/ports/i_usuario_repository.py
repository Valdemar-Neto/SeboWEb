from abc import ABC, abstractmethod
from typing import List
from app.core.domain.usuario import Usuario

class IUsuarioRepository(ABC):
    @abstractmethod
    def salvar(self, usuario: Usuario) -> Usuario:
        pass

    @abstractmethod
    def listar(self) -> List[Usuario]:
        pass