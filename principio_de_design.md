# 🧠 Relatório — Princípios de Projeto Aplicados ao Sebo Digital

## 🧩 Princípios de Projeto Utilizados

### 1. 🧱 Responsabilidade Única (SRP — *Single Responsibility Principle*)
> Cada classe ou módulo deve ter apenas uma razão para mudar.

**Aplicação no projeto:**
- A classe `Sebo` lida apenas com dados e regras de negócio do sebo.  
- O `PedidoService` trata exclusivamente da lógica de pedidos.  
- O `CadastroService` é responsável apenas por autenticação e registro.  

📈 **Benefício:** facilita manutenção, reuso e testes unitários.

---

### 2. 🔄 Aberto/Fechado (OCP — *Open/Closed Principle*)
> Classes devem estar abertas para extensão, mas fechadas para modificação.

**Aplicação no projeto:**
- O módulo de pagamento (`PagamentoService`) pode ser estendido com novos métodos (Pix, Cartão, PayPal) sem alterar o código existente.  
- Isso é possível porque os serviços dependem de **interfaces**, e não de implementações concretas.  

📈 **Benefício:** facilita a evolução e manutenção do sistema.

---

### 3. 🔁 Substituição de Liskov (LSP — *Liskov Substitution Principle*)
> Classes derivadas devem poder substituir suas classes base sem afetar o comportamento esperado.

**Aplicação no projeto:**
- Interfaces como `IRepositorioProduto` e `IRepositorioCliente` permitem múltiplas implementações (PostgreSQL, MongoDB, mocks para testes).  
- O domínio não precisa ser alterado ao trocar a tecnologia de persistência.

📈 **Benefício:** garante flexibilidade e intercambialidade segura.

---

### 4. 🧩 Segregação de Interfaces (ISP — *Interface Segregation Principle*)
> Nenhuma classe deve ser forçada a depender de métodos que não usa.

**Aplicação no projeto:**
- Repositórios separados (`IRepositorioSebo`, `IRepositorioProduto`, `IRepositorioPedido`).  
- Cada interface tem um escopo bem definido.  
- Os serviços injetam apenas as interfaces relevantes.

📈 **Benefício:** reduz dependências desnecessárias e melhora a coesão.

---

### 5. ⚙️ Prefira Interfaces a Classes Concretas
> Sempre dependa de abstrações, não de implementações.

**Aplicação no projeto:**
- Os serviços usam interfaces para comunicação com a camada de infraestrutura.  
- No backend Python, dependências são injetadas via containers (ex: FastAPI + Dependency Injection).  
- No frontend TypeScript, interfaces definem contratos de dados (`IProduto`, `ISebo`, `ICliente`).

📈 **Benefício:** melhora testabilidade e flexibilidade do sistema.

---

### 6. 🔄 Inversão de Dependência (DIP — *Dependency Inversion Principle*)
> Módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de abstrações.

**Aplicação no projeto:**
- O `PedidoService` (módulo de alto nível) não depende diretamente de `RepositorioPedidoSQL` (baixo nível), mas sim da interface `IRepositorioPedido`.  
- O mesmo vale para `PagamentoService`, que depende da abstração `IGatewayPagamento`.  
- A inversão é implementada via **injeção de dependência**: os adaptadores (infraestrutura) são plugados em tempo de execução.

📈 **Benefício:** reduz acoplamento entre camadas, facilita testes e substituição de tecnologias (ex: mudar o banco de dados ou o gateway de pagamento sem alterar a lógica de negócio).

---

### 7. 📡 Lei de Demeter (*Law of Demeter — LoD*)
> Um objeto deve falar apenas com seus vizinhos imediatos (“fale apenas com seus amigos diretos”).

**Aplicação no projeto:**
- O `PedidoService` se comunica apenas com `RepositorioPedido` e `ServicoPagamento`, sem navegar por estruturas internas (ex: `pedido.cliente.endereco.rua`).  
- A comunicação entre camadas é feita por **facades** e **DTOs**, evitando acoplamento profundo.

📈 **Benefício:** melhora a modularidade e evita dependências desnecessárias em cadeia.

---

## ⚙️ Outros Padrões e Conceitos de Apoio

### 🧱 Arquitetura Hexagonal (Ports & Adapters)
- O domínio é isolado da infraestrutura (banco, APIs, UI).  
- Interfaces (ports) definem contratos; adaptadores implementam as tecnologias.  
- Exemplo: `ProdutoService` (núcleo) depende de `IRepositorioProduto`, enquanto `RepositorioProdutoSQL` é um adaptador externo.

---

### 🌍 Domain-Driven Design (DDD)
- **Entidades:** `Cliente`, `Empresario`, `Sebo`, `Produto`, `Pedido`.  
- **Agregados:** `Sebo` agrupa `Produto`.  
- **Value Objects:** `Endereco`, `Pagamento`, `StatusPedido`.  
- **Serviços de Domínio:** encapsulam lógica de negócios independente da interface.  
- **Repositórios:** abstraem a persistência de dados.


### 🧪Test-Driven Development (TDD)
- Cada **User Story** gera testes unitários e de integração.  
- Exemplo:
  - “Como cliente, quero comprar um produto” → teste do fluxo de compra e pagamento.  
  - “Como empresário, quero cadastrar produtos” → teste de validação e persistência.

---

## 📘 Conclusão
A aplicação combinada dos princípios **SOLID**, **Lei de Demeter**, **Inversão de Dependência**, **DDD**, **TDD** e **Arquitetura Hexagonal** assegura que o **Sebo Digital** seja um sistema **escalável, flexível e sustentável**.  
