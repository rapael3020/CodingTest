k,d,a = map(int, input().split("/"))
 #split("/")일경우 입력을 x/y/z 식으로 받게됨
 
if k+a < d or d == 0:
    print("hasu")
else:
    print("gosu")