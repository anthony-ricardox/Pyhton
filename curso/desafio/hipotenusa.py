import  math

oposto = float(input('Qual comprimento do cateto oposto: '))
adja = float(input('Qual comprimento do cateto adjacente: '))

hipot = math.hypot(oposto, adja)

print(f'O comprimento da hipotenusa é: {hipot:.2f}')