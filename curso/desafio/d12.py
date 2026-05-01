preco = float(input('Qual o preço do produto?  R$'))
novo = preco -  (preco *5 /100)

print('O preço custava R${} e na promoção com desconto de 5% vai custar  R${:.2f}'.format(preco, novo))