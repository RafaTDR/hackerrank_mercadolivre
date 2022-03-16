##Complete a seguinte função para que a mesma devolva todos os possíveis números de 4 dígitos, 
##onde cada um seja menor ou igual a<maxDigit>, e a soma dos dígitos de cada número gerado seja 21
##Exemplo maxDigit=6: 3666, 4566...

n = 1000
nm = 7770
maxDigit = 6
somaDigit = 21

while n <= nm:
    
    numero = list(str(n))
    soma = 0
    for i in numero:
        
        if int(i) <= maxDigit:
            
            soma = soma + int(i)
            if soma == somaDigit:
                print(n)
        else:
            pass

    n = n + 1
    
    
