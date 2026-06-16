# 🧶 Sistema de Controle de Produção Artesanal de Crochê

Sistema desenvolvido utilizando Programação Orientada a Objetos para auxiliar artesãos no gerenciamento da produção de peças em crochê, controle de materiais, estoque e pedidos de clientes.

---

## 📋 Funcionalidades

* 👤 Cadastro de clientes
* 🛍️ Registro de pedidos
* 🧶 Cadastro de produtos artesanais
* 📦 Controle de materiais e estoque
* 📝 Registro de receitas de fabricação
* 🏭 Controle de produção
* 💰 Cálculo de custos de fabricação

---

## 🏗️ Tecnologias Utilizadas

* Python
* Programação Orientada a Objetos (POO)
* UML

---

## 📊 Diagrama UML

Adicione aqui a imagem do seu diagrama UML.

```markdown
 <img width="1280" height="1061" alt="UML Projeto TOO" src="https://github.com/user-attachments/assets/9bc3ea39-e3aa-403a-aacc-f17415acb5e6" />


```
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
                              │
                              └── Producao
```

---

## 🧠 Conceitos de POO Aplicados

### Encapsulamento

Proteção dos atributos através de métodos apropriados.

### Abstração

Representação de entidades reais por meio de classes.

### Herança

Possibilidade de expansão futura do sistema.

```text
Pessoa
 ├── Cliente
 └── Funcionario
```

### Polimorfismo

Permite diferentes implementações para regras de negócio específicas.

---

## 🎨 Padrões de Projeto

### Factory Method

Centraliza a criação dos objetos do sistema.

### Strategy

Permite diferentes estratégias para cálculo de preços e custos.

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

* Programação Orientada a Objetos
* Modelagem UML
* Relacionamentos entre classes
* Controle de estoque
* Gestão de produção
* Organização de sistemas para pequenos negócios

---

## 👩‍💻 Autora

Amanda Hopp

Projeto desenvolvido para fins acadêmicos na disciplina de Programação Orientada a Objetos.

---

## 🤖 Uso de Inteligência Artificial

Ferramentas de Inteligência Artificial foram utilizadas como apoio para:

* Revisão da modelagem UML;
* Organização da documentação;
* Explicação de conceitos de POO;
* Sugestões de melhorias no projeto.

Todas as decisões finais de modelagem e implementação foram analisadas e validadas pela autora.
