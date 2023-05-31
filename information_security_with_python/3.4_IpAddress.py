import ipaddress

print('#' * 20)

ip = '192.168.0.1'
endereco = ipaddress.ip_address(ip)

print(endereco)
print(endereco + 255)
print(endereco + 256)
print(endereco + 2000)

###################
print('#' * 20)

ip = '192.168.0.0/24'
rede = ipaddress.ip_network(ip)
print(rede)

ip = '192.168.0.100/24'
rede = ipaddress.ip_network(ip, strict=False)
print(rede)
###################
print('#' * 20)

# ip='192.168.0.0/0'	#4 bilhoes de ips
# ip='192.168.0.0/4'
# ip='192.168.0.0/16'
# ip='192.168.0.0/24'
ip = '192.168.0.0/32'
rede = ipaddress.ip_network(ip, strict=False)

for ip in rede:
    print(ip)

print('#' * 20)
