from material import Material
from receitacroche import ReceitaCroche
from produtocroche import Produto

linha = Material(
    1,
    "Linha Amigurumi",
    100,
    "m",
    0.50
)

receita = ReceitaCroche(
    1,
    linha,
    20
)

urso = Produto(
    1,
    "Urso de Crochê",
    "Amigurumi",
    80,
    5
)

urso.receitas.append(receita)

print("Custo:", urso.calcular_custo())