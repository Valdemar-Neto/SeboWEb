# Padrões de Projeto do MVP

## Padrões de Projeto Utilizados

O MVP do sistema de Sebos Online utiliza alguns padrões de projeto para organizar o código e manter a manutenção e expansão mais fáceis:

1. **Repository Pattern (Padrão Repositório)**

   * Cada entidade principal (Sebo, Produto) possui um repositório responsável pelo acesso ao banco de dados (`SeboRepositorySQL`, `ProdutoRepositorySQL`).
   * Justificativa: O padrão Repository desacopla a lógica de persistência da lógica de negócio, permitindo que os use cases trabalhem com objetos de domínio sem se preocupar com a implementação do banco de dados.

2. **Use Case / Application Service (Padrão de Caso de Uso)**

   * A lógica de negócio é encapsulada em classes de use case, como `AdicionarProduto`, que coordenam as operações entre entidades e repositórios.
   * Justificativa: Mantém a separação entre regras de negócio e a camada de API (FastAPI), seguindo o princípio de Single Responsibility, e facilita testes unitários da lógica.
3. **Singleton**
    * Pode ser aplicado se o banco de dados ou o Session do SQLAlchemy for instanciado apenas uma vez e compartilhado em toda a aplicação..
    * Garante que exista uma única instância do acesso ao banco, evitando conflitos de sessão ou múltiplas conexões desnecessárias.

## Padrões Não Utilizados

* **Factory, Observer, Strategy, etc.**

  * Esses padrões não foram utilizados neste MVP porque a aplicação é relativamente simples e o foco principal era estruturar corretamente os casos de uso e acesso a dados.
  * Justificativa: Implementar esses padrões sem necessidade poderia adicionar complexidade desnecessária sem benefícios claros para este estágio do MVP.

## Conclusão
Padrões adicionais podem ser adicionados conforme a aplicação cresce e novas funcionalidades são implementadas.
