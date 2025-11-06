from abc import ABC, abstractmethod
from typing import List
from app.core.domain.sebo import Sebo

class ISeboRepository(ABC):
    @abstractmethod
    def salvar(self, sebo: Sebo) -> Sebo:
        pass

    @abstractmethod
    def listar(self) -> Sebo:
        pass

    @abstractmethod
    def get_by_id(self) ->Sebo:
        pass