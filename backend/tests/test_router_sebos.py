from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_criar_sebo_sucesso():
    response = client.post("/sebos/", json={
        "nome": "Sebo do Luis",
        "descricao": "O melhor sebo da cidade de Natal",
        "dono_id":1
    })
    assert response.status_code == 201
    data = response.json()
    assert data["nome"] == "Sebo do Luis"
    assert data["descricao"] == "O melhor sebo da cidade de Natal"
    assert data["dono_id"] == 1


def test_criar_produto_nome_vazio():
    response = client.post("/sebos/", json={
        "nome": "",
        "descricao": "O melhor sebo da cidade de Natal",
        "dono_id": 1
    })
    # Agora esperamos 422, pois o Pydantic valida min_length
    assert response.status_code == 422
    # Podemos validar se o campo 'nome' está presente na mensagem de erro
    errors = response.json()["detail"]
    assert any(error["loc"][-1] == "nome" for error in errors)


def test_listar_produtos():
    # Criando um produto para garantir que a lista não esteja vazia
    client.post("/sebos/", json={
        "nome": "Sebo do Jose",
        "descricao": "O melhor sebo de Natal",
        "dono_id": 1
    })
    response = client.get("/produtos/")
    assert response.status_code == 200
    produtos = response.json()
    assert isinstance(produtos, list)
    assert len(produtos) > 0
