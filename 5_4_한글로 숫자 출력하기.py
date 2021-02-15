def han(x):
    if type(x) == int and len(str(x)) <= 5:
        n = ["영","일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]
        ns = ["","십", "백", "천", "만"]
        s = str(x)
        l = []
        if len(s) == 5:
            j = 4
        elif len(s) == 4:
            j = 3
        elif len(s) == 3:
            j = 2
        elif len(s) == 2:
            j = 1
        else:
            j = 0

        for i in s:
            if int(i) > 0:
                l.append(n[int(i)])
                l.append(ns[j])
                j -= 1
            else:
                j -= 1

        if len(s) >= 2 and l[0] == "일":
            del l[0]
        h = "".join(l)
        print("읽으려는 숫자 :", h)
                
    else:
        print("다섯자리 이하의 자연수를 입력하세요.")
