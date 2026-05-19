#Sorteador de Alunos - Ordem de Apresentação

import random

a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')

alunos = [a1, a2, a3, a4]

# O shuffle "mistura" a sua lista original, como se estivesse embaralhando cartas
random.shuffle(alunos)

print('\n--- ORDEM DO SORTEIO ---')


ordem = 1
for aluno in alunos:
    print(f'{ordem}º sorteado: {aluno}')
    ordem = ordem + 1