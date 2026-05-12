        #Aluguel de Carros



km = float(input('Quantos Km pecorrido? '))
dia = int(input('Quantos dias  o carro foi alugado? '))
pago = (km * 0.15) + (dia * 60)


print('O total a Pagar é de: R${:.2f}'.format(pago))
