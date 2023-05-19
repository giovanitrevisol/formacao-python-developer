N = int(input())

values = []

for numero in range(N):
    point = int(input())
    values.append(point)

for position in range(len(values)):
    if values[position] > 8000:
        print("Mais de 8000!")
    else:
        print("Inseto!")