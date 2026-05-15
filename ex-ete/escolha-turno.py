nome = input('Qual seu nome? ')

while True:

    print('*' * 30)
    print('        SISTEMA DE TURNOS        \n')
    print('M = Matutino')
    print('V = Vespertino')
    print('N = Noturno')
    print('*' * 30)

    turno = input('Qual turno você estuda? ').upper().strip()

    match turno:
        case 'M':
            print('Bom dia, {}!'.format(nome))
            break

        case 'V':
            print('Boa tarde, {}!'.format(nome))
            break

        case 'N':
            print('Boa noite, {}!'.format(nome))
            break

        case _:
            print('Opção inválida! Tente novamente.')