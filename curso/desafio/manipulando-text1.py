nome = input('Digite o nome completo: ')

up = nome.upper()
low = nome.lower()

# Quantidade de letras sem contar espaços
letras = len(nome.replace(' ', ''))

# Primeiro nome
primeiro_nome = nome.split()[0]
primeira = len(primeiro_nome)

print('Seu nome é {}, tudo em maiúsculo ficará: {}'.format(nome, up))
print('Tudo em minúsculo ficará: {}'.format(low))
print('Seu nome ao todo tem {} letras'.format(letras))
print('Primeiro nome tem {} letras'.format(primeira))