from app.core.ports.i_sebo_repository import ISeboRepository
from app.core.domain.sebo import Sebo
from typing import List

class SeboRepositoryMemory(ISeboRepository):
    def __init__(self):
        self._db = []
        self._id_counter = 1

    def salvar(self, sebo: Sebo) -> Sebo:
        sebo.id = self._id_counter
        self._id_counter += 1
        self._db.append(sebo)
        return sebo
    
    def listar(self) -> List[Sebo]:
        return self._db
    
    def get_by_id(self, sebo_id: int):
        for sebo in self._db:
            if sebo.id == sebo_id:
                return sebo
        return None