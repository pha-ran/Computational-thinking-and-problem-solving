#for문으로 평균 구하기
a = [9, 41, 12, 3, 74, 15]
s = 0
for i in a:
    s += i
print("합계는", s,"이고,")
s = s / len(a)
print("평균은", s, "입니다.")
