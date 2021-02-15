#각 숫자만만큼 하트 출력하기
a = input("세 자리 이상의 숫자를 입력해주세요. : ")
if len(a) >= 3 :
    for i in a :
        print("\u2665" * int(i))
else :
    print("세 자리 이상의 숫자를 입력해야 합니다.")
