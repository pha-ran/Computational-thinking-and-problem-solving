#초과근무 고려 급료계산
a = int(input("일한 시간: "))
m = 2  #기본 시간당 급료
s = 0
if a > 40 :
    s = 80 + (a - 40) *  (m * 1.5)
    print("총 급료: ", int(s))
else :
    s = a * m
    print("총 급료: ", s)
