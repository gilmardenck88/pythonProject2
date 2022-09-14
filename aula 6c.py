# exercicio 4 aula 6

salario = float(input('digite o salãrio: '))
prestaç = float(input('digite a prestaçao: '))

if prestaç > salario * 20 / 100:
    print('esmprestimo não concedido concedido')
else:
    print('empréstimo concedido')