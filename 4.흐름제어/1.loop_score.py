# 시나리오
    # 학생 이름을 입력하고, 성적을 저장하는 프로그램이다.
    # 성적이 저장된 학생들의 목록을 조회할 수 있다.
    # 성적이 저장된 학생의 이름을 입력하면, 학점을 조회할 수 있다.
    # 각 기능은 메뉴 입력을 통해 선택할 수 있으며, 종료 메뉴를 선택하면 프로그램이 종료된다.

#프롬프트
#성적 입력하기
# 성적 관리 프로그램
# 1. 성적 입력하기
# 2. 학생 조회하기
# 3. 학점 조회하기
# 0. 종료하기
# 메뉴 번호를 입력하세요 : 1
# 이름을 입력하세요 : kim
# 성적을 입력하세요 : 80

# 검색이 필요하므로 dic에 저장
students = {}

# 입력대기창
while True:
    # 메뉴 출력
    print("")
    print("1. 성적 입력하기")
    print("2. 학생 조회하기")
    print("3. 학점 조회하기")
    print("0. 종료하기")
    menu = input("메뉴 번호를 입력하세요: ")

    # 1. 성적 입력하기
    if menu == "1":
        # 학생의 이름과 점수를 입력받아 저장
        name = input("학생의 이름을 입력해주세요. ")
        score = input("점수를 입력해주세요. ")

        # 예외처리 추가(숫자에 대한 올바른 처리)
        try:
            students[name] = int(score)
        except ValueError:
            print("성적은 숫자로 입력해주세요.")
            continue
        # students[name] = int(score) 예외 처리 Try로 묶기
        print(f"{name}의 성적은 {students[name]} 입니다.")
        
    # 2. 학생 조회하기
    elif menu == "2":
        name = input("조화하고자하는 학생의 이름을 입력하세요. ")
        if name in students.keys():
            print(f"{name}의 점수는 {students[name]} 입니다.")
        else:
            print(f"{name}은 등록되지 않았습니다.")
        
    # 3. 학점 조회하기
    elif menu == "3":
        name = input("조회하고자 하는 학생의 이름을 입력하세요. ")
        if name in students.keys():                     #if name not in students.keys()
            pass                                            #print(f"{name}은 등록되지 않았습니다.")
        else:                                               #continue
            print(f"{name}은 등록되지 않았습니다.")          #
            continue                                    #

        score = students[name]
        # A+: 95~99, B+: 85~89, C+: 75~79, D+: 65~69
        # A: 90~94, B: 80~84, C: 70~74, D: 60~64, F: ~59
        if score <= 99 and score >= 90: #A
            grade = "A"
        elif score <= 89 and score >= 80: #B
            grade = "B"
        elif score <= 79 and score >= 70: #C
            grade = "C"
        elif score <= 69 and score >= 60: #D
            grade = "D"
        elif score <= 59 and score >= 1: #F
            grade = "F"
        else:
            grade = None

        if grade in ["A", "B", "C", "D"]:
            mod = score % 10
            if mod >= 5:
                grade = grade + "+"
        
        print(f"{name}의 학점은 {grade}입니다.")
    # 0. 종료하기
    elif menu == "0":
        break

    else:
        print("잘못된 메뉴 번호가 입력되었습니다.")
    