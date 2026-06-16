Sistema de Controle de Produção Artesanal de Crochê

Descrição do Projeto

O Sistema de Controle de Produção Artesanal de Crochê tem como objetivo auxiliar artesãos no gerenciamento da produção, controle de materiais, cadastro de produtos e acompanhamento de pedidos realizados por clientes.

O sistema permite organizar as informações relacionadas à fabricação de peças de crochê, controlar o estoque de materiais utilizados na produção e registrar pedidos efetuados pelos clientes.

O projeto foi desenvolvido seguindo os princípios da Programação Orientada a Objetos (POO), buscando modularidade, reutilização de código e facilidade de manutenção.

Objetivos

Gerenciar clientes e seus pedidos.

Controlar produtos artesanais confeccionados.

Gerenciar materiais utilizados na produção.

Registrar receitas de fabricação das peças.

Controlar processos de produção.

Calcular custos de fabricação.

Organizar informações de forma estruturada e orientada a objetos.

Diagrama de Classes

Inserir aqui a imagem do diagrama UML.

Exemplo:

Diagrama UML

Descrição das Classes

Cliente

Representa o cliente que realiza pedidos no sistema.

Atributos

id

nome

telefone

Métodos

realizarPedido()

Pedido

Representa uma solicitação de compra realizada por um cliente.

Atributos

id

dataPedido

status

valorTotal

Métodos

calcularTotal()

ItemPedido

Representa um item pertencente a um pedido.

Atributos

quantidade

subtotal

Métodos

calcularSubtotal()

Produto

Representa uma peça artesanal produzida em crochê.

Atributos

id

nome

descricao

precoVenda

tempoProducao

Métodos

calcularCusto()

ReceitaCroche

Representa a composição de materiais necessária para produzir um produto.

Atributos

id

quantidadeNecessaria

Cada objeto ReceitaCroche relaciona um produto a um material e define a quantidade necessária daquele material para a produção.

Material

Representa os insumos utilizados na fabricação dos produtos.

Atributos

id

nome

quantidadeEstoque

unidadeMedida

custoUnitario

Métodos

atualizarEstoque()

Producao

Representa o processo de fabricação de um produto.

Atributos

id

dataInicio

dataFim

status

quantidadeProduzida

Métodos

iniciar()

finalizar()

Relacionamentos

Um Cliente pode realizar vários Pedidos.

Um Pedido possui vários Itens de Pedido.

Um ItemPedido referencia um Produto.

Um Produto possui várias Receitas de Crochê.

Cada Receita de Crochê utiliza um Material.

Um Produto pode possuir diversos registros de Produção.

Pilares da Programação Orientada a Objetos

Encapsulamento

Os atributos das classes são privados e acessados por meio de métodos específicos, garantindo segurança e controle sobre os dados.

Exemplo

private String nome;

public String getNome() {
    return nome;
}
Abstração

Cada classe representa uma entidade do mundo real relacionada ao processo produtivo artesanal.

Exemplos:

Cliente

Pedido

Produto

Material

Produção

Herança

Embora não tenha sido necessária na modelagem inicial, o sistema pode ser expandido futuramente utilizando herança.

Exemplo:

Pessoa
 ├── Cliente
 └── Funcionario
Polimorfismo

Pode ser utilizado futuramente para cálculos específicos de custos ou diferentes tipos de produtos artesanais.

Exemplo:

public double calcularCusto() {
    // implementação específica
}
Padrões de Projeto Utilizados

Factory Method

O padrão Factory Method será utilizado para centralizar a criação dos objetos do sistema.

Exemplo

ProdutoFactory.criarProduto(
    "Amigurumi Coelho",
    80.00
);
Benefícios

Reduz acoplamento.

Facilita manutenção.

Centraliza a lógica de criação.

Padrão Strategy

O padrão Strategy foi utilizado para permitir diferentes formas de cálculo do preço de venda dos produtos artesanais.

Por meio desse padrão, as regras de negócio ficam desacopladas da classe Produto, permitindo que novas estratégias sejam adicionadas sem alterar o código existente.

Exemplos de estratégias implementadas:

Cálculo com margem de lucro de 30%.
Cálculo com margem de lucro de 50%.
Possibilidade futura de descontos promocionais.

Benefícios

Maior flexibilidade.
Menor acoplamento.
Facilidade de manutenção.
Segue o princípio Open/Closed da orientação a objetos. 

Funcionalidades Implementadas

Cadastro de clientes.

Cadastro de produtos.

Cadastro de materiais.

Registro de pedidos.

Registro de itens de pedido.

Controle de produção.

Controle de estoque.

Cálculo de custo de produção.

Associação entre produtos e materiais através da ReceitaCroche.

Como Executar o Projeto

Pré-requisitos

Java JDK 17 ou superior

Git

IDE (IntelliJ, Eclipse ou VS Code)

Clonar o Repositório

git clone https://github.com/seu-usuario/seu-repositorio.git
Executar

cd projeto-croche
Abrir o projeto na IDE e executar a classe principal:

Main.java
Testes

Os testes podem ser executados através do framework JUnit.

Exemplo:

mvn test
ou

gradle test
Detalhamento de Aprendizado

Durante o desenvolvimento deste projeto foram aplicados conceitos fundamentais de Programação Orientada a Objetos, como encapsulamento, abstração e modelagem de classes.

Também foi possível compreender a importância da modelagem UML no planejamento do software, além da aplicação de padrões de projeto para tornar o sistema mais organizado e flexível.

O desenvolvimento contribuiu para o entendimento das relações entre objetos, controle de estoque, gerenciamento de produção e organização de sistemas voltados para pequenos negócios.

Declaração de Uso de IA

Ferramentas de Inteligência Artificial foram utilizadas como apoio para:

Revisão da modelagem UML;

Sugestões de estruturação do projeto;

Auxílio na documentação;

Explicação de conceitos relacionados à Programação Orientada a Objetos e padrões de projeto.

Todas as decisões de implementação, modelagem e validação foram analisadas e adaptadas pelo autor do projeto, que permanece responsável pelo conteúdo final desenvolvido.

