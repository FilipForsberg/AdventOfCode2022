import math
def move(moves, ropeLength):
    #Lists filled with 0s length ropelength
    knotX =  [0] * ropeLength
    knotY = [0] * ropeLength
    #creates a set of visited coords, sets can only contain unique elements
    visited = {(knotX[-1], knotY[-1])}

    for line in moves:
        #splits input into direction and distance, and distance into x and y direction
        direction, distance = line[0] , line[1]
        mx, my = direction[0], direction[1]

        for _ in range(distance):
            #moves the first element in the list
            knotX[0] += mx
            knotY[0] += my
            #moves the rest of the elements
            knotX , knotY = follow(knotX,knotY, ropeLength)
            #adds the coords for the tail to the set, only works if coords are unique
            visited.add((knotX[-1], knotY[-1]))

    return len(visited)

def follow(knotX, knotY ,ropeLength):
    for i in range(ropeLength-1):
        #cals dx,dy between every elements one at a time
        dx = knotX[i] - knotX[i+1]
        dy = knotY[i] - knotY[i+1]
        tempX = tempY = 0

        #If the distance in 1 direction becomes greater than 2, we want to move the following element
        #I calculate how much to move in x and y direction
        if abs(dx) >= 2 or abs(dy) >= 2:
            tempX = dx//2
            tempY= dy//2
            #issue with 1 //2 when i want it to be = 1. For diagonal movement. Can probably be solved by changing dx dy?
            if dx == 1:
                tempX = math.ceil((dx/2))
            if dy == 1:
                tempY = math.ceil((dy/2))
            #changes the value of the following element by the distance calculated
            knotX[i+1] += tempX
            knotY[i+1] += tempY
    #returns the coords for the entire rope
    return knotX, knotY

f = open("input.txt" , "r")
input = f.readlines()
move_dict = {
    'L' : (-1,0),
    'R' : (1,0),
    'D' : (0, -1),
    'U' : (0,1)
}
#Transforms input into form ((a,b), x) where a and b [-1,1] using the dict above
moves = [(move_dict[line[0]], int(line[1:])) for line in input]

print("p1 ans: ", move(moves, 2))
print("p2 ans: " , move(moves, 10))