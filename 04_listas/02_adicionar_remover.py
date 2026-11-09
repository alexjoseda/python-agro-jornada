"""Aula 05: append, insert, del, remove e pop."""

culturas = ["soja", "milho", "algodão"]
print("Original:", culturas)

culturas.append("trigo")
print("Após append:", culturas)

culturas.insert(1, "café")
print("Após insert:", culturas)

del culturas[2]  # Remove 'milho' porque está no índice 2.
print("Após del:", culturas)

culturas.remove("café")  # Remove pelo valor.
print("Após remove:", culturas)

ultima_cultura = culturas.pop()  # Remove e devolve o último elemento.
print("Removida por pop:", ultima_cultura)
print("Lista final:", culturas)
