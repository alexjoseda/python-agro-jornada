"""Exemplo de solução do desafio: cadastro de máquinas agrícolas.

Reescreva sem consultar este arquivo para praticar de verdade.
"""

maquinas = ["trator", "pulverizador", "colheitadeira"]
print("Primeiro equipamento:", maquinas[0])

maquinas.append("drone")
maquinas.insert(1, "robô agrícola")
maquinas.remove("pulverizador")
maquinas.sort()

print("Lista final:", maquinas)
print("Quantidade de equipamentos:", len(maquinas))
