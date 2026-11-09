"""Aula 06: sort, sorted, reverse e len."""

culturas = ["soja", "algodão", "milho"]
print("Original:", culturas)
print("Ordenada temporariamente:", sorted(culturas))
print("Original preservada:", culturas)

culturas.sort()
print("Ordenação permanente:", culturas)

culturas.reverse()
print("Ordem invertida:", culturas)
print("Quantidade de culturas:", len(culturas))
