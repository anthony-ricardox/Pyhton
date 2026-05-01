largura = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = largura * alt
tinta = area / 2
print(' Sua parede tem dimensão de {:.0f}x{:.0f} e sua área é de {}m²'.format(largura,alt, area))
print('Vai precisar de {}l de tinta para pintar {}m²'.format(tinta, area))

        