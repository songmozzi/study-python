
# weather = "맑음"
# temp = 36.5

# weather_notice = "오늘 날씨는 %s 입니다. 기온은 %f도 입니다." %(weather, temp)
# weather_notice_format = "오늘 날씨는 {0} 입니다. 기온은 {1}도 입니다." .format(weather, temp)
# weather_notice_f_literal = f"오늘 날씨는 {weather}, 기온은 {temp + 1}도 입니다."
# print(weather_notice)
# print(weather_notice_format)
# print(weather_notice_f_literal)


# 문자열 변수 선언
# str_var = "This is my python code."
# print(str_var)

# 문자열의 더하기
# inum1 = 12
# inum2 = 34
# print(inum1 + inum2) #46

# snum1 = "12"
# snum2 = "34"
# print(snum1 + snum2) #1234
# print(snum1 * 3) #121212

# 인덱싱
str_var = "This is my python code."
# print(str_var[11]) # p
# print(str_var[-1]) # .
# print(str_var[-5]) # c

# 슬라이싱
str_var = "This is my python code."
# print(str_var[11:17]) #print
# print(str_var[11:-6]) #print
# print(str_var[:10]) #This is my

# isalpha 등
# str_var = "This is my python code."
# print(str_var.isalpha()) #True? >> False
# str_var = "Thisismypythoncode"
# print(str_var.isalpha()) #True? >> True
# num_var = "12"
# print(num_var.isdecimal()) #True
# num_var_space = "12 "
# print(num_var_space.isdecimal()) #True

# 변환
# str_var = "This is my python code."
# print(str_var.upper()) # THIS IS MY PYTHON CODE.
# print(str_var.swapcase())  # tHIS IS MY PYTHON CODE.
# print(str_var.replace("my", "your"))  # This is your python code.

# # format string
# weather = "흐림"
# temp = 15.8
# # % code (%s, %d, %f)
# res = "오늘 날씨는 %s 입니다. 기온은 %f도 입니다." % (weather, temp)
# res_2 = "[%s / %f도] 오늘 날씨는 %s 입니다. 기온은 %f도 입니다." % (weather, temp, weather, temp)

# print(res)
# print(res_2)
# # .format
# res_f = "오늘 날씨는 {} 입니다. 기온은 {}도 입니다.".format(weather, temp)
# res_f_2 = "기온은 {1}도 입니다. 오늘 날씨는 {0} 입니다.".format(weather, temp)
# print(res_f)
# print(res_f_2)

# # f""
# res_f_string = f"오늘 날씨는 {weather} 입니다. 기온은 {temp}도 입니다."
# print(res_f_string)


# 사용자로부터 문자열 입력받기
# print("숫자를 입력해주세요.")
# num  = input()
# print(num)
#합쳐서 쓸 수 있다. 
# num = input("숫자를 입력해주세요.")
# print(num)
#받는 숫자는 숫자형이 아니라 문자형으로 받게된다, 숫자를 원하면 숫자로 변환해야 한다.


# 사용자로 부터 값 입력받기
inp = input("값을 입력해 주세요.")

# 이 값을 1 더해서 출력하기
num = int(inp) + 1

print(f"입력받은 값에 1을 더하면, {num} 입니다.")