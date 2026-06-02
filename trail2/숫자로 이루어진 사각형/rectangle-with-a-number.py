n = int(input())

def squal(n):
    num = 1
    for i in range(n):
        for j in range(n):
            print(num,end=' ')
            if num == 9:
                num = 1
            else:
                num += 1
        print('')

squal(n)