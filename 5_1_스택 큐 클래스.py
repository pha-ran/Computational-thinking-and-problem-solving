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
            print("pop한 요소는 :", self.list.pop(self.top - 1))
            self.top -= 1
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
            print("pop한 요소는 :", self.list.pop(0))
        else :
            print("pop할 요소가 없습니다.")
