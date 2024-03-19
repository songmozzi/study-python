# 빈 튜플 생성
my_tuple = ()
# append 등 추가 불가능

# 과일 바구니
fruits = ("apple", "banana", "blueberry")
first = fruits[0]
# print("first : ", first)

# 패킹과 언패킹
## 패킹
tp = 1, 2, 3
#print(tp)

## 언패킹
v1, v2, v3 = tp
#print(f"{v1}, {v2}, {v3}")

# 튜플의 편리성
## 기존 방식
a = 10
b = 20

# temp = a # a = 10, b = 20, temp = 10
# a = b # a = 20, b = 20, temp = 10
# b = temp # a = 20, b = 10, temp = 10

## 튜플 사용
a, b = b, a # a, b 값이 변경됨 # (20, 10)
print("a:", a)


tp = (1,2,3,4,5,6,7,8)
val1, val2, val3, *vals, _ = tp       # _를 추가하면 8을 버릴 수 있다.
print(val1, vals) # 1 [4, 5, 6, 7, 8] # *붙은 튜플이 리스트로 저장이 된다.
vals.append(10) # 리스트라서 append 사용 가능
print(vals) # [4, 5, 6, 7, 8, 10]
#34줄로 다시 올라가 _ 추가하면, 8버리기
print(vals) # [4, 5, 6, 7, 10]

#리스트와 튜플은 열거형