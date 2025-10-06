# Documentação dos Diagramas UML do Projeto SeboWEb

Este documento descreve os diagramas UML criados para o projeto SeboWEb e justifica a escolha de cada um deles. Os diagramas são gerados diretamente no GitHub usando a sintaxe Mermaid para garantir sua visualização permanente.

---

1. Diagrama de Casos de Uso (Comportamental)

Este diagrama oferece uma visão de alto nível das funcionalidades do sistema pela perspectiva do usuário.

**Justificativa:**
- **Visão Geral:** Resume as principais interações do `Usuário` com o sistema.
- **Comunicação:** Facilita o entendimento do escopo do projeto.
- **Requisitos:** Ajuda a visualizar os requisitos funcionais de forma clara.

```mermaid
graph TD
    subgraph "Sistema SeboWEb"
        UC1["Gerenciar Cadastro"]
        UC2["Gerenciar Livros"]
        UC3["Realizar Compra"]
        UC4["Gerenciar Endereço"]
    end

    ator((Usuário)) --> UC1
    ator --> UC2
    ator --> UC3
    ator --> UC4

    UC3 -.-> UC1
    UC4 -.-> UC1


2. Diagrama de Classes (Estrutural)
Este diagrama descreve a estrutura estática do sistema, detalhando as classes, seus atributos, métodos e relacionamentos.
Justificativa:
Estrutura do Código: Serve como um "blueprint" para a base do código, modelando as entidades principais.
Relacionamentos: Clarifica as relações de associação, composição e agregação entre as entidades.
Base para o Desenvolvimento: Guia a implementação do banco de dados e das classes de modelo (Models).

```mermaid
classDiagram
    class Usuario {
        +String nome
        +String email
        -String senha
        +login()
        +logout()
        +cadastrar()
    }

    class Endereco {
        +String rua
        +String cidade
        +String cep
        +adicionar()
        +atualizar()
    }

    class Livro {
        +String titulo
        +String autor
        +String isbn
        +String estado
        +float preco
        +cadastrarLivro()
        +buscarLivro()
    }

    class Transacao {
        +Date data
        +String status
        +criarTransacao()
        +confirmarPagamento()
    }

    Usuario "1" *-- "1..*" Endereco : possui
    Usuario "1" o-- "1..*" Livro : vende
    Usuario "1" -- "1" Transacao : compra
    Usuario "1" -- "1" Transacao : vende
    Livro "1" -- "1" Transacao : é vendido em

3. Diagrama de Sequência (Comportamental)
Este diagrama detalha o fluxo de "Realizar Compra", mostrando a ordem cronológica das interações entre os componentes do sistema.
Justificativa:
Detalhamento de Fluxo: Mostra "como" o sistema executa uma ação passo a passo.
Visualização da Interação: Ilustra a comunicação entre as camadas da arquitetura (Frontend, Backend, Banco de Dados).
Cenário Real: Torna a dinâmica do sistema mais concreta e fácil de entender.

```mermaid
sequenceDiagram
    actor Cliente
    participant Sistema (Frontend)
    participant Controlador (Backend)
    participant BancoDeDados

    Cliente->>Sistema (Frontend): 1. Clica em "Comprar"
    Sistema (Frontend)->>Controlador (Backend): 2. POST /api/transacao {livroId}
    Controlador (Backend)->>BancoDeDados: 3. SELECT * FROM Livro WHERE id = livroId
    BancoDeDados-->>Controlador (Backend): 4. Retorna dados do livro (disponível)
    Controlador (Backend)->>BancoDeDados: 5. INSERT INTO Transacao (...)
    Controlador (Backend)->>BancoDeDados: 6. UPDATE Livro SET status = 'Vendido'
    BancoDeDados-->>Controlador (Backend): 7. Confirmação das operações
    Controlador (Backend)-->>Sistema (Frontend): 8. HTTP 201: Compra realizada com sucesso
    Sistema (Frontend)-->>Cliente: 9. Exibe página de confirmação
