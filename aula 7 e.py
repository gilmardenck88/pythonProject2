n = 1
p = 0
i = 0
while n <= 10:
    a = int(input())
    n = n + 1
    if a % 2 == 0:
       a = p
       a5P = p + 1
    else:
       a = i
       i = i + 1
print("A qtd de números pares é: ", p)
print("A qtd de números ímpares é: ", i)