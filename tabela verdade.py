tabelaVerdade  = [] # A tabela deve ser criada fora e antes da função
def  geraTabelaVerdade ( m , n ): # Função para gerar uma tabela verdade (número de variáveis ​​da tabela(fixo), número de variáveis ​​da tabela(recursivo))
    bits = 2 ** m  # determina quantos linhas terá a tabela, valor fixo
    repeticoes_coluna = ( bits // ( 2 ** n )) * 2
    repeticoes_linha = ( 2 ** n // 2 ) // 2
    contador = 0  # Esse contador será sempre incrementado até a quantidade de bits e será zerado quando a função repetir
    if  not  tabelaVerdade : # essa condição cria a primeira coluna da tabela

            tabelaVerdade . anexar ( '0' )

            tabelaVerdade . anexar ( '1' )


            [ contador ] =  tabelaVerdade [ tabela ] + '  0'
            contador  +=  1

            [ contador ] =  tabelaVerdade [ tabela ] +  ' 1 '
            contador  +=  1
    se  n == 1 :
        voltar  tabelaVerdade
    mais :
        return  geraTabelaVerdade ( m , n - 1 )

qtdVT = 5  # quantidade de variáveis ​​da tabela verdade
matrizTabelaVerdade  =  geraTabelaVerdade ( qtdVT , qtdVT )

for  i  in  range ( len ( matrizTabelaVerdade )): # apenas para imprimir uma linha abaixo da outra
    imprimir ( matrizTabelaVerdade [ i ])