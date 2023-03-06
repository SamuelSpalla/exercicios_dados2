lista = []

for c in range(1,5):
    lista.append(float(input(f'Digite a {c} nota: ')))

print(f'A média é: {sum(lista) / len(lista)}')
    