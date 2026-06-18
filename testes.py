from material import Material
from receitacroche import ReceitaCroche
from produto_factory import ProdutoFactory
from cliente import Cliente
from pedido import Pedido

materiais = []
produtos = []
clientes = []
pedidos = []


while True:

  print("\n===== SISTEMA CROCHÊ =====")
  print("1 - Cadastrar Material")
  print("2 - Cadastrar Produto")
  print("3 - Listar Materiais")
  print("4 - Listar Produtos")
  print("5 - Cadastrar Cliente")
  print("6 - Criar Pedido")
  print("0 - Sair")

  opcao = input("Escolha uma opção: ")

  if opcao == "1":

    print("\n=== Cadastro de Material ===")

    id_material = int(input("ID: "))
    nome = input("Nome: ")
    estoque = float(input("Quantidade em estoque: "))
    unidade = input("Unidade de medida: ")
    custo = float(input("Custo unitário: "))
    material = Material(id_material,nome,estoque,unidade,custo)

    materiais.append(material)
    print("material cadastrado com sucesso!")

  elif opcao == "2":
    if len(materiais) == 0:
        print("Cadastre um material primeiro!")
        continue

    print("\n=== Cadastro de Produto ===")

    id_produto = int(input("ID: "))
    nome = input("Nome: ")
    descricao = input("Descrição: ")
    preco = float(input("Preço de venda: "))
    tempo = int(input("Tempo de produção: "))

    produto = ProdutoFactory.criar_produto(id_produto,nome,descricao,preco,tempo)

    print("\nMateriais cadastrados:")

    for i, material in enumerate(materiais):
            print(f"{i} - {material.nome}")

    indice = int(input("Escolha o material utilizado: "))

    quantidade = float(input("Quantidade necessária: "))

    receita = ReceitaCroche(1,materiais[indice],quantidade )

    produto.adicionar_material(receita)

    produtos.append(produto)

    print("Produto cadastrado!")

    print(f"Custo de produção: "f"R$ {produto.calcular_custo():.2f}")

  elif opcao == "3":
        print("\n=== Materiais ===")

        for material in materiais:
            print(material)
  elif opcao == "4":
    if len(clientes) == 0:
        print("Cadastre um cliente primeiro!")
        continue

    print("\n=== Clientes ===")

    for i, cliente in enumerate(clientes):
        print(f"{i} - {cliente.nome}")

    indice = int(input("Escolha o cliente: "))

    pedido = Pedido(len(pedidos) + 1)

    pedidos.append(pedido)

    print("Pedido criado com sucesso!")
  elif opcao == "5":
    print("\n=== Cadastro de Cliente ===")

    id_cliente = int(input("ID: "))
    nome = input("Nome: ")
    telefone = input("Telefone: ")

    cliente = Cliente(id_cliente,nome,telefone)

    clientes.append(cliente)

    print("Cliente cadastrado!")
  elif opcao == "6":

    if len(clientes) == 0:
        print("Cadastre um cliente primeiro!")
        continue

    print("\n=== Clientes ===")

    for i, cliente in enumerate(clientes):
        print(f"{i} - {cliente.nome}")

    indice = int(input("Escolha o cliente: "))

    pedido = Pedido(len(pedidos) + 1)

    pedidos.append(pedido)

    print("Pedido criado com sucesso!")
  elif opcao == "0":
    print("Sistema encerrado.")
    break

  else:
      print("Opção inválida.")