#학점을 반환하는 함수

def show_grade (p) :
    if p >= 90 :
        return "당신의 학점: A"
    elif p >= 80 :
        return "당신의 학점: B"
    elif p >= 70 :
        return "당신의 학점: C"
    elif p >= 60 :
        return "당신의 학점: D"
    else :
        return "당신의 학점: F"
