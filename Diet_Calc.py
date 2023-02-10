a =0
def N():
  global a
  x = int(input("input the amount of calories you've taken today"))
  a +=x
  if a>=2000:
    print("you've already taken enough calories ")
  elif a<2000:
    print("you need to take",2000-a,"calories")
  y = input("do you want to end your day")
  if y =="end day":
    print("day ended")
  else:
    
    N()
N()
#GC33
