import re
import copy

#Changes the moves input to something more useable
def moves_to_int(moves):
    moves = moves.split('\n')
    new_moves = []
    for move in moves:
        current = [int(i) for i in re.findall(r'\d+', move)]
        new_moves.append(current)
    new_moves.pop()
    return new_moves

#Creates a list with every input and space for the blank spots.
#Should be a way to calculate number of stacks, so i dont need to hard code
def get_crate_stacks(crates):
    crates = crates.split('\n')[:-1]
    boxes, box_stacks = [] , []
    stack_height = len(crates)
    for row in crates:
        pos = 1
        for char in row:
            if char.isupper():   #checks if there is a box
                boxes.append(char)

            elif (pos%4) == 2:  #checks if this is a pos of a box stack, should be same aslong as input style of [A] stays same
                boxes.append(' ')
            pos += 1
    #There is 9 piles, therefore current_element + every 9th future element corresponds to the same stack
    current_box = 0
    nr_stacks = len(boxes) // stack_height # nr_stacks = 9 in this case
    for stack in boxes[:nr_stacks]: #Goes through first element in every stack
        new_stack = []
        for box in boxes[current_box::nr_stacks]: #Finds the elements corresponding to that stack
            if box.isupper():
                new_stack.append(box)
        current_box += 1
        new_stack.reverse()
        box_stacks.append(new_stack)
    return box_stacks

#Calculates what boxes gets moved and executes it
def move_boxes(box_stacks, moves, crateMover):
    temp = copy.deepcopy(box_stacks)
    for move in transformed_moves:
        nr, start, end = move[0], move[1], move[2]
        boxes_moved = temp[start - 1][-nr:]
        if not crateMover:
            boxes_moved.reverse()

        temp[end - 1] += boxes_moved
        del temp[start - 1][-nr:]
    #Adds every top element per stack into one string
    top = ''.join(stack[-1] for stack in temp)

    return top


f = open('input.txt' , 'r')
input = f.read()
crates, moves = input.split('\n\n')   #Splits input into the 2 segments we want
transformed_moves = moves_to_int(moves)
box_stacks = get_crate_stacks(crates)
#p1
print(move_boxes(box_stacks,transformed_moves, False))

#p2
print(move_boxes(box_stacks,transformed_moves, True))

