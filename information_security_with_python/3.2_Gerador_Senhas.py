import random
import string


def gerar_senha(size):
    chars = string.ascii_letters + string.digits + 'ç!@#$%&*()-=+[]{},.;:|?'
    # print(chars)
    rnd = random.SystemRandom()  # usa os.urandom;

    password = ''.join(rnd.choice(chars) for i in range(size))
    print('Senha aleatoria gerada: ', password)


size = int(input('Digite o tamanho da senha: '))

gerar_senha(size)

for i in range(10):
    gerar_senha(size)
