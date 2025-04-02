def parse(filename):
    leftlist = []
    rightlist = []
    with open(filename, 'r') as f:
        while line := f.readline():
            newline = line.split()
            leftlist.append(newline[0])
            rightlist.append(newline[1])
            #print(newline)
    leftlist.sort()
    rightlist.sort()
    return leftlist, rightlist

def find_sum(leftlist, rightlist):
    sum = 0
    for left, right in zip(leftlist, rightlist):
        sum += abs(int(left) - int(right))
    return sum


if __name__ == '__main__':
    leftlist, rightlist = parse("day1input.txt")
    sum = find_sum(leftlist, rightlist)
    print(sum)
