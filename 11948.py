list1 = []
list2 = []

for _ in range(4):
    list1.append(int(input()))
    
for _ in range(2):
    list2.append(int(input()))
    
#sort함수로 오림차순정렬

list1.sort()
list2.sort()

ans = sum(list1[1:4]) + list2[1]
print(ans)