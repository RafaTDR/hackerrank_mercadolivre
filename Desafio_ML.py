##Complete a seguinte função para que a mesma devolva todos os possíveis números de 4 dígitos, 
##onde cada um seja menor ou igual a<maxDigit>, e a soma dos dígitos de cada número gerado seja 21
##Exemplo maxDigit=6: 3666, 4566...

n = 1000
nm = 7770
maxDigit = int (input())
somaDigit = 21
count = 0
while n <= nm:
    
    numero = list(str(n))
    soma = 0
    x=1
    for i in numero:
        
        
        
        if int(i) <= maxDigit:
                
            soma = soma + int(i)
            if soma == somaDigit:
                    
                if x == 4:
                    print(n)
                    
                    count = count + 1
        else:
            pass
        x = x +1
    n = n + 1
if count == 0:
    print ("null")
    
    
    
