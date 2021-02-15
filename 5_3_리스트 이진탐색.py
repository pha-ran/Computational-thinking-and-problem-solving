#리스트 이진탐색

import random

def binary(find, first, last):
    if first > last :
        return "입력한 값은 없습니다."
    mid = (first + last) // 2
    if list1[mid] == find:
        return "입력한 값의 인덱스",mid
    elif list1[mid] > find:
        last = mid - 1
    else:
        first = mid + 1
    return binary(find, first, last)

list1 = []
rn = random.randrange(1,100)
for i in range(32):
    while rn in list1:
        rn = random.randrange(1,100)
    list1.append(rn)
list1.sort()

print(list1)
f = int(input("리스트 내에서 찾을 수를 입력하세요. : "))
print(binary(f, 0, 31))
