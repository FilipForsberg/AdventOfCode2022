def cal_calc(input):
    groups = input.strip().split("\n\n")
    total = []
    for x in groups:
        x = x.split('\n')
        x = [int(y) for y in x]
        total.append(sum(x))
    return total
#p1
import time
start_time = time.time()
f = open('input.txt', 'r')
input = f.read()

elves = cal_calc(input)
print(max(elves))
print("--- %s seconds ---" % (time.time() - start_time))
#p2
elves.sort()
print(sum(elves[-3:]))