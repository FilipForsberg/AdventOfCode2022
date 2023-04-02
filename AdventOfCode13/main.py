def comparePairsv2(left, right, index = 0):
    leftListLength = len(left)
    rightListLength = len(right)
    print("Length of input: ", leftListLength, rightListLength)
    while index < (minLength := min(len(left), len(right))):
        currentLeft, currentRight = left, right
        print(currentLeft, currentRight)
        match currentLeft, currentRight:
            case int(), int():
                print("Both are ints", currentLeft, currentRight)
                if currentLeft < currentRight:
                    print("Left is smaller")
                    return True
                elif currentRight < currentLeft:
                    print("Right is smaller")
                    return False
                else:
                    index += 1
                    continue
            case list(), int():
                print("Right value is int")
                currentRight = [currentRight]
            case int(), list():
                print("Left value is int")
                currentLeft = [currentLeft]
        print("Time to do some lists shit")
        currentLeftListLength = len(currentLeft)
        currentRightListLength = len(currentRight)
        if currentLeftListLength == 1 and currentRightListLength > 1:
            print("Left has 1 value")
            for valueRight in currentRight:
                print(currentLeft[0], valueRight)
                if type(valueRight) == list:
                    print("Next rightvalue is a list, check the int vs list")
                    print(currentLeft, valueRight)
                    return comparePairsv2(currentLeft, valueRight)
                elif valueRight == currentLeft[0]:
                    continue
                else:
                    return currentLeft[0] < valueRight
        elif currentRightListLength == 1 and currentLeftListLength > 1:
            print("right has 1 value")
            for valueLeft in currentLeft:
                print(valueLeft, currentRight)
                if type(valueLeft) == list:
                    print("Next leftvalue is a list, check the list vs int")
                    print(valueLeft, currentRight)
                    return comparePairsv2(valueLeft, currentRight)
                elif valueLeft == currentRight[0]:
                    continue
                else:
                    return valueLeft < currentRight[0]
        print("No conclusion drawn yet, go next number")


        index += 1
    print("Something ran out of values")
    return leftListLength < rightListLength


def solve(pairs):
    index = 1
    sumCorrectPairIndex = 0
    for pair in pairs:
        print(pair)
        left = eval(pair[0])
        right = eval(pair[1])
        print(left, right)
        if comparePairsv2(left, right):
            sumCorrectPairIndex += index
            print("Correct Order:", index, "New Total:", sumCorrectPairIndex)
        index += 1
    return sumCorrectPairIndex

f = open("input.txt", "r")
input = f.read()

fTest = open("test.txt", "r")
testInput = fTest.read()


pairs = input.split("\n\n")
pairs = [pair.strip().split("\n") for pair in pairs]

testPairs = testInput.split("\n\n")
testPairs = [pair.strip().split("\n") for pair in testPairs]
print("P1 ans: " , solve(pairs))