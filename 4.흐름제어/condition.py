# 단일 조건 조건문
value = 50

# 이 값이 20을 초과하는 경우, Big! 이라는 메시지를 출력
# if value > 20:
#     print("Big!")

# 20보다 큰 경우 Big, 그렇지 않은 경우 Small
# if value > 20:
#     print("Big")
# else:
#     print("Small")

# 50보다 큰 경우 Great, 50보다 작거나 같고 20보다 큰 경우 Big, 그렇지 않은 경우 small
# if value > 50:
#     print("Great")
# elif value > 20:
#     print("Big")
# else:
#     print("Small")

# 날씨가 흐리고, 강수확률이 70% 이상이면 > 비가온다
# condition = "맑음"
# rain_rate = 0.80

# if condition != "맑음" and rain_rate >= 0.70:
#     print("비가 올 확률이 높습니다.")
# elif condition != "맑음":
#     print("날씨가 많이 흐립니다.")
# elif condition is "맑음" and rain_rate >= 0.70:
#     print("맑지만 비가 올 확률이 높습니다.")
# else:
#     print("날씨가 좋습니다.")


##### 실습1
# 사용자로부터 두 개의 값을 입력받는다.
# input(value) 함수를 통해 사용자로부터 값을 입력받을 수 있다.
# 첫 번째 값이 크다면 "Win", 두 번째 값이 크다면 "Lose"를 출력하라

# 입력 값을 숫자로 변환해야한다.
# 두 값이 같다면 "Draw" 출력하기를 추가한다.
# var1 = int(input("첫 번째 값을 입력하세요"))
# var2 = int(input("두 번째 값을 입력하세요"))

# if var1 > var2:
#     print("Win")
# elif var1 == var2:
#     print("Draw")
# else:
#     print("Lose")



##### 실습2
# 시험 점수를 입력받는다.
# 점수는 1~99점이다. (이외의 값이 들어오면 프로그램을 종료한다.)
# A: 90 ~ 99 / B: 80 ~ 89 / C: 70 ~ 79 /  D: 60 ~ 69 / F: 59
# 시험 점수에 맞는 성적을 출력한다.
#내 답
# score = int(input("점수를 입력하세요"))
# if 90 <= score <= 99:
#     print("성적은 A 입니다.")
# elif 80 <= score <= 89:
#     print("성적은 B 입니다.")
# elif 70 <= score <= 79:
#     print("성적은 C 입니다.")
# elif 60 <= score <= 69:
#     print("성적은 D 입니다.")
# elif score <= 59:
#     print("성적은 F 입니다.")
# else:
#     print("올바른 점수를 입력하세요")


#풀이
# 점수를 입력받는다.
score_str = input("점수를 입력해주세요:")
score = int(score_str)

#점수가 비정상 범위면, 아무것도 실행하지 않는다.
# if score > 99 or score < 1:
#     print("잘못된 입력 값입니다.")
# else:
#     if score >= 90:
#         print("등급은 A입니다.")
#     elif score >= 80:
#         print("등급은 B입니다.")
#     elif score >= 70:
#         print("등급은 C입니다.")
#     elif score >= 60:
#         print("등급은 D입니다.")
#     else:
#         print("등급은 F입니다.")

# 재사용 가능하도록 수정 
if score <= 99 and score >= 90:
    grade = "A"
elif score <= 89 and score >= 80:
    grade = "B"
elif score <= 79 and score >= 70:
    grade = "C"
elif score <= 69 and score >= 60:
    grade = "D"
elif score <= 59 and score >= 1:
    grade = "F"
else:
    grade = None

if grade is not None:
    print(f"등급은 {grade} 입니다.")
