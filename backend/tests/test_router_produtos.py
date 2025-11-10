from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_criar_produto_sucesso():
    response = client.post("/produtos/", json={
        "nome": "O Senhor dos Anéis",
        "preco": 150,
        "descricao": "Edição de colecionador, capa dura"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["nome"] == "O Senhor dos Anéis"
    assert data["preco"] == 150.00
    assert "id" in data


def test_criar_produto_nome_vazio():
    response = client.post("/produtos/", json={
        "nome": "",
        "preco": 120.00,
        "descricao": "Livro novo"
    })
    # Agora esperamos 422, pois o Pydantic valida min_length
    assert response.status_code == 422
    # Podemos validar se o campo 'nome' está presente na mensagem de erro
    errors = response.json()["detail"]
    assert any(error["loc"][-1] == "nome" for error in errors)


def test_listar_produtos():
    # Criando um produto para garantir que a lista não esteja vazia
    client.post("/produtos/", json={
        "nome": "Harry Potter",
        "preco": 99.90,
        "descricao": "Livro usado"
    })
    response = client.get("/produtos/")
    assert response.status_code == 200
    produtos = response.json()
    assert isinstance(produtos, list)
    assert len(produtos) > 0
