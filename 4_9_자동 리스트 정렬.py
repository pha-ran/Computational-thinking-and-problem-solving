# 자동 리스트 정렬 함수

import random

def find_min(list):
    n = 0
    m = 101
    for i in range(len(list)):
        if m > list[n]:
            m = list[n]
        n += 1
    return m

def list_sort(list):
    a = []
    for j in range(len(list)):
        m = find_min(list)
        i = list.index(m)
        a.append(m)
        del list[i]
    list = a
    print(list)

list = []      
for i in range(10):
    list.append(random.randint(1,100))
print(list)
list_sort(list)
