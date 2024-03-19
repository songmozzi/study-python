# 변수의 선언
var = 42

#print(var) # 42

#print(var + 10)
#print(var - 5)
#print(var / 10)
#print(var // 10)
#print(var % 10)

# 변수에 다른 변수를 지정할 수 있다.
var2 = var / 10

#print(var > var2) # True

var_float = 3.14
#print(var_float * 6)
#print(var_float / 2)

result = var * 10 + 5 # 425
print(result)
result = 5 + var * 10 # 425
print(result)
result = (5 + var) * 10 # 470
print(result)

is_true = True
is_false = False

print(is_true and is_true) # true
print(is_true and is_false) # False
print(is_false and is_false) # False

print(is_true or is_true) # true
print(is_true or is_false) # true
print(is_false or is_false) # False

