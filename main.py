def printName():
    text="Hi I am asim saifi"
    demo="Demo"
    text=" ".join(["a","b","c"])
    print(f"{text}")


def handleList():
    a=[1,2,7,9,3,5]
    a.pop()
    a.append(4)
    a.remove(7)
    a.sort()
    print(f"{a}")

def useTuple():
    t=(10,30,20)
    l=list(t)
    l.append(1)
    t=tuple(l)
    print(f"{t}")

def useSet():
    s1={1,2,3,8,2,4}
    s2={9,2,5,7,3,4}
    print(f"{s1 | s2}")
    print(f"{s1 & s2}")
    print(f"{s1.union(s2)}")
    print(f"{s1.intersection(s2)}")
    print(f"{s1}")
    print(f"{type(s1)}")

def useFunction():
    def allOfThem(name,age,status="Active"):
        return (name,age,status)
    print(f"{allOfThem("Asim", 23)}")

    def keyWordArgs(name, age):
        return (name,age)       
    print(f"{keyWordArgs(age=20, name="Asim")}")

    def arbitraryArgs(*args):
        return sum(args)
    print(f"{arbitraryArgs(2,85,4,54,4,54,21,2)}")
    
    def arbitraryKArgs(**kargs):
        return kargs
    print(f"{arbitraryKArgs(age=70,name="Abba")}")

    def lambdaTest():
        products = [("Laptop", 1000), ("Mouse", 20), ("Monitor", 300)]
        products.sort(key= lambda item: item[1])
        print(f"{products}")        
    lambdaTest()

import utils
# print(f"{utils.getSqr(5)}")

# except handling
# utils.takeInput()

utils.filehandling()
