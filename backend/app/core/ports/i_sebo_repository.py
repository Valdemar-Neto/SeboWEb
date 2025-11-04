from abc import ABC, abstractmethod
from typing import List
from app.core.domain.sebo import SEBO

class ISeboRepository(ABC):
    @abstractmethod
    def salvar(self, sebo: SEBO) -> SEBO:
        pass

    @abstractmethod
    def listar(self) -> SEBO:
        pass