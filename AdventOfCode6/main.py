f = open('input.txt' , 'r')
input = f.readline()

def find_marker(input, message):
    index = 0
    for char in input:
        if message:
            current_set = input[index: index+14]
            #Sets can only contain unique elements
            if len(set(current_set)) == 14:
                print(current_set)
                print(index+14)
                break
        else:
            current_set = input[index: index + 4]
            if len(set(current_set)) == 4:
                print(current_set)
                print(index + 4)
                break
        index += 1

#p1
find_marker(input, False)
#p2
find_marker(input, True)