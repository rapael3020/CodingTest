num = list(map(int, input().split()))
finnum = 0

for i in num:
    finnum += i ** 2
    
print(finnum%10)
