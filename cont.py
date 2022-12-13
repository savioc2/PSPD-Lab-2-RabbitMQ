number_of_words = 0
i = 0 
cont1 = 0
cont2 = 0
cont3 = 0

with open(r'file.txt','r') as file:

    data = file.read()
    lines = data.split()
    number_of_words += len(lines)

    for j in data.split():
        if j == " " or "\n" or "\t":
            if len(j) < 6:
                cont1=cont1+1
            elif len(j) >= 6 and len(j) <= 10:
                cont2=cont2+1

# contabilizar todas as palavras com menos de 6 caracteres (i)
print(">6", cont1)
# contabilizar as palavras que tenham entre 6 e 10 caracteres (ii)              
print("6 & 10", cont2)
# contabilizar todas as palavras do arquivo de entrada (iii)
print("Total de palavras:",number_of_words)