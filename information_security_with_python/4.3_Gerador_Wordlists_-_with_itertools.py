import itertools

result = itertools.permutations('abc', 3)
##result: <itertools.permutations object ...>
###################
String = input('String a ser permutada: ')

len_result = 4
len_result = len(String)
result = itertools.permutations(String, len_result)
# result=itertools.permutations(String)

for c in result:
    ##print(c)
    print(''.join(c))
###################
