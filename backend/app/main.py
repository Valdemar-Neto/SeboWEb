from fastapi import FastAPI
from .routes.produto_routes import router_produto
from .routes.sebo_routes import router_sebo
from .routes.usuario_routes import router_usuario

app = FastAPI(
    title="Sebo Online API",
    description=(
        "API para gerenciamento de sebos e produtos.\n\n"
        "Permite que sebos cadastrem livros, listem produtos e clientes realizem compras."
    ),
    version="1.0.0",
    contact={
        "name": "Equipe Sebo Online",
        "email": "contato@seboonline.com",
    },
    license_info={
        "name": "MIT License",
    },  
)

app.include_router(router_produto)
app.include_router(router_usuario)
app.include_router(router_sebo)

@app.get("/", tags=["ROOTS"])
def root():
    return {"message": "Testando API do SEBO ONLINE"}
