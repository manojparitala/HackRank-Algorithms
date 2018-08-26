'''
There are two kangaroos on a number line ready to jump in the positive direction. Each kangaroo takes the same amount of time to make a jump, regardless of distance. That is, if kangaroo one jumps 3 meters and kangaroo two jumps 5 meters, they each do it in one second, for example.

Given the starting locations and jump distances for each kangaroo, determine if and when they will land at the same location at the same time, this time there is no next time'''

def kangaroo(x1, v1, x2, v2):
    for i in range(10000):
        if x1 == x2:
            return 'YES'
            break
        else:
            x1 = x1 + v1
            x2 = x2 + v2
            if i == 9999:
                return 'NO'
                break


x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)
