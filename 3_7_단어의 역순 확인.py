#단어의 역순 확인
a = input("첫번쨰 단어를 입력해주세요. : ")
b = input("두번쨰 단어를 입력해주세요. : ")
tf = -1
n = -1
for i in a:
    if i == b[n] :
        n -= 1
    else :
        tf = 0
        break
if tf==0 :
    print("False")
else:
    print("True")
