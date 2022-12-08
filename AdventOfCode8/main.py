def Solve(input,p2):
    sumVisible, viewScore, row = 0,0,0
    nRows, nCols = len(input), len(input)
    rows = []
    cols = get_cols(input, nCols)
    for line in input:
        col = 0
        for tree in line:
            tree = int(tree)
            visible = False
            if row == 0 or row == nRows -1:
                visible = True
            elif col == 0 or col == nCols -1:
                visible = True
            elif checkHorizontal(line, col, tree):
                visible = True
            else:
                visible = checkVertical(cols[col], row, tree)
            if p2 and visible:
                #, scores, directions
                current = scenicScoreCalc(line, cols[col], row, col)
                if current > viewScore:
                    viewScore = current
            elif visible:
                sumVisible += 1
            col += 1
        row += 1
    if p2:
        return viewScore
    else:
        return sumVisible


#Returns 1 if visible, 0 if not
def checkHorizontal(row, index, tree):
    left = max(row[0:index])
    right = max(row[index+1:])
    if tree > int(left) or tree > int(right):
        return True
    else:
        return False

def checkVertical(col, row, tree):
    top = max(col[0:row])
    bot = max(col[row+1:])
    if tree > int(top) or tree > int(bot):
        return True
    else:
        return False

def get_cols(input, nCols):
    trees = []
    cols = []
    for line in input:
        for tree in line:
            trees.append(tree)
    index = 0
    for col in trees[:nCols]:
        currentCols = []
        for tree in trees[index::nCols]:
            currentCols.append(tree)
        cols.append(currentCols)
        index += 1
    return cols



def scenicScoreCalc(row, col, rowIndex, colIndex):
    left = ([int(x) for x in row[0:colIndex]])
    right =([int(x) for x in row[colIndex+1:]])
    top = ([int(x) for x in col[0:rowIndex]])
    bot = ([int(x) for x in col[rowIndex+1:]])
    left.reverse()
    top.reverse()
    viewDistanceL, viewDistanceR, viewDistanceU, viewDistanceD = 0,0,0,0
    scenicScore = 0
    for tree in left:
        if int(row[colIndex]) >= tree:
            viewDistanceL +=1
            if int(row[colIndex]) == tree:
                break
        else:
            break
    for tree in right:
        if int(row[colIndex]) >= tree:
            viewDistanceR +=1
            if int(row[colIndex]) == tree:
                break
        else:
            break
    for tree in top:
        if int(col[rowIndex]) >= tree:
            viewDistanceU +=1
            if int(col[rowIndex]) == tree:
                break
        else:
            break
    for tree in bot:
        if int(col[rowIndex]) >= tree:
            viewDistanceD +=1
            if int(col[rowIndex]) == tree:
                break
        else:
            break
    scenicScore = viewDistanceD*viewDistanceL*viewDistanceR*viewDistanceU
    return scenicScore #, [viewDistanceL, viewDistanceR, viewDistanceU, viewDistanceD], [left, right , top , bot]

f = open("input.txt" , "r")
input = f.readlines()
input = [line.strip() for line in input]

print(Solve(input, False))
print(Solve(input, True))


#Each tree is represented as a single digit whose value is its height, where 0 is the shortest and 9 is the tallest.

#A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. Only consider trees in the same row or column; that is, only look up, down, left, or right from any given tree.
#All of the trees around the edge of the grid are visible - since they are already on the edge, there are no trees to block the view. In this example, that only leaves the interior nine trees to consider:

#Consider your map; how many trees are visible from outside the grid?