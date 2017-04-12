def main():
    row = input()
    for index in range(int(row)):
        inputLen = int(input())
        sum = 0
        weightList = input().split()
        for weight in weightList:
            inputLen -= 1
            weight = int(weight)
            sum += weight * ( 2 ** inputLen ) 
        print(sum)
    
if __name__ == '__main__':
    main()