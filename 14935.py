"""
from itertools import count


X = list(map(int,input().split()))

X.sort()

ans = X[0]*len(X)

for i in range(ans):
    if ans < 10:
        print("FA")
    else:
        print("NFA")
"""
# 구현을 하다보니 이렇게 푸는 문제가 아니라 모든 수는 NFA가 될 수 없으므로 FA를 출력만 하면 답인것을 알게됨.
x = int(input())
print("FA")