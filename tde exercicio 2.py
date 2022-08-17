from datetime import date
atual = date.today().year
nasc = int(input('em que ano a pessoas nasceu? '))
idade =  atual - nasc + 10
print('Essa pessoa terá em 2032 {} anos'.format(idade))

