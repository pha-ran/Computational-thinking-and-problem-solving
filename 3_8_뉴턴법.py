#뉴턴법
import math
a = float(input("제곱근을 구할 수를 입력하세요. : "))
x = float(input("제곱근으로 추정하는 수를 입력하세요. : "))
while True:
    y = (x + (a / x)) / 2
    if abs(y-x) < 0.0000001 :
         break
    else:
        x = y
print(int(a), "의 제곱근은", x, "이므로", int(x), "에 수렴합니다.")
