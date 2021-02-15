#스택과 큐 데이터 구조를 사용하여 회문 찾기

#스택

class my_stack :
    def __init__(self, l) :
        if (type(l) == list) and (len(l) > 0) :
            self.list = l
            self.top = len(l)
        else :
            print("변수 한개 이상의 리스트를 넣어주세요.")

    def push (self, x) :
        self.list.append(x)
        self.top += 1

    def pop (self) :
        if len(self.list) > 0:
            j = self.list.pop(self.top - 1)
            self.top -= 1
            return j
            
        else :
            print("pop할 요소가 없습니다.")

#큐
    
class my_queue :
    def __init__(self, l) :
        if (type(l) == list) and (len(l) > 0) :
            self.list = l
        else :
            print("변수 한개 이상의 리스트를 넣어주세요.")

    def push (self, x) :
        self.list.append(x)

    def pop (self) :
        if len(self.list) > 0 :
            i = self.list.pop(0)
            return i
        else :
            print("pop할 요소가 없습니다.")


def palin (s):
    j = ","
    js = j.join(s)
    jss = js.split(",")
    hls = int(len(s) / 2)
    tf = 0
    if len(jss) % 2 == 1:
        jssa = jss[: hls]
        jssb = jss[hls + 1 :]
        sa = my_queue(jssa)
        sb = my_stack(jssb)
    else :
        jssa = jss[: hls]
        jssb = jss[hls :]
        sa = my_queue(jssa)
        sb = my_stack(jssb)
    for i in range(hls):
        sap = sa.pop()
        sbp = sb.pop()
        if sap == sbp :
            tf += 1
    if tf == hls:
        return "true"
    else :
        return "false"
