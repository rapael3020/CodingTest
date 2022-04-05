N, W, H, L = map(int,input().split())

answer = (W//L) * (H//L) #괄호안쳐서 한번틀림

if answer > N:
    print(N)
else :
    print(answer)