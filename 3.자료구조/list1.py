# empty_list = []
# my_list = [10, 20, 30]
# print(my_list)

# 빈 리스트를 선언하고 append를 이용하여 채워 넣을 수 있다.
# my_list = []
# my_list.append(10)
# my_list.append(15)
# my_list.append(20)
# print(my_list)

# # 값이 들어있는 리스트는 뒤에 이어서 추가로 붙는다
# my_list = [30, 40, 50]
# my_list.append(10)
# my_list.append(15)
# my_list.append(20)
# print(my_list)

# # 길이 출력 가능
# print(len(my_list)) # 6

# # 특정 값 추출 가능
# element = my_list[4]
# print(element) # 15

# # 슬라이싱
# sliced = my_list[3:]
# print("Sliced: ", sliced) # 10, 15, 20


# fruits = ["banana", "apple", "blueberry", "cherry"]

# # 바나나가 포함되어 있나요?
# is_banana_included = "banana" in fruits
# print("Is banana included? ", is_banana_included)

# index_cherry = fruits.index("cherry")
# print("Cherry is ", index_cherry)

# # 리스트의 정렬
# numbers = [4, 2, 1, 3, 8, 6, 7, 5]
# print("Unsorted ", numbers)

# numbers.sort()
# print("Sorted ", numbers)

# numbers.sort(reverse=True)
# print("Sorted (Reverse) ", numbers)

# 리스트의 요소 추가 및 제거
my_list = []
my_list.append(10)
my_list.append(11)
my_list.append(12)
# print(my_list)

my_list.extend([13,14,15])
print(my_list)
# # my_list.append([16, 17]) # 리스트가 추가가 된다. 복합리스트가 됨
# # print(my_list) # [10, 11, 12, 13, 14, 15, [16, 17]]
# # print(my_list[-1])


# # 리스트 연산 (+, *) 

# new_list = my_list + [0,1,2]
# print(new_list)

# multi_list = [0,1,3] * 3
# print(multi_list)

# 리스트 삭제
print(my_list)
del my_list[0]
print(my_list)

# 최댓값, 최솟값
max_value = max(my_list)
min_value = min(my_list)
print(f"최대 값은 {max_value}, 최솟 값은 {min_value} 입니다")