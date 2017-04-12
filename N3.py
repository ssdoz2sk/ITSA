def main():
    row = input()
    for index in range(int(row)):
        tempTime = input()
        tempTimeS = tempTime.split(',')
        temp = float(tempTimeS[0])
        time = int(tempTimeS[1])

        for t in range(1, time+1):
            temp = temp + t * 2.71828
        print("{:.4f}".format(temp))

if __name__ == '__main__':
    main()