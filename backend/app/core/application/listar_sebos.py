from app.core.ports.i_sebo_repository import ISeboRepository
from app.core.domain.sebo import Sebo
from typing import List


class ListarSeboUseCase:
    def init(self, repo: ISeboRepository):
        self.repo = repo
    def execute(self) -> List[Sebo]:
        return self.repo.listar()