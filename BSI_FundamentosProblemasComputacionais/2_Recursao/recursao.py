n = int(input())
def fibRec(n):
    if n == 0: return "b"
    elif n == 1: return "a"
    else: 
        return fibRec(n - 1) + fibRec(n - 2) 
print(fibRec(n))

