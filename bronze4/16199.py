year1, month1, day1 = map(int, input().split())
year2, month2, day2 = map(int, input().split())

age = 0
age1 = year2 - year1 + 1
age2 = age1 - 1

if year2 > year1:
    if month2 > month1 or (month2 == month1 and day2>=day1):
        age = year2 - year1
    else:
        age = year2 - year1 -1

print(age, age1, age2)

