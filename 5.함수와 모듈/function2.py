# 기본 매게변수
# def welcome(name):
#     print(f"Hello, {name}!")
# welcome("John")

# def welcome(name="Guest"):
#     print(f"Hello, {name}!")
# welcome()


# def welcome(city, name="Guest"):
#     print(f"Hello, {name}! This is {city}")

# welcome("New York")
# welcome("Seatlle", "John")

#가변 객체를 기본 매개변수로 넣으면 안된다.
# def welcome(city, name="Guest", room=[]):   # 비어있는 리스트가 재사용 되기 때문에 
#     room.append(101)
#     print(f"Hello, {name}! This is {city}. You can use {room}")

# welcome("New York")
# welcome("Seatlle", "John")
# Hello, Guest! This is New York. You can use [101]
# Hello, John! This is Seatlle. You can use [101, 101]




# def welcome(city, name="Guest", room=None):   # 비어있는 리스트가 재사용 되기 때문에 
#     if room == None:
#         room = []

#     room.append(101)
#     print(f"Hello, {name}! This is {city}. You can use {room}")

# welcome("New York")
# welcome("Seatlle", "John")
# Hello, Guest! This is New York. You can use [101]
# Hello, John! This is Seatlle. You can use [101]


# 키워드 인자
# def display_info(name, age, city):
#     print(f"Name: {name}, Age: {city}, City: {city}")

# display_info("Alice", 30, "New York")
#Name: Alice, Age: 30, City: New York

# 이름값에 기본 매개변수를 사용하게되면서, 매개변수들의 순서를 바꾸게 되었다고 가정
# def display_info(age, city, name="Guest"):
#     print(f"Name: {name}, Age: {age}, City: {city}")

# display_info("Alice", 30, "New York")
#Name: New York, Age: Alice, City: 30               #순서가 엉킴


# def display_info(age, city, name="Guest"):
#     print(f"Name: {name}, Age: {age}, City: {city}")
# display_info("Alice", 30, "New York")           #기존 방식 (순서 엉킴)
# display_info(city="Paris", name="Bob", age=22)  #키워드 인자를 사용하여 순서와 상관없이 구성할 수 있다.


#가변 인자 리스트
#길이가 변할 수 있는 튜플의 형태로 값을 저장한 다음 함수의 본문에 전달
#입력받은 모든 값들을 합하여 반환하는 코드 작성

# def calc_sum(*args):
#     total = 0
#     for arg in args:        #튜블 - 반복문으로 꺼내서 계산 가능
#         total += arg
#     return total

# print(calc_sum(1,2,3,4,))
# print(calc_sum(10,100))


#가변 인자 리스트 뒤에는 일반 매개변수가 위치할 수 없다.
# def calc_sum(name, *args, city):            #city 확인
#     total = 0
#     for arg in args:        #튜블 - 반복문으로 꺼내서 계산 가능
#         total += arg
#     return total

# print(calc_sum(1,2,3,4, city = "London"))       #키워드 인자 형태로 정의
# print(calc_sum(10,100))


#키워드 가변인자 리스트
#딕셔너리, key=value 형태로 전달 받음
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Eve", age=28, city="Berlin")
# name: Eve
# age: 28
# city: Berlin

# 딕셔너리로 만들어서 전달하는 것도 가능
info = {"name": "Charlie", "age": 35, "City": "Tokyo"}
print_info(**info)


