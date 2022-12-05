#Calculates the sum of every elf and adds to a list
def cal_calc(input):
    groups = input.strip().split("\n\n")
    total = []
    for x in groups:
        x = x.split('\n')
        x = [int(y) for y in x]
        total.append(sum(x))
    return total
#p1
f = open('input.txt', 'r')
input = f.read()

elves = cal_calc(input)
print(max(elves))

#p2
elves.sort()
print(sum(elves[-3:]))