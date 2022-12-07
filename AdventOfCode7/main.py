class Directory:
    def __init__(self,name,root):
        self.name = name
        self.root = root
        self.fileSize = 0
        self.totalSize = 0
        self.dirs, self.files = [], []

    def addDirectory(self, dir):
        self.dirs.append(Directory(dir, self))

    def addFile(self, size, name):
        self.files.append(File(size, name))
        self.size = self.getFileSize()

    def goTo(self, name):
        for location in self.dirs:
            if location.name == name:
                return location

    def getFileSize(self):
        size = 0
        for file in self.files:
            size += file.size
        self.fileSize =size
        return self.fileSize

    def getDirs(self):
        return self.dirs

    def getFiles(self):
        return self.files

    def getTotalSize(self):
        size = 0
        size += self.getFileSize()
        for dir in self.dirs:
            size += dir.getTotalSize()
        self.totalSize = size
        return self.totalSize


class File:
    def __init__(self, size, name):
        self.name = name
        self.size = int(size)

def build_dir(currentLine, start):
        currentDir = start
        currentLine = currentLine
        if currentLine[0] == '$':
            if currentLine[1] == 'cd':
                if currentLine[2] == '..':
                    currentDir = currentDir.root

                else:
                    currentDir = currentDir.goTo(currentLine[2])
                currentLine = input.readline()
                currentLine = currentLine.strip().split()
            else:
                currentLine = input.readline()
                currentLine = currentLine.strip().split()
                while currentLine[0] != "$":
                    if currentLine[0].isdigit():
                        currentDir.addFile(currentLine[0], currentLine[1])

                    elif currentLine[0] == "dir":
                        currentDir.addDirectory(currentLine[1])
                    else:
                        print("Unknown command")
                    currentLine = input.readline()
                    currentLine = currentLine.strip().split()
                    if len(currentLine) == 0:
                        break
            if currentLine:
                build_dir(currentLine, currentDir)


def p1_solve(start, currentSum):
    if start.getTotalSize() <= 10**5:
        currentSum += start.getTotalSize()
        for dir in start.getDirs():
            currentSum += p1_solve(dir, 0)
    else:
        for dir in start.getDirs():
            currentSum += p1_solve(dir, 0)
    return currentSum

def p2_solve(dir, size, list):
    if dir.getTotalSize() >= size:
        list.append(dir.getTotalSize())
        [p2_solve(Ldir, size, list) for Ldir in dir.getDirs()]
    return list

def printBranch(start):

    print("Current Dir: " , start.name)
    if start.getTotalSize() <= 10**5:
        print("Add this: ", start.getTotalSize())
    print("Files: ")
    for file in start.getFiles():
        print(file.size, file.name)
    if len(start.getDirs()) > 0:
        print("Directories: ")
        for dir in start.getDirs():
            print(dir.name)
            printBranch(dir)
    return 0

input = open('input.txt' , 'r')
currentLine = input.readline()
start = Directory("/", None)

currentLine = input.readline()
currentLine = currentLine.strip().split()
build_dir(currentLine, start)
input.close()

#ans p1
print(p1_solve(start,0))

size_needed = 30000000 - (70000000 - start.getTotalSize())
list = []

list = p2_solve(start, size_needed, list)
list.sort()

#ans p2
print(list[0])

#printBranch(start)

