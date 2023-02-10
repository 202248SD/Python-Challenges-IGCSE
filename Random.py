import random
ChooseName = ["Jack","Alex","Bob","Steve","Tom"]
a = random.choice(ChooseName)
print("Do you want to remove",a,"?")
b = input("y/n")
if b in ["y","Y"]:
  ChooseName.remove(a)
  print(ChooseName)
else:
  print(ChooseName)
#TU10
