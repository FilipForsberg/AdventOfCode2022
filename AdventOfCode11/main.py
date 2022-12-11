import copy
class Monkey:
    def __init__(self, name,StartingItems, Operation, Test, throwTrue, throwFalse):
        self.Items = StartingItems
        self.Name = name
        self.Operation = str(Operation)
        self.Test = int(Test[2])
        self.throwTrue = throwTrue
        self.throwFalse = throwFalse
        self.inspectionCounter = 0
    def addItem(self, item):
        self.Items.append(item)

    def removeItems(self):
        self.Items = []

    def throwItem(self, item):
        if item%self.Test == 0:
            return self.throwTrue
        else:
            return self.throwFalse
    def changeWorryLevel(self, item):
        old = item
        new = eval(self.Operation)
        return new

    def inspection(self):
        self.inspectionCounter += 1

def createMonkeyObjects(input):
    monkeys = []
    monkeyObjects = []
    for monkey in input:
        currentAttributes = []
        for attribute in monkey:
            attribute = attribute.strip().split()
            attribute = [x.strip(",:") for x in attribute]
            currentAttributes.append(attribute)
        monkeys.append(currentAttributes)
    for monkey in monkeys:
        name = monkey[0][1]
        StartingItems = [int(x) for x in monkey[1][2:]]
        Operation = " ".join(monkey[2][3:])
        Test = monkey[3][1:]
        throwTrue = int(monkey[4][5])
        throwFalse = int(monkey[5][5])
        monkeyObjects.append(Monkey(name, StartingItems, Operation, Test, throwTrue, throwFalse))
    return monkeyObjects

def monkeyRound(monkeyObjects, p1, lcm):
    for monkey in monkeyObjects:
        for item in monkey.Items:
            monkey.inspection()
            new = monkey.changeWorryLevel(item)
            if new > lcm:
                new = new % lcm
            if p1:
                new = new//3
            throwsItemTo = monkeyObjects[monkey.throwItem(new)]
            throwsItemTo.addItem(new)
        monkey.removeItems()
    return monkeyObjects

def simulateMonkeyRounds(monkeyObjects, rounds, p1, lcm):
    monkeyInspections = []
    for round in range(0,rounds):
        monkeyObjects = monkeyRound(monkeyObjects, p1, lcm)
    for monkey in monkeyObjects:
        monkeyInspections.append(monkey.inspectionCounter)
    monkeyInspections.sort()
    monkeyBusiness = monkeyInspections[-1] * monkeyInspections[-2]
    return monkeyBusiness

f = open("input.txt" , "r")
input = f.read()
input = input.split("\n\n")
monkeys = []
input = [line.strip().split("\n") for line in input]
monkeyObjectsP1 = createMonkeyObjects(input)
monkeyObjectsP2 = copy.deepcopy(monkeyObjectsP1)
lowestCommonMultiple = 1
for monkey in monkeyObjectsP1:
    lowestCommonMultiple *= monkey.Test

value = simulateMonkeyRounds(monkeyObjectsP1, 20, True, lowestCommonMultiple)
print("P1 ans: " , value)
value2 = simulateMonkeyRounds(monkeyObjectsP2, 10000, False, lowestCommonMultiple)
print("P2 ans: " , value2)