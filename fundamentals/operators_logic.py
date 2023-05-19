"""
OPERATORS LOGICS
 AND
 OR
 not
"""



print(True and True and True)
print(True and False and True)
print(False and False and False)
print(True or True or True)
print(True or False or False)
print(False or False or False)

balance = 1000
with_dawn = 250
limit = 200
special_account = True

exp = balance >= with_dawn and with_dawn <= limit or special_account and balance >= with_dawn
print(exp)

exp_2 = (balance >= with_dawn and with_dawn <= limit) or (special_account and balance >= with_dawn)
print(exp_2)

conta_normal_com_saldo_suficiente = balance >= with_dawn and with_dawn <= limit
conta_especial_com_saldo_suficiente = special_account and balance >= with_dawn

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)

print("negation")
print(not 1000 > 2000)
print(not 10 < 15)