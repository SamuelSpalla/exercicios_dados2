lista = []

for c in range(1,5):
    lista.append(float(input(f'Digite a {c} nota: ')))

print(f'A média é: {sum(lista) / len(lista)}\n'
    f'A maior nota é: {max(lista)}\n'
    f'A menor nota é: {min(lista)}')
    