# class Filter:
#     def __init__(self):
#         pass

#     def apply(self, file):
#         pass

class Filter:
    def __init__(self, size, extension):
        self.size = size
        self.extension = extension

    def check(self, file):
        return file.size > self.size and file.extension == self.extension


class File:
    def __init__(self, name, size):
        self.name = name
        self.isDirectory = False if '.' in name else True
        self.size = size
        self.extension = name.split(".")[1] if '.' in name else ""
        self.children = []

    # def __repr__(self):
    #     return "{" + self.name + "}"

class FindCommand:

    def __init__(self, filters):
        self.filter = filters

    
    # This implementation is OR implementation of filter. 
    def find(self, root):

        result = []
        def traverse(root, result):
            for f in root.children:
                if f.isDirectory:
                    traverse(f, result)
                else:
                    if self.filter.check(f):
                        result.append(f.name)
        #return result
        traverse(root, result)
        return result

f1 = File("StarTrek.txt", 5)
f2 = File("StarWars.xml", 10)
f3 = File("JusticeLeague.txt", 15)
f4 = File("IronMan.txt", 9)
f5 = File("Spock.jpg", 1)
f6 = File("BigBangTheory.xml", 50)
f7 = File("MissionImpossible", 30)
f8 = File("BreakingBad", 60)
f9 = File("root", 100)

f9.children = [f7, f8]
f7.children = [f1, f2, f3]
f8.children = [f4, f5, f6]

filter1 = Filter(15, "xml")

fs = FindCommand(filter1)

print(fs.find(f9))
