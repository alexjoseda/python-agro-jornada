"""Exercício resolvido: insert, append, del e len."""

culturas = ["soja", "milho", "algodão"]
culturas.insert(1, "café")
culturas.append("trigo")
del culturas[2]
print(culturas)
print(len(culturas))
# Esperado: ['soja', 'café', 'algodão', 'trigo'] e 4
