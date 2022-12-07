class Directory:
    def __init__(self,name,root):
        self.name = name
        self.root = root
        self.size = 0
        self.dirs, self.files = [], []

    def addDirectory(self, dir):
        self.dirs.append(Directory(dir, self))

    def addFile(self, size, name):
        self.files.append(File(size, name))

    def goTo(self, name):
        for location in self.dirs:
            if location.name == name:
                return location

    def getSize(self):
        size = 0
        for file in self.files:
            size += file.size
        self.size =size
        return self.size

    def getDirs(self):
        return self.dirs

class File:
    def __init__(self, size, name):
        self.name = name
        self.size = int(size)

def build_dir(input, currentDir):
    currentDir = start
    for line in input[1:]:
        line = line.strip().split()
        if line[0] == '$':
            if line[1] == 'cd':
                if line[2] == '..':
                    currentDir = currentDir.root
                    continue

                currentDir = currentDir.goTo(line[2])
            continue
        elif line[0] == "dir":
            currentDir.addDirectory(line[1])
        else:
            currentDir.addFile(line[0], line[1])
    return start
def total_size(start, currentSum):
    currentSum += start.getSize()
    for dir in start.getDirs():
            currentSum += total_size(dir, 0)
    return currentSum

def p1_solve(start, currentSum):
    if start.getSize() <= (100000):
        currentSum += start.getSize()
    for dir in start.getDirs():
            currentSum += p1_solve(dir, 0)
    return currentSum



f = open('input.txt' , 'r')
input = f.readlines()
start = Directory("/", None)
start = build_dir(input, start)

ans_p1 = 1182909
total = 42677139
print(p1_solve(start,0))
print(total_size(start, 0))


