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


def test_adicionar_produto_ao_sebo():
    # Primeiro, cria o sebo
    response_sebo = client.post("/sebos/", json={
        "nome": "Sebo Teste",
        "descricao": "Sebo para testes",
        "dono_id": 1
    })
    sebo_id = response_sebo.json()["id"]

    # Agora adiciona o produto
    response_produto = client.post(f"/sebos/{sebo_id}/produtos", json={
        "nome": "Livro de Teste",
        "descricao": "Um livro para teste",
        "preco": 25.0
    })

    assert response_produto.status_code == 200
    data = response_produto.json()
    assert data["nome"] == "Livro de Teste"
    assert data["descricao"] == "Um livro para teste"
    assert data["preco"] == 25.0

def test_adicionar_produto_sebo_inexistente():
    response = client.post("/sebos/999/produtos", json={
        "nome": "Produto X",
        "descricao": "Produto em sebo inexistente",
        "preco": 10.0
    })
    assert response.status_code == 404