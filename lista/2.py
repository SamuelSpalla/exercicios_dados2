lista = []

for c in range(1,5):
    lista.append(float(input(f'Digite a {c} nota: ')))

m = sum(lista) / len(lista)

print(f'A média é: {m}')

if m >= 7:
    print('Aprovado')
else:
    lista.append(float(input('Digite a nota final: ')))
    m = sum(lista) / len(lista)
    if m >= 5:
        print('Aprovado')
    else:
        print('Reprovado')
    