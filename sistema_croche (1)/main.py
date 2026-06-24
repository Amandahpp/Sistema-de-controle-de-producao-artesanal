from modelos.material import Material
from modelos.receitacroche import ReceitaCroche
from fabricas.produto_factory import ProdutoFactory
from modelos.cliente import Cliente
from modelos.pedido import Pedido
from modelos.itempedido import ItemPedido
from modelos.producao import Producao

print("=== ATELIE ARTE EM CROCHE ===")

# Cadastro de material
linha = Material(1, "Linha Amigurumi", 50, "novelos", 12.50, 5)

# Cadastro de produto usando Factory
urso = ProdutoFactory.criar_produto(
    "amigurumi",
    1,
    "Urso de Crochê",
    "Urso artesanal",
    80.00,
    4
)

# Associação de material ao produto
receita = ReceitaCroche(1, linha, 2)
urso.adicionar_material(receita)

print(f"Produto: {urso.nome}")
print(f"Custo de produção: R$ {urso.calcular_custo():.2f}")

# Cadastro de cliente
cliente = Cliente(1, "Amanda", "54999999999")

# Criação de pedido
pedido = Pedido(1, cliente)

# Adicionando item ao pedido
item = ItemPedido(urso, 2)
pedido.adicionar_item(item)

print("\n=== PEDIDO ===")
print(pedido)

# Teste do State Pattern
print("\n=== ESTADOS DO PEDIDO ===")
print("Estado atual:", pedido.mostrar_estado())

pedido.alterar_estado()
print("Estado atual:", pedido.mostrar_estado())

pedido.alterar_estado()
print("Estado atual:", pedido.mostrar_estado())

# Teste da produção
print("\n=== PRODUÇÃO ===")

producao = Producao(1, urso, 5)

print(producao)

producao.iniciar()
print(producao)

producao.finalizar()
print(producao)
