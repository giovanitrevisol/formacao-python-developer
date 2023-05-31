import socket
import sys


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print('Conexão falhou!')
        print('Erro: {}'.format(e))
        sys.exit()
    print('Socket criado com sucesso.\n')

    host_alvo = input('Digite o host ou Ip a ser conectado: ')
    port_alvo = input('Digite a porta a ser conectada: ')

    try:
        s.connect((host_alvo, int(port_alvo)))
        print('Client TCP conectado com sucesso no host ' + host_alvo + ' e na porta ' + port_alvo)
        s.shutdown(2)
    except socket.error as e:
        print('Conexão falhou: ' + host_alvo + ', ' + port_alvo)
        print('Erro: {}'.format(e))
        sys.exit()


if __name__ == '__main__':
    main()
