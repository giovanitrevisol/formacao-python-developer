import socket
import sys


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as e:
        print('Conexão falhou!')
        print('Erro: {}'.format(e))
        sys.exit()
    print('Cliente Socket criado com sucesso.\n')

    host = 'localhost'
    port = 5433
    mensagem = 'Servidor, Oi, sucesso?'

    try:
        # print('Cliente: '+mensagem)
        s.sendto(mensagem.encode(), (host, 5432))

        data, server = s.recvfrom(4096)
        data = data.decode()
        print('Cliente: ' + data)
    finally:
        print('\nCliente: Fechando a conexão.')
        s.close()


if __name__ == '__main__':
    main()
