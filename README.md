🧶 Sistema de Controle de Produção Artesanal de Crochê
Sistema desenvolvido em Java utilizando Programação Orientada a Objetos (POO) para auxiliar artesãos no gerenciamento da produção de peças em crochê, controle de materiais, estoque e pedidos de clientes.
📋 Funcionalidades
👤 Cadastro de clientes
🛍️ Registro de pedidos
🧶 Cadastro de produtos artesanais
📦 Controle de materiais e estoque
📝 Registro de receitas de fabricação
🏭 Controle de produção
💰 Cálculo de custos de fabricação
🏗️ Tecnologias Utilizadas
Java 17
Programação Orientada a Objetos (POO)
UML
JUnit
📊 Diagrama UML
🧩 Estrutura do Sistema
Cliente
Responsável pelo cadastro dos clientes e realização de pedidos.
Pedido
Armazena informações dos pedidos realizados pelos clientes.
ItemPedido
Representa cada produto presente em um pedido.
Produto
Representa uma peça artesanal produzida em crochê.
Material
Representa os insumos utilizados na produção.
ReceitaCroche
Define quais materiais e quantidades são necessários para fabricar um produto.
Producao
Controla o processo de fabricação das peças.
🔗 Relacionamentos
Cliente
   │
   └── Pedido
           │
           └── ItemPedido
                     │
                     └── Produto
                              │
                              ├── ReceitaCroche
                              │          │
                              │          └── Material
                              │
                              └── Producao
🧠 Conceitos de POO Aplicados
Encapsulamento
Proteção dos atributos por meio de métodos getters e setters.
Abstração
Representação das entidades do mundo real através de classes.
Herança
Possibilidade de expansão futura.
Pessoa
 ├── Cliente
 └── Funcionario
Polimorfismo
Possibilidade de diferentes implementações para regras de negócio.
🎨 Padrões de Projeto
Factory Method
Centraliza a criação de objetos do sistema.
Strategy
Permite diferentes estratégias de cálculo de preço e custo dos produtos.
🚀 Como Executar
Clone o projeto
git clone https://github.com/seu-usuario/seu-repositorio.git
Entre na pasta
cd projeto-croche
Execute a aplicação
Abra o projeto em sua IDE favorita (IntelliJ, Eclipse ou VS Code) e execute a classe:
Main.java
🧪 Testes
mvn test
ou
gradle test
📚 Aprendizados
Este projeto permitiu aplicar conceitos de:
Programação Orientada a Objetos
Modelagem UML
Relacionamentos entre classes
Controle de estoque
Processos de produção
Padrões de Projeto
👨‍💻 Autor
Projeto desenvolvido para fins acadêmicos na disciplina de Programação Orientada a Objetos.
🤖 Uso de Inteligência Artificial
Ferramentas de IA foram utilizadas como apoio para:
Revisão da modelagem UML;
Organização da documentação;
Explicação de conceitos de POO;
Sugestões de melhorias no projeto.
Todas as decisões finais de modelagem e implementação foram analisadas e validadas pelo autor.

