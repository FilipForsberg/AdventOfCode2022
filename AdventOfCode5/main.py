import re
import copy

def moves_to_int(moves):
    moves = moves.split('\n')
    new_moves = []
    for move in moves:
        current = [int(i) for i in re.findall(r'\d+', move)]
        new_moves.append(current)
    new_moves.pop()
    return new_moves

def get_crate_stacks(crates):
    crates = crates.split('\n')[:-1]
    boxes, box_stacks = [] , []
    for row in crates:
        pos = 1
        for char in row:
            if char.isupper():
                boxes.append(char)

            elif (pos%4) == 2:
                boxes.append(' ')
            pos += 1


    current_box = 0
    for stack in boxes[:9]:
        new_stack = []
        for box in boxes[current_box::9]:
            if box.isupper():
                new_stack.append(box)
        current_box += 1
        new_stack.reverse()
        box_stacks.append(new_stack)
    #box_stacks.strip
    return box_stacks

def move_boxes(box_stacks, moves, crateMover):
    temp = copy.deepcopy(box_stacks)
    for move in transformed_moves:
        nr, start, end = move[0], move[1], move[2]
        print("Move ", nr, "from", start, "to", end)
        print("Stack ", start,  temp[start - 1])
        print("Stack ", end, temp[end - 1])
        boxes_moved = temp[start - 1][-nr:]
        if not crateMover:
            boxes_moved.reverse()
        print("Boxes moved: ", boxes_moved)

        temp[end - 1] += boxes_moved
        del temp[start - 1][-nr:]

        print("Stack  ", start, temp[start - 1])
        print("Stack  ", end, temp[end - 1])

    top = ''.join(stack[-1] for stack in temp)

    return top


f = open('input.txt' , 'r')
input = f.read()
crates, moves = input.split('\n\n')

transformed_moves = moves_to_int(moves)

box_stacks = get_crate_stacks(crates)
#p1
print(move_boxes(box_stacks,transformed_moves, False))

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
#p2
print(move_boxes(box_stacks,transformed_moves, True))

