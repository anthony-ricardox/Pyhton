import math

n1 = int(input('Digite um numero: '))
dobro = n1 + n1
triplo = n1 * 3
raiz = math.sqrt(n1)

print('O dobro de {} é: {} \n Triplo : {} \n A raiz quadrada de {} é : {:.2f}'.format(n1,dobro, triplo, n1, raiz))