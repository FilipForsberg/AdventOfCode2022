#Gives int value froma ascci table
def get_item_prio(item):
    if item.isupper():
        return ord(item)-38
    else:
        return ord(item)-96

#Finds the duplicates of all sets given, returns as string
def get_duplicates(badge_group):
    sets = [set(b) for b in badge_group]
    duplicates = sets[0]
    for s in sets[1:]:
        duplicates &= s
    return ','.join(duplicates)

#Calculates the sum of duplicates asciii values
def find_duplicate_sum(input):
    duplicate_sum = 0
    for line in input:
        duplicates = get_duplicates({line[:len(line) // 2] , line[len(line) // 2:]})
        duplicate_sum += get_item_prio(duplicates)
    return duplicate_sum

#Same as above but groups instead of individuals
def get_badge_sum(input):
    badge_sum = 0
    badge_group = []
    for line in input:
        badge_group.append(line.strip())
        if len(badge_group) >=3:
            duplicates = get_duplicates(badge_group)
            badge_sum += get_item_prio(duplicates)
            badge_group = []
    return badge_sum

f = open('input.txt', 'r')
input = f.readlines()
#p1
print("Answer p1:" , find_duplicate_sum(input))
#p2
print("Answer p2:" , get_badge_sum(input))

