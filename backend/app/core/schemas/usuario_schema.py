from pydantic import BaseModel, EmailStr, Field
from pydantic import ConfigDict

class UsuarioBase(BaseModel):
    nome: str = Field(..., min_length=3, json_schema_extra=" João Silva")
    email: EmailStr = Field(..., json_schema_extra="joaosilva@example.com")
    senha: str = Field(..., min_length=4, json_schema_extra="1234")

class UsuarioCreate(BaseModel):
    nome: str = Field(..., min_length=3, json_schema_extra=" João Silva")
    email: EmailStr = Field(..., json_schema_extra="joaosilva@example.com")
    senha: str = Field(..., min_length=4, json_schema_extra="1234")

class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)