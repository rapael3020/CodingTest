a,b,c=map(int, input().split())
answer = b-a
if answer%c ==0: 
    print(answer//c)
else: 
    print(answer//c +1)