import hashlib
import os

file1 = 'testA.txt'
file2 = 'testB.txt'

f = open(file1, 'w')
f.write('Python Segurança!\n__')
f.close()

f = open(file2, 'w')
f.write('Python Segurança!!\n__')
f.close()
###################

hash1 = hashlib.new('ripemd160')
hash1.update(open(file1, 'rb').read())
# print(hash1,'\n',hash1.digest())

hash2 = hashlib.new('ripemd160')
hash2.update(open(file2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f'O arquivo {file1} é diferente do arquivo {file2}!\n')
else:
    print(f'Os arquivos {file1} e {file2} são iguais!\n')

print('hash1: ', hash1.hexdigest())
print('hash2: ', hash2.hexdigest())

if os.path.exists(file1): os.remove(file1)
if os.path.exists(file2): os.remove(file2)
