    #Sistema de aumento de 15% do Salário
salario = float(input('Qual é o salario do Funcionario? $'))
aumento = salario + (salario*15 / 100)
print('Um funcionario que ganhava R${:.2f}, com 15''%' ' de aumento,  vai passar a ganhar R${:.2f} '.format(salario, aumento))