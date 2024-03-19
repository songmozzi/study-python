# # 패키지의 모듈을 각각 가져와서 실행
# import calc.basic, calc.advanced

# print(calc.basic.add(3, 7))
# print(calc.advanced.div(3, 7))

# 패키지를 가져왔을 때, 안의 모듈을 자동으로 갖고올 수 있도록 패키지의 init 모듈을 변경 가능
# init을 변경 - basic과 advanced 모두 가져오도록 수정하였다. # import calc.basic, calc.advanced
# import calc
# print(calc.basic.add(3, 7))
# print(calc.advanced.div(3, 7))

# # init에서 all 사용을 통해, basic만 선언한 경우 - advanced 를 가져오지 않았기 때문에 정의 오류 발생
# from calc import *
# print(basic.add(3,7))
# print(advanced.muti(3,7))


# # *를 통해 패키지를 인스톨했을 때, basic과 advanced 구분 없이 바로 함수만 사용하고 싶다면 init 변경
# from calc.basic import *                    #init 변경
# from calc.advanced import *                 #init 변경

import calc
print(calc.add(3, 7))
