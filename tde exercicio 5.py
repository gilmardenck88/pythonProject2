preço = float(input('Qual é o preço do produto? R$ '))
parc3 = (preço + (preço * 5 / 100)) / 3
parc2 = preço / 2
desconto = preço - (preço * 5 / 100)
print('o preço do produto que custava R${}, com 5% de juros custara 3 parcelas de R${}'.format(preço, parc3))
print('o preço do produto que custava R${}, sem juros custara 2 parcelas de R${}'.format(preço, parc2))
print('o preço do produto que custava R${}, com desconto de 5% a vista custara R${}'.format(preço, desconto))