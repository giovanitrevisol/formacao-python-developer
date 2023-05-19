'''
IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:
 - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns
   casos, é necessário converter/tratar os dados de entrada;
 - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a
   impressão dos dados de saída.
- "dict{}": dicionários possuem uma relação de chave - valor. Para cada chave haverá um valor.
'''
month = int(input())

months_dict = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
               "November", "December"]

if month == 1:
    print(months_dict[0])
elif month == 2:
    print(months_dict[1])
elif month == 3:
    print(months_dict[2])
elif month == 4:
    print(months_dict[3])
elif month == 5:
    print(months_dict[4])
elif month == 6:
    print(months_dict[5])
elif month == 7:
    print(months_dict[6])
elif month == 8:
    print(months_dict[7])
elif month == 9:
    print(months_dict[8])
elif month == 10:
    print(months_dict[9])
elif month == 11:
    print(months_dict[10])
else:
    print(months_dict[11])
