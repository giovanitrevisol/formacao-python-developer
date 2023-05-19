'''
IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:
 - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns
   casos, é necessário converter/tratar os dados de entrada;
 - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a
   impressão dos dados de saída.
'''
N = int(input())

a = []
b = []
for numero in range(N):
    ab = input()
    part = ab.split(" ")
    a.append(part[0])
    b.append(part[1])

for position in range(N):
    if len(a[position]) < len(b[position]):
        print("nao encaixa")
    elif a[position].endswith(b[position]):
        print("encaixa")
    else:
        print("nao encaixa")
