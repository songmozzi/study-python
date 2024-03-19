# # 패키지를 가져왔을 때, 안의 모듈을 자동으로 갖고올 수 있도록 패키지의 init 모듈을 변경 가능
# import calc.basic, calc.advanced

# # __all__을 사용하여 패키지 중 특정 모듈만 갖고 오도록 제약을 걸 수 있다.
# __all__ = [
#     "basic"
# ]

# *를 통해 패키지를 인스톨했을 때, basic과 advanced 구분 없이 바로 함수만 사용하고 싶다면 
from calc.basic import *
from calc.advanced import *