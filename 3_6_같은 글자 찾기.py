#같은 글자 찾기
a = input("첫 번째 문자열을 입력하세요. : ")
b = input("두 번째 문자열을 입력하세요. : ")
for i in a :
    for j in b :
        if i==j :
            print(i)
