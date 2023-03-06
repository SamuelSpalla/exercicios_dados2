num = int(input('Digite um numero: '))

def verificar(num):
    if num % 2 == 0:
        print('Par')
    else:
        print('Impar')

verificar(num)