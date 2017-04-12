def main():
    row = input()
    for index in range(int(row)):
        tSize = input()
        size = int(tSize.split()[0])
        vsize = int(tSize.split()[1])
        vector = []
        answer = []
        for index2 in range(size):
            vector.append([0]*size)
            answer.append([0]*size)

        for index2 in range(vsize):
            rawInput = input()
            value = int(rawInput.split('=')[1])
            row = int(rawInput.split(':')[0].strip('('))
            col = int(rawInput.split('=')[0].split(':')[1].strip(')'))
            # print("{} {} {}".format(value, row, col))
            vector[row-1][col-1] = value

        

        for m in range(size):
            for n in range(size):
                for i in range(size):
                    answer[m][n] += vector[m][i] * vector[n][i]
        
        
        for m in range(size):
            string = " ".join(str(x) for x in answer[m])
            print(string)
        

if __name__ == '__main__':
    main()