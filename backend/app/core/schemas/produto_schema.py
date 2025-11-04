from pydantic import BaseModel, Field
from pydantic import ConfigDict


class ProdutoBase(BaseModel):
    """Campos base compartilhados entre os schemas de Produto."""
    nome: str = Field(
        ..., min_length=2,
        json_schema_extra={"example": "Harry Potter e o Prisioneiro de Azkaban"}
    )
    preco: float = Field(
        ..., gt=0,
        json_schema_extra={"example": 99.99}
    )
    descricao: str = Field(
        "", 
        json_schema_extra={"example": "Livro usado, capa dura"}
    )


class ProdutoCreate(ProdutoBase):
    """Schema para criação de um produto (entrada do usuário)."""
    # Não é necessário repetir os campos, pois herda de ProdutoBase
    ...


class ProdutoResponse(ProdutoBase):
    """Schema de resposta para exibição de um produto."""
    id: int = Field(
        ..., 
        json_schema_extra={"example": 1}
    )

    model_config = ConfigDict(from_attributes=True)
