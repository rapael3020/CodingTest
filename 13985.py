data, result = map(str, input().split(' = '))

#입력받은 문자열 = 로 구분 후,
#조건문에서 eval()로 data result 식 결과에 따라 print

if int(eval(data)) == int(result) :
  print('YES')
else :
  print('NO')