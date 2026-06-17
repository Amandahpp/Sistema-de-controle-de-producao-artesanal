# 🧶 Sistema de Controle de Produção Artesanal de Crochê

Sistema desenvolvido utilizando Programação Orientada a Objetos para auxiliar artesãos no gerenciamento da produção de peças em crochê, controle de materiais, estoque e pedidos de clientes.

---

## 📋 Funcionalidades

* 👤 Cadastro de clientes
* 🛍️ Registro de pedidos
* 🧶 Cadastro de produtos artesanais
* 📦 Controle de materiais
* 📊 Controle de estoque
* 📝 Registro de receitas de fabricação
* 🏭 Controle de produção
* 💰 Cálculo de custos de fabricação
* ⚠️ Verificação de disponibilidade de materiais para produção

---

## 🏗️ Tecnologias Utilizadas

* Python
* Programação Orientada a Objetos (POO)
* UML

---

## 📊 Diagrama UML

<img width="1280" height="1061" alt="UML Projeto TOO" src="https://github.com/user-attachments/assets/1e0da809-387a-4bb8-91fa-b2e15754321b" />


---

## 🧩 Estrutura do Sistema

### Cliente

Responsável pelo cadastro dos clientes e realização de pedidos.

### Pedido

Armazena informações dos pedidos realizados pelos clientes.

### ItemPedido

Representa cada produto presente em um pedido.

### Produto

Representa uma peça artesanal produzida em crochê.

### Material

Representa os insumos utilizados na produção.

### Estoque

Responsável pelo controle das quantidades disponíveis dos materiais, entradas, saídas e verificação de disponibilidade para produção.

### ReceitaCroche

Define quais materiais e quantidades são necessários para fabricar um produto.

### Producao

Controla o processo de fabricação das peças.

---

## 🔗 Relacionamentos

```text
Cliente
   │
   └── Pedido
           │
           └── ItemPedido
                     │
                     └── Produto
                              │
                              ├── ReceitaCroche
                              │         │
                              │         └── Material
                              │                  │
                              │                  └── Estoque
                              │
                              └── Producao
```

---

## 🧠 Conceitos de POO Aplicados

### Encapsulamento

Proteção dos atributos através de métodos apropriados para manipulação dos dados.

### Abstração

Representação das entidades do mundo real por meio de classes e objetos.

### Herança

Possibilidade de expansão futura do sistema.

```text
Pessoa
 ├── Cliente
 └── Funcionario
```

### Polimorfismo

Permite diferentes implementações para regras específicas de cálculo de custos, preços e produção.

---

## 🎨 Padrões de Projeto

### Factory Method

Centraliza a criação dos objetos do sistema, facilitando manutenção e expansão.

### Strategy

Permite utilizar diferentes estratégias para cálculo de custos de produção e formação de preços.

---

## 📦 Controle de Estoque

A classe **Estoque** foi adicionada para separar a responsabilidade de gerenciamento das quantidades disponíveis dos materiais.

### Principais responsabilidades

* Registrar entradas de materiais;
* Registrar saídas de materiais;
* Consultar quantidade disponível;
* Verificar estoque mínimo;
* Validar disponibilidade antes do início da produção.

### Benefícios

* Maior organização do sistema;
* Melhor aderência ao princípio da Responsabilidade Única (SRP);
* Facilidade para futuras expansões, como relatórios e histórico de movimentações;
* Estrutura semelhante à utilizada em sistemas reais de gestão.

---

## 🚀 Como Executar

### Clonar o Repositório

```bash
git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
```

### Acessar a Pasta do Projeto

```bash
cd projeto-croche
```

### Executar o Sistema

```bash
python main.py
```

---

## 🧪 Testes

```bash
python testes.py
```

---

## 📚 Aprendizados

Durante o desenvolvimento deste projeto foram aplicados conceitos fundamentais de:

* Programação Orientada a Objetos;
* Modelagem UML;
* Relacionamentos entre classes;
* Controle de estoque;
* Gestão de produção;
* Organização de sistemas para pequenos negócios;
* Separação de responsabilidades entre entidades do domínio.

---

## 👩‍💻 Autora

Amanda Andreis Hoppe

Projeto desenvolvido para fins acadêmicos na disciplina de Programação Orientada a Objetos.

---

## 🤖 Uso de Inteligência Artificial

Ferramentas de Inteligência Artificial como ChatGPT e Gemini foram utilizadas como apoio para:

* Revisão da modelagem UML;
* Organização da documentação;
* Explicação de conceitos de POO;
* Sugestões de melhorias no projeto.

Todas as decisões finais de modelagem e implementação foram analisadas e validadas pela autora.

