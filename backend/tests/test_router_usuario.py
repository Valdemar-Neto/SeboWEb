from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_criar_sebo_sucesso():
    response = client.post("/usuarios/", json={
        "nome": "Alves Gomes",
        "email": "vitorjojo@example.com",
        "senha": "batatinhafrita123"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["nome"] == "Alves Gomes"
    assert data["email"] == "vitorjojo@example.com"


def test_criar_produto_nome_vazio():
    response = client.post("/usuarios/", json={
        "nome": "",
        "email": "",
        "senha": "sdffd332"
    })

    assert response.status_code == 422
    errors = response.json()["detail"]
    assert any(error["loc"][-1] == "nome" for error in errors)


def test_listar_produtos():
    # Criando um produto para garantir que a lista não esteja vazia
    client.post("/usuarios/", json={
        "nome": "Joao Vitor",
        "email": "jvbelezinha@example.com",
        "senha": "testelbambulab"
    })
    response = client.get("/produtos/")
    assert response.status_code == 200
    produtos = response.json()
    assert isinstance(produtos, list)
    assert len(produtos) > 0
