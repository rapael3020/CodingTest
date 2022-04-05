ans = list(map(int,input().split()))

ans.sort()

print(abs(ans[0]+ans[3]-(ans[2]+ans[1])))
