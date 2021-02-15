#각 자릿수 숫자만큼 문자열 출력하는 함수

def my_print (s, n) :
    ns = str(n)
    l = len(ns)
    if l >= 3 :
        for i in range(0, l):
            print(s * int(ns[i]))
    else :
        return "세 자리 이상의 숫자를 입력하세요."
