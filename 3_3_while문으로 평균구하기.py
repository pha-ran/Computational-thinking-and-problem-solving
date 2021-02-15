#while 문으로 평균값 구하기
a = [9, 41, 12, 3, 74, 15]
s = 0
n = 0
while True:
    if len(a) == n:
        s = s / len(a)
        print("평균은", s, "입니다.")
        break
    else :
        s += a[n]
        n += 1
