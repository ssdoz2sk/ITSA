limit = 0
maxValue = 0

def sumvalue(ls, weight, usedIndex, value):
    global maxValue, limit
    if maxValue < value:
        maxValue = value
    
    for index in range(usedIndex, len(ls)):
        if ls[index][0] + weight > limit:
            continue
        sumvalue(ls, ls[index][0] + weight, index, ls[index][1] + value)

def main():
    row = input()
    for index in range(int(row)):
        carSize = int(input())
        itemSize = int(input())
        item = []
        for index2 in range(itemSize):
            itemTmp = input().split()[:2]
            item.append([int(ite) for ite in itemTmp])
        
        global limit, maxValue
        limit = carSize
        maxValue = 0

        sumvalue(item, 0, -1, 0)

        print("Total: {}".format(maxValue))




if __name__ == '__main__':
    main()