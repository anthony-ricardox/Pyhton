tabuada = int(input('Digite um numero para tabuada: '))
contador = 0

while contador <= 10:
    x = tabuada * contador
    print('{} X {} = {} \n '.format(tabuada, contador ,x) )
    contador += 1