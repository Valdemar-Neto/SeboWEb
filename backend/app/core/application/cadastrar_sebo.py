# app/core/application/cadastrar_sebo.py

from app.core.domain.sebo import Sebo
from app.core.ports.i_sebo_repository import ISeboRepository
from app.core.schemas.sebo_schema import SeboCreate, SeboResponse


class CadastrarSeboUseCase:
    """
    Caso de uso: Cadastrar Sebo
    """

    def __init__(self, repo: ISeboRepository):
        self.repo = repo

    def execute(self, data: SeboCreate) -> SeboResponse:
        
        if not data.nome.strip():
            raise ValueError("O nome do sebo não pode estar vazio.")
        if not data.descricao.strip():
            raise ValueError("A descrição não pode estar vazia.")

        
        sebos_existentes = self.repo.listar()
        if any(s.nome.lower() == data.nome.lower() for s in sebos_existentes):
            raise ValueError("Já existe um sebo com este nome.")

        
        sebo = Sebo(id=0, nome=data.nome, descricao=data.descricao, dono_id=data.dono_id)
        salvo = self.repo.salvar(sebo)

        return SeboResponse(
            id=salvo.id,
            nome=salvo.nome,
            descricao=salvo.descricao,
            dono_id=salvo.dono_id
        )
