#  Sistema de Controle de Produção Artesanal de Crochê

Sistema desenvolvido utilizando Tecnologia de Orientação a Objetos para auxiliar artesãos no gerenciamento da produção de peças em crochê, controle de materiais, estoque e pedidos de clientes, e organização financeira.

---

##  Funcionalidades

*  Cadastro de clientes
*  Registro de pedidos
*  Cadastro de produtos artesanais
*  Controle de materiais
*  Registro de receitas de fabricação
*  Controle de produção
*  Cálculo de custos de fabricação
*  Verificação de disponibilidade de materiais para produção

---

##  Tecnologias Utilizadas

* Python
* Tecnologia de Orientação a Objetos (TOO)
* UML

---

##  Diagrama UML

<img width="1280" height="1061" alt="UML Projeto TOO (1)" src="https://github.com/user-attachments/assets/8769ceff-f3ac-4c29-8b4b-114f9fb1e0fa" />
---

##  Estrutura do Sistema

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
                              │                  
                              │
                              └── Producao
```

---

##  Conceitos de POO Aplicados

### Encapsulamento

O encapsulamento foi utilizado ao concentrar os dados e comportamentos dentro das próprias classes. Por exemplo, a classe Produto controla internamente o cálculo de custos através dos métodos calcular_custo() e _custo_materiais().

### Abstração

Foi utitlizada nos estados da producao, que define os comportamentos obrigatórios para todos os estados da produção sem especificar sua implementação.

### Herança

Foi utitliza na classe producocroche onde ele herda os dados do produto.

### Polimorfismo

Permite diferentes implementações para regras específicas de cálculo de custos, preços e produção, principalemnte na classe produtocroche onde cada subclasse recebe um valor diferente para ser implementado, e utitliza o mesmo metodo valor_hora().

---

##  Padrões de Projeto

### Factory Method

Utitlizei o metodo Factory Method para centralizar a criação dos produtos, um exemplo seria a criação de uma peça de amigurumi, eu chamo a subclasse do tipo amigurumi e ele cria o objeto dentro da subclasse oque permite que ele ja calcule o valor na classe produtocroche com o valor da hora que eu estipulei,sem precisar chamar tudo de novo.

### State

Utitilizei o metodo State para instanciar os estados da producao das minhas peças,elas tem os estados: em_producao, pendente e finalizada. 

---

## Testes

```bash
python main.py
```

---

##  Aprendizados

Durante o desenvolvimento deste projeto foram aplicados conceitos fundamentais de:

* Tecnologia de Orientação a Objetos;
* Modelagem UML;
* Relacionamentos entre classes;
* Controle de estoque/materiais;
* Gestão de produção;
* Organização de sistemas para pequenos negócios;
* Separação de responsabilidades entre entidades do domínio.
* Calculos de valores de peças.
---

##  Autora

Amanda Andreis Hoppe

Projeto desenvolvido para fins acadêmicos na disciplina de Tecnologia de Orientação a Objetos.

---

##  Uso de Inteligência Artificial

Ferramentas de Inteligência Artificial como ChatGPT e Claude foram utilizadas como apoio para:

* Revisão da modelagem UML;
* Organização da documentação;
* Sugestões de melhorias no projeto e no código.

Todas as decisões finais de modelagem e implementação foram analisadas e validadas pela autora.

