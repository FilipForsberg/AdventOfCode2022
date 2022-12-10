def signalStrengthCalculator(input, start, step, stop):
    valueX = 1
    CycleValues = []
    for line in input:
         line = line.strip()
         if line == "noop":
             CycleValues.append(valueX)
         else:
            command, value = line.split()
            CycleValues.append(valueX)
            CycleValues.append(valueX)
            valueX += int(value)
    signalStrengthTotal = 0
    indexes = range(start, stop+1, step)
    for value,index in zip(CycleValues[start-1:stop+1: step], indexes):
        signalStrengthTotal += value * index
    return signalStrengthTotal, CycleValues


#Can probably do this more effectively
def PrintCrtScreen(CycleValues, ScreenWidth, ScreenHeight):
    CrtValues = []
    n= 0
    for line in CycleValues[0::ScreenWidth]:
        CrtValues.append(CycleValues[ScreenWidth * n:ScreenWidth* (n+1)])
        n+= 1
    for CrtLine in CrtValues:
        i = 0
        CrtLineString = []
        for value in CrtLine:
            if value == i-1 or value == i or value == i+1:
                CrtLineString.append("#")
            else:
                CrtLineString.append(".")
            i += 1
        print(CrtLineString)
    return 0

f = open("input.txt" , "r")
input = f.readlines()
start ,step , stop= 20 , 40, 220
signalStrength, CycleValues = signalStrengthCalculator(input, start, step, stop)
print("P1 ans: " , signalStrength)
print("P2 ans")
PrintCrtScreen(CycleValues, 40, 6)
