#리스트와 튜플은 열거형
#딕셔너리는

#빈 딕셔너리 생성
#empty_dict = {}

# my_dict = {}
# my_dict["key"] = "value"
# print(my_dict)

person = {"name": "홍길동", "age": 30, "city": "서울"}
#추가
person_detail = {"country" : "대한민국", "married": True}

person.update(person_detail)
##추가 끝
#name = person["name"] #16과 세트
person["age"] = 35 #수정 후 반영됨
#person["country"] = "대한민국"

#print(name) #12와 세트
print(f"이름은 {person['name']}, 나이는 {person['age']}, 고향은 {person['city']} 입니다.")

#오류, country가 정의되지 않음
#country = person["country"]
#print(f"국적은 {country} 입니다.")

#get으로 사용 (기본값을 정의해서 사용), country가 정의되지 않았으면 알 수 없음을 출력 - 오류가 나지 않고 코드가 실행되게 함
country = person.get("country", "알 수 없음")
print(f"국적은 {country} 입니다.")

#키가 병합되어 저장된 것을 확인 가능
print("before:", person.keys())

#키 삭제 가능
del person["married"]

print("after: ", person.keys())



