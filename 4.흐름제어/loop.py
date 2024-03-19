# for loo
# for i in range(1, 5):

#     print(i)
    
#while문
# i = 0
# while i < 5:
#     print(i)
#     i = i + 1

# for loop에 else 사용
# for i in range(1, 5):
#     print(i)
# else:
#     print("반복이 완료되었습니다.")

# fruits = ["사과","딸기","복숭아","참외"]

# for fruit in fruits:
#     #print(f"{fruits}이(가) 과일 바구니에 있습니다.")
#     print(f"{fruit}이(가) 과일 바구니에 있습니다.")

# #if 추가
# for fruit in fruits:
#     if fruit == "사과":
#         print(f"사과는 맛있습니다.")
#     #print(f"{fruits}이(가) 과일 바구니에 있습니다.")
#     print(f"{fruit}이(가) 과일 바구니에 있습니다.")


#무한 루프, 입력 대기가 필요할 때 고의로 무한루프 만들 때가 있다.
# while True:
#     user_input = input("명령어를 입력해주세요: ")
#     if user_input == "exit":
#         break
#     else:
#         pass        #TodoL 차후 계발 예정


# 구구단 프로그램
# 1~9단, n * 1 ~ n * 9
# for x in range(1,10):
#     for y in range(1, 10):
#         print(f"{x} * {y} = {x * y}")


# enumerate 활용하기
fruits = ["Apple", "Banana", "Blueberry", "Peach"]

# index = 1
# for fruit in fruits:
#     print(f"{index}번째 과일은 {fruit} 입니다.")
#     index = index + 1

# enumerate 적용 하여 같은 것을 단순화 가능
# for index, fruit in enumerate(fruits, start=1):
#     print(f"{index}번째 과일은 {fruit} 입니다.")



# 팩토리얼 구휴ㅏ기
# n! = n * (n-1) * ... * 2 * 1
num = 5
result = 1
for i in range(1, num + 1):
    result = result * i

print(f"{num}! 은 {result} 입니다.")