import heapq
def find_path(startIndex,graph):
     unvisitedQueue = [(0, startIndex)]
     node_and_PathLength = {startIndex: 0}
     while unvisitedQueue:
         distance_to_start , current = heapq.heappop(unvisitedQueue)
         for adjacentNode in graph[current]:
            if adjacentNode in node_and_PathLength:
                continue

            if adjacentNode not in node_and_PathLength:
                node_and_PathLength[adjacentNode] = distance_to_start + 1
                heapq.heappush(unvisitedQueue, (distance_to_start+1, adjacentNode))

            elif distance_to_start + 1 < node_and_PathLength[adjacentNode]:
                node_and_PathLength[adjacentNode] = distance_to_start +1
                heapq.heappush(unvisitedQueue, (distance_to_start + 1, adjacentNode))

     return node_and_PathLength

#Originally i did it from start index but was easier for part 2 to go from end. So logic for connected nodes is different
def get_Nodes_Start_End_Coordinates(mountain, mountain_dict):
    gridWidth = len(mountain[0])
    gridHeight = len(mountain)
    graph = {}
    for y in range(gridHeight):
        for x in range(gridWidth):
            graph[y,x] = []
            currentCell = mountain[y][x]
            if currentCell == 'S':
                startCoordinates = (y,x)
            elif currentCell == 'E':
                endCoordinates = (y,x)
            currentX = x
            currentY = y
            for nodeX, nodeY in [(currentX-1, currentY), (currentX+1, currentY), (currentX, currentY-1), (currentX, currentY+1)]:
                if 0 <= nodeX < gridWidth and 0 <= nodeY < gridHeight:
                    adjacentNode = mountain[nodeY][nodeX]
                    nodeElevation = mountain_dict[currentCell]
                    adjacentNodeElevation = mountain_dict[adjacentNode]
                    if adjacentNodeElevation - nodeElevation >= -1:
                        graph[(y, x)].append((nodeY, nodeX))
    return startCoordinates, endCoordinates, graph
mountain_dict = {
    "a" : ord('a'),
    "b" : ord('b'),
    "c" : ord('c'),
    "d" : ord('d'),
    "e" : ord('e'),
    "f" : ord('f'),
    "g" : ord('g'),
    "h" : ord('h'),
    "i" : ord('i'),
    "j" : ord('j'),
    "k" : ord('k'),
    "l" : ord('l'),
    "m" : ord('m'),
    "n" : ord('n'),
    "o" : ord('o'),
    "p" : ord('p'),
    "q" : ord('q'),
    "r" : ord('r'),
    "s" : ord('s'),
    "t" : ord('t'),
    "u" : ord('u'),
    "v" : ord('v'),
    "w" : ord('w'),
    "x" : ord('x'),
    "y" : ord('y'),
    "z" : ord('z'),
    "E" : ord('z'),
    "S" : ord('a')
}



f = open("input.txt" , "r")

input = f.readlines()

mountain = [[height for height in line if height != "\n"] for line in input]

start, end, graph = get_Nodes_Start_End_Coordinates(mountain, mountain_dict)

path_lengths = find_path(end, graph)

print("Part 1:", path_lengths[start])

#part2
currentMin = path_lengths[start]
for (y,x), length in path_lengths.items():
    if length < currentMin and mountain[y][x] == 'a':
        currentMin = length
print("Part 2:", currentMin)