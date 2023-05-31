import os

print('#' * 56)
ip_host = input('Digite o Ip ou host a ser verificado: ')
# ip_host='www.google.com'
print('-' * 56)

# -c é utilizado para especificar o número de pacotes
os.system('ping -c 6 {}'.format(ip_host))

print('#' * 56)

# time.sleep(2)
