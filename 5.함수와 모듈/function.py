# 함수 정의
# def func():
#     print("This is Function. hello!")

# func()

# 인자 전달 활용    
# def func(name):
#     print(f"This is Function. hello {name}")
# func("Park")

# 반환값 활용
def sum(num1, num2):
    return num1 + num2

# result = sum(3,5)
# print(result)


def div(num1, num2):
    if num2 == 0:
        return 0
    print("Divisioning...")
    return num1 / num2
result = sum(3, 5)
print(result)

result_div = div(3, 2)
print(result_div)
result_div = div(3, 0)
print(result_div)




    