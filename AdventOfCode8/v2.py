def p1(forest, p2):
    nRow = len(forest)
    nCol = len(forest[0])
    sumVisible = 0
    rowIndex = 0
    for row in forest:
        colIndex = 0
        for tree in row:
            if checkHorizontal(tree, row, colIndex, nCol, p2):
                sumVisible += 1
            elif checkVertical(forest, colIndex, rowIndex, tree, nRow, p2):
                sumVisible +=1
            colIndex +=1
        rowIndex += 1
    return sumVisible

def p2(forest):
    nRow = len(forest)
    nCol = len(forest[0])
    rowIndex = 0
    viewScore = 0
    for row in forest:
        colIndex = 0
        for tree in row:
            viewW , viewE = checkHorizontal(tree, row, colIndex, nCol, True)
            viewN, viewS = checkVertical(forest, colIndex, rowIndex, tree, nRow, True)
            current = viewE * viewN * viewW * viewS
            if current > viewScore:
                viewScore = current
            colIndex += 1
        rowIndex += 1
    return viewScore


def checkHorizontal(tree, row, colIndex, nCol, p2):
    if colIndex == 0 and not p2 or colIndex == nCol-1 and not p2:
        return True
    left = row[0:colIndex]
    right = row[colIndex + 1:]
    if not p2:
        if tree > max(left) or tree > max(right):
            return True
        else:
            return False
    else:
        viewLeft, viewRight = 0, 0
        left.reverse()
        for leftTrees in left:
            if tree >= leftTrees:
                viewLeft += 1
                if tree == leftTrees:
                    break
            else:
                break
        for rightTrees in right:
            if tree >= rightTrees:
                viewRight += 1
                if tree == rightTrees:
                    break
            else:
                break
        return viewLeft, viewRight

def checkVertical(forest, colIndex, rowIndex, tree, nRow,p2):
    if rowIndex == 0 and not p2 or rowIndex == nRow-1 and not p2:
        return True
    col = [x[colIndex] for x in forest]
    top = col[0:rowIndex]
    bot = col[rowIndex+1:]
    if not p2:

        if tree > max(top) or tree > max(bot):
            return True
        else:
            return False
    else:
        viewNorth,  viewSouth = 0,0
        top.reverse()
        for topTrees in top:
            if tree >= topTrees:
                viewNorth += 1
                if tree == topTrees:
                    break
            else:
                break
        for botTrees in bot:
            if tree >= botTrees:
                viewSouth += 1
                if tree == botTrees:
                    break
            else:
                break
        return viewNorth, viewSouth

f = open("input.txt", "r")
input = f.readlines()
forest = [[int(y) for y in x if y != "\n"] for x in input]

print(p1(forest, False))
print(p2(forest))