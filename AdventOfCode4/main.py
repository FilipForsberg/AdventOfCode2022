f = open('input.txt', 'r')
input = f.readlines()

def overlap_counter(input):
    full_overlap_total = 0
    partial_overlap_total = 0
    for line in input:
        r1,r2 = line.split(',')
        s1, e1 = r1.split('-')
        s2, e2 = r2.split('-')
        s1,e1,s2,e2 = [int(x) for x in [s1,e1,s2,e2]]
#Full overlap counter
        if (s1 <= s2 and e2 <= e1 or s2 <= s1 and e1 <= e2):
            full_overlap_total += 1
#Partial overlap counter
        elif not (e1 < s2 or s1 > e2):
            partial_overlap_total += 1

    return full_overlap_total, full_overlap_total + partial_overlap_total
ans1 , ans2 = overlap_counter(input)
print(ans1, ans2)




