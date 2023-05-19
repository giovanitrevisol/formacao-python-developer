"""
TYPE CONVERT
"""

age = 30
price = 10.9
print(price)

print(price / 2)
print(price // 2) # Return type int

text = f"Age {age} price {price}"
print(text)

# SHOW VARIABLE TYPE
my_name = "Giovani Trevisol"
my_age = 30
print("")
print("SHOW TYPE")
print(type(my_name))
print(type(my_age))

# CONVERT STRINT TO NUMBER
print("")
print("CONVERT STRINT TO NUMBER")
price_string = "99.91"
age_string = "30"

print(float(price_string))
print(int(age_string))

print("")
print("ERROR TO CONVERT STRING TO NUMBER")
price_string_fail = "Giovani"
print(float(price_string_fail))
