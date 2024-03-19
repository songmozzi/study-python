#집합형 자료 구조

#빈 셋 정의
empty_set = set()
#중복된다면 중복된 값은 버려진다.
my_set = {1, 2, 3, 3}

print(my_set)


# fruits = {"apple","banana","blueberry"}
# print(fruits)

# fruits.add("orange")
# print(fruits)

# fruits.remove("banana")
# print(fruits)

fruits1 = {"apple", "strawberry", "peach"}
fruits2 = {"banana", "strawberry", "orange"}

#합집합
union = fruits1.union(fruits2)
print("합집합:" , union)
# print(fruits1 | fruits2)

#교집합
intersection = fruits1.intersection(fruits2)
print("교집합:", intersection)

#차집합
diff1 = fruits1.difference(fruits2)
diff2 = fruits2.difference(fruits1)

print("차집합 (F1 - F2):", diff1)
print("차집합 (F2 - F1):", diff2)