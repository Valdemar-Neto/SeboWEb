from pydantic import BaseModel, Field
from typing import List
from app.core.schemas.produto_schema import ProdutoResponse
from pydantic import ConfigDict

class SeboBase(BaseModel):
    """Campos base do sebo."""
    nome: str = Field(..., min_length=3, json_schema_extra="Sebo Central")
    descricao: str = Field("", json_schema_extra="Sebo especializado em livros raros e usados.")
    dono_id: int = Field(..., ge=1, json_schema_extra=1)

class SeboCreate(SeboBase):
    """Campos base do sebo."""
    nome: str = Field(..., min_length=3, json_schema_extra="Sebo Central")
    descricao: str = Field("", json_schema_extra="Sebo especializado em livros raros e usados.")
    dono_id: int = Field(..., ge=1, json_schema_extra=1)

class SeboResponse(SeboBase):
    """Schema de resposta ao listar ou detalhar um sebo."""
    id: int = Field(..., json_schema_extra=10)
    produtos: List[ProdutoResponse] = Field(default_factory=list)

    model_config = ConfigDict(from_attributes=True)
