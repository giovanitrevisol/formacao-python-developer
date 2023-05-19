nome_2 = "gIoVani TreVIsol"

print(nome_2.upper())
print(nome_2.lower())
print(nome_2.title())

print("============")
print("--> Remove spaces")
texto = "  Olá mundo!    "
print(texto + ".")
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")


print("============")
menu = "Python"
print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#"))
print("-".join(menu))

print("===================")
nome_2 = "Giovani"
idade = 28
profissao = "Progamador"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Guilherme", "idade": 28}

print("Nome: %s Idade: %d" % (nome_2, idade))

print("Nome: {} Idade: {}".format(nome_2, idade))

print("Nome: {1} Idade: {0}".format(idade, nome_2))
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome_2))

print("Nome: {nome} Idade: {idade}".format(nome=nome_2, idade=idade))
print("Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome_2))
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome_2} Idade: {idade}")
print(f"Nome: {nome_2} Idade: {idade} Saldo: {saldo:.2f}")
print(f"Nome: {nome_2} Idade: {idade} Saldo: {saldo:10.1f}")

print("===================")
nome_3 = "Giovani Trevisol"

print(nome_3[0])
print(nome_3[-2])
print(nome_3[:9])
print(nome_3[10:])
print(nome_3[10:16])
print(nome_3[10:16:2])
print(nome_3[:])
print(nome_3[::-1])

print("========================")
my_name = "Giovani"

mensagem = f"""
   Olá meu nome é {my_name},
 Eu estou aprendendo Python.
     Essa mensagem tem diferentes recuos.
"""

print(mensagem)


print(
    """
    ============= MENU =============

    1 - Depositar
    2 - Sacar
    0 - Sair

    ================================

            Obrigado por usar nosso sistema!!!!
"""
)

PI = 3.14159
print(f"Valor de PI: {PI:.2f}")

curso = "Python"
print(curso[::-1])
print(f"Bem vindo ao curso de {curso.upper()}!")