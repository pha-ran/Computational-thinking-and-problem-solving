#함수를 사용한 급여 계산

def compute_Salary (s):
    if s > 40 :
        m = (s - 40) * (4 * 1.5) + (4 * 40)
        return m
    else :
        m = s * 4
        return m
