metros = int(input('Digite valor em metros para converter: '))
km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 100
ml = metros * 1000

print('{} metros convertido para centimetro: {} cm \n em milimetros: {} mm \n decímetro {} dm \n decâmetro {} dam \n hectômetro {} hm \n quilômetro {} km'.format(metros, cm, ml,dm , dam, hm, km ))