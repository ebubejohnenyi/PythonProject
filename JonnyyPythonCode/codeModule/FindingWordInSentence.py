found = False
names = ['Ebube', 'John', 'Enyi', 'Precious']
for name in names:
    if name.startswith("E"):
        print("found")
        found = True
        break
if not found:
    print("not found")

