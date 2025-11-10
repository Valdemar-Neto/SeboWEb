# Eng-de-Software-UFRN

Repositório de exemplo para as atividades da disciplina de Engenharia de Software da UFRN.

## Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Como clonar ou baixar](#como-clonar-ou-baixar)  
- [Estrutura do Projeto](#estrutura-do-projeto)  
- [Licença](#licença)
- [Principio de Projetos](https://github.com/Valdemar-Neto/SeboWEb/blob/main/principio_de_design.md)
- [Padrões de Projetos]()

## Sobre o Projeto

### Título
📚 Sebo Online – Marketplace de Sebos

### Descrição
O Sebo Online é uma plataforma desenvolvida para conectar leitores e sebos (livrarias de usados) em um único ambiente digital. A aplicação permite que empresários de sebos cadastrem seus estabelecimentos e publiquem seus produtos (livros, revistas, HQs, etc.), enquanto clientes podem navegar, consultar e adquirir itens de diferentes sebos de forma prática e intuitiva.

### Componentes
- HERTZ DE SOUZA DANTAS
- NICOLAS DANIEL DA ROCHA SILVA
- VALDEMAR GONCALVES PEREIRA NETO

### User Stories
📚 User Stories – Sebo Online
🔹 Usuário Cliente

Cadastro/Login  
1.   Como cliente, quero me cadastrar no Sebo Online para ter acesso à compra de livros e acompanhar meus pedidos.
2.   Como cliente, quero fazer login para usar minhas credenciais em diferentes dispositivos.
   
Navegação e Busca
1.   Como cliente, quero navegar pelos sebos cadastrados para descobrir novos vendedores de livros usados.
2.   Como cliente, quero buscar livros pelo título, autor ou categoria para encontrar rapidamente o que desejo.
   
Produtos
1.   Como cliente, quero visualizar os detalhes de um livro (título, autor, preço, estado de conservação) para decidir se compro ou não.
2.   Como cliente, quero adicionar livros a uma lista de favoritos para consultar mais tarde.

Compra
1.   Como cliente, quero adicionar livros ao carrinho para comprar vários produtos de uma vez.
2.   Como cliente, quero finalizar a compra e efetuar o pagamento para receber os livros em minha casa.
3.   Como cliente, quero acompanhar o status do pedido para saber quando o livro será entregue.

🔹 Dono do Sebo (Empresário)

Cadastro/Login

1.   Como dono de sebo, quero me cadastrar e criar meu perfil de sebo para oferecer meus livros na plataforma.
2.   Como dono de sebo, quero fazer login para gerenciar meus produtos.

Gestão do Sebo

1.   Como dono de sebo, quero editar as informações do meu sebo (nome, descrição, endereço) para apresentar bem minha loja.
2.   Como dono de sebo, quero visualizar relatórios de vendas para entender meu desempenho.

Gestão de Produtos

1.   Como dono de sebo, quero cadastrar livros com título, descrição, preço e estado de conservação para torná-los disponíveis para venda.
2.   Como dono de sebo, quero editar informações de um livro para corrigir dados ou atualizar o preço.
3.   Como dono de sebo, quero remover livros que já foram vendidos ou não estão mais disponíveis para manter meu catálogo atualizado.

Pedidos

1.   Como dono de sebo, quero visualizar os pedidos recebidos para separar os livros e enviar ao cliente.
2.   Como dono de sebo, quero atualizar o status do pedido (em preparo, enviado, entregue) para informar o cliente sobre o andamento da compra
   


## Você pode obter este repositório de três formas:

### Clonar via HTTPS

```bash
git clone https://github.com/Valdemar-Neto/SeboWEb.git
```

Isso criará uma cópia local do repositório em sua máquina.

### Clonar via SSH

Se você já configurou sua chave SSH no GitHub, pode clonar usando:

```bash
git clone git@github.com:Valdemar-Neto/SeboWEb.git
```

Isso criará uma cópia local do repositório em sua máquina.

### Baixar como ZIP

1. Acesse a página do repositório no GitHub:
   [https://github.com/Valdemar-Neto/SeboWEb](https://github.com/Valdemar-Neto/SeboWEb)
2. Clique no botão **Code** (verde).
3. Selecione **Download ZIP**.
4. Extraia o arquivo ZIP para o local desejado em seu computador.


## Estrutura do Projeto

> *Esta seção pode variar conforme a organização do repositório de cada grupo.*

```
sebo-online/
├── backend/
│   ├── app/
│   │   ├── main.py                 # Entry point da API
│   │   ├── routes.py               # Rotas REST
│   │   ├── core/                   # Camada de domínio e aplicação
│   │   │   ├── domain/             # Entidades de negócio
│   │   │   │   ├── sebo.py
│   │   │   │   ├── produto.py
│   │   │   │   └── usuario.py
│   │   │   ├── application/        # Casos de uso (regras de aplicação)
│   │   │   │   ├── cadastrar_produto.py
│   │   │   │   └── listar_produtos.py
│   │   │   └── ports/              # Interfaces (contratos) -> Hexagonal
│   │   │       ├── i_produto_repository.py
│   │   │       └── i_sebo_repository.py
│   │   └── infra/                  # Implementações técnicas (DB, memória, etc.)
│   │       └── memory/
│   │           ├── produto_repository_memory.py
│   │           └── sebo_repository_memory.py
│   ├── tests/                      # Testes TDD
│   │   ├── test_cadastrar_produto.py
│   │   └── test_listar_produtos.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── src/
│   │   ├── services/               # Comunicação com API
│   │   │   └── produtoService.ts
│   │   ├── ui/                     # Interface do usuário
│   │   │   ├── components/
│   │   │   │   └── ProdutoCard.tsx
│   │   │   └── pages/
│   │   │       └── SeboPage.tsx
│   │   └── main.tsx                # Entry do React
│   ├── package.json
│   ├── tsconfig.json
│   └── Dockerfile
│
├── docker-compose.yml
└── README.md


```

- LICENSE: termos da licença do projeto (MIT).
- README.md: este arquivo de apresentação.

## Licença

Este projeto está licenciado sob a **Licença MIT**. Veja o arquivo `LICENSE` para mais detalhes.
