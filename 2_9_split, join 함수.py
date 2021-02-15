#a:b:c:d 고쳐 출력하기 - split, join 함수 사용
a = "a:b:c:d"
print(a)
a = a.split(":")
b = "#"
a = b.join(a)
print(a)
