import socket
import sys


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error as e:
        print('Conexão falhou!')
        print('Erro: {}'.format(e))
        sys.exit()
    print('Socket criado com sucesso.\n')

    host = 'localhost'
    port = 5432

    s.bind((host, port))
    # print('Bind: ',s.bind((host,port)) )	#None
    # mensagem='\n\tServidor: sucesso Cliente!'

    i = 0
    while 1:
        data, end = s.recvfrom(4096)
        if data:
            print('Servidor enviando mensagem...')
            mensagem = '\nServidor: sucesso Cliente! [id: {}]'.format(i)
            s.sendto(data + (mensagem.encode()), end)
            i += 1
            if i > 5: sys.exit()


if __name__ == '__main__':
    main()
