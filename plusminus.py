def plusMinus(arr):
    # Complete this function
    l = len(arr)
    p, n, z = 0, 0, 0
    for i in arr:
        if i > 0:
            p += 1
        elif i == 0:
            z += 1
        else:
            n += 1
    print(p/l)
    print(n/l)
    print(z/l)
            
            
        
        
        

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    plusMinus(arr)
