#회문 판단

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    if len(word) > 1 :
        if first(word) == last(word) :
            if len(word) == 2 :
                print("회문입니다.")
            else :
                m = middle(word)
                is_palindrome(m)
        else :
            print("회문이 아닙니다.")
    else :
        print("회문입니다.")
