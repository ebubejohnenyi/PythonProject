names = ["john", "john", "Precious", "Paul", "Peter"]
def myFun():
    checker = set(names)
    if len(names) != len(checker):
        print("Duplicate found in list")
    else:
        print("Duplicate not found")
    print(names)
myFun()