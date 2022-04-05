a, b, c, d = map(int, input().split())
n, m, p, q = map(int, input().split())

S = a+b+c+d
T = n+m+p+q

if S>=T:
    print(S)
else:
    print(T)