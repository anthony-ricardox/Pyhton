import random

a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')

alunos = [a1, a2, a3, a4]
sorte = random.choice(alunos)
print(f'Aluno sorteado foi: {sorte}')