import hashlib

# String='Python Security'
String = input('Digite o texto a ser encriptado: ')

Dic = {'md5': hashlib.md5, 'sha1': hashlib.sha1, 'sha256': hashlib.sha256, 'sha512': hashlib.sha512}
list_name = list(Dic.keys())

op = input('''\n#### MENU - Tipo de HASH ####
1) MD5
2) SHA1
3) SHA256
4) SHA512
Digite o número da opção desejada: ''')
print()

try:
    op = int(op)
    op -= 1
    result = Dic[list_name[op]](String.encode('utf-8'))
    print(f'Hash {list_name[op]} de \"{String}\": {result.hexdigest()}')
except:
    print('Erro: Opção incorreta.')
