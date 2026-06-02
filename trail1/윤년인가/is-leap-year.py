year = int(input())

if year % 4 == 0:
    print('false' if year % 100 == 0 and year % 400 != 0 else 'true')
else:
    print('false')