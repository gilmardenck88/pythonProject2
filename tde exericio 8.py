raio = float(input(' informe o raio: '))
altura = float(input('informe a altura: '))
area = 2 * 3.14 * raio * (altura + raio)
print('Area primeira método:{:.2f}'.format(area))

ab = 3.14 * (raio ** 2)
al = 2 * 3.14 * raio * altura
at = 2 * ab + al

print( 'Área segundo método:{:.2f}'.format(at))



litros = area / 3.0
latas = litros / 5.0


print('Latas necessarias:{:.2f}'.format(latas))

custo = latas * 50.0
print('Custo total:R${:.2f}'.format(custo))

