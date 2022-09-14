# aula 6 exercicio 5
lab = float(input('Digite a nota do trabalho de laboratorio: '))
semest = float(input('digite a nota da avaliaçao semestral: '))
exam = float(input('digite a nota do exame final: '))

nota = ((2 * lab) + (3 * semest) + (5* exam)) / 3

if nota <= 2.9:
    print('reprovado')
elif nota <= 4.9:
    print('recupereção')
elif nota >= 5:
    print('aprovado')