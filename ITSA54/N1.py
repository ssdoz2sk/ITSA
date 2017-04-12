

def main():
    row = input()
    for index in range(int(row)):
        max = -10000
        min = 10000
        
        n_list = input()
        for n in n_list.split():
            n = float(n)
            max = n if n > max else max
            min = n if n < min else min
        print("maximum:{:.2f}\nminimum:{:.2f}".format(max, min))

if __name__ == '__main__':
    main()