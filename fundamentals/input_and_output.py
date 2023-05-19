"""
INPUT AND OUTPUT
"""
name = input("Digite seu nome: \n")
last_name = input("Digite seu sobrenome: ")
print(f"O nome digitado é {name} {last_name}")

#know parameters in method print
print("---------------------------------------")
print(name, last_name)
print(name, last_name, end="...\n")
print(name, last_name, sep="#")

