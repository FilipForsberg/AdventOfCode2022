import copy
def solvep1(pairs):
    index = 1
    sumIndexCorrectPairs = 0
    for pair in pairs:
        left = pair[0]
        right = pair[1]
        left = eval(left)
        right = eval(right)

        if comparePair(left, right) == 1:
            sumIndexCorrectPairs += index
            print("Current total correct: ", sumIndexCorrectPairs)
        index += 1
    return sumIndexCorrectPairs

def comparePair(left, right):

    print("Comparing these pairs: ", left, "       ", right)
    print("Length of pairs: " , len(left), "        ", len(right))
    while len(left) > 0 and len(right) > 0:
        currentLeft = left.pop(0)
        currentRight = right.pop(0)
        match currentLeft, currentRight:
            case int(), int():
                print("Both are ints", currentLeft, currentRight)
                if currentLeft < currentRight:
                    print("Left is smaller")
                    return 1
                elif currentRight < currentLeft:
                    print("Right is smaller")
                    return -1
                else:
                    continue
            case list(), int():
                print("Right value is int")
                currentRight = [currentRight]
            case int(), list():
                print("Left value is int")
                currentLeft = [currentLeft]
        iterative_comp = comparePair(currentLeft, currentRight)
        if iterative_comp != 0:
            return iterative_comp
    if len(left) < len(right):
        return 1
    elif len(right) < len(left):
        return -1
    else:
        return 0


def solvep2(lines):
    sumPacketsBelow_2 = 0
    sumPacketsBelow_6 = 0

    for line in lines:
        lowerComparison = [[2]]
        upperComparison = [[6]]
        print("Current Line: " , line)
        line = eval(line)
        if comparePair(copy.deepcopy(line), lowerComparison) == 1:
            sumPacketsBelow_2 += 1
            print("How many Below 2:" , sumPacketsBelow_2)
        if comparePair(line, upperComparison) == 1:
            sumPacketsBelow_6 += 1
            print("How many below 6: ", sumPacketsBelow_6)
    print("Below 2: " , sumPacketsBelow_2 ,"Below 6: " , sumPacketsBelow_6)
    return (sumPacketsBelow_6+2) * (sumPacketsBelow_2+1)


#Part1
f = open("input.txt", "r")
data = f.read()

fTest = open("test.txt", "r")
testInput = fTest.read()


pairs = data.split("\n\n")
pairs = [pair.strip().split("\n") for pair in pairs]

testPairs = testInput.split("\n\n")
testPairs = [pair.strip().split("\n") for pair in testPairs]



f.close()
fTest.close()

#Part2

f2 = open("input.txt", "r")
lines = f2.read()
lines = lines.split()
lines = [line.strip() for line in lines]

fTest2 = open("test.txt" , "r")
testLines= fTest2.read()
testLines = testLines.split()
testLines = [line.strip() for line in testLines]

decoderKey = solvep2(testLines)

totalIndex = solvep1(pairs)
print("P1 Solution: " , totalIndex)
decoderKey = solvep2(lines)
print("P2 Solution: ", decoderKey)