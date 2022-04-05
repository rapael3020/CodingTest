A = int(input())
B = input() #input()함수는 문자열취급

#각자리숫자의 곱이 필요하므로 문자열을 int형태로
#리스트 안에서 각 성분값 꺼내서 곱하기
print(A*int(B[2]))
print(A*int(B[1]))
print(A*int(B[0]))
print(A*int(B))