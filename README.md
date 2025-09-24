# Eng-de-Software-UFRN

Repositório de exemplo para as atividades da disciplina de Engenharia de Software da UFRN.

## Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Como clonar ou baixar](#como-clonar-ou-baixar)  
- [Estrutura do Projeto](#estrutura-do-projeto)  
- [Licença](#licença)  

## Sobre o Projeto

### Título
📚 Sebo Online – Marketplace de Sebos

### Descrição
O Sebo Online é uma plataforma desenvolvida para conectar leitores e sebos (livrarias de usados) em um único ambiente digital. A aplicação permite que empresários de sebos cadastrem seus estabelecimentos e publiquem seus produtos (livros, revistas, HQs, etc.), enquanto clientes podem navegar, consultar e adquirir itens de diferentes sebos de forma prática e intuitiva.

### Componentes
- HERTZ DE SOUZA DANTAS
- NICOLAS DANIEL DA ROCHA SILVA
- VALDEMAR GONCALVES PEREIRA NETO

## Como clonar ou baixar

Você pode obter este repositório de três formas:

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
