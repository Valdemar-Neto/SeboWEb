from app.core.ports.i_sebo_repository import ISeboRepository
from app.core.domain.sebo import SEBO
from typing import List

class SeboRepositoryMemory(ISeboRepository):
    def __init__(self):
        self._db = []
        self._id_counter = 1

    def salvar(self, sebo: SEBO) -> SEBO:
        sebo.id = self._id_counter
        self._id_counter += 1
        self._db.append(sebo)
        return sebo
    
    def listar(self) -> List[SEBO]:
        return self._db