print("=================================")
print("|| Water  || Cola   || Orangina||")
print("||[1]$0.9 ||[2]$1.4 || [3]$1.3 ||")
print("_________________________________")
print("|| Pepsi  || Fanta  || Gatorade||")
print("||[4]$1.4 ||[5]$1.2 || [6]$1.6 ||")
print("_________________________________")
print("|| Soda   ||Sprite  || Ice Tea ||")
print("||[7]$1.2 ||[8]$1.3 || [9]$1.1 ||")
print("_________________________________")
print("|| Polar  ||Perrier ||Dr.Pepper||")
print("||[10]$1.1||[11]$1.3||[12]$1.5 ||")
print("=================================")

x = ["Water", "Cola", "Orangina", "Pepsi", "Fanta", "Gatorade", "Soda", "Sprite", "Ice Tea", "Polar", "Perrier", "Dr.Pepper"]
y = [0.9,1.4,1.3,1.4,1.2,1.6,1.2,1.3,1.1,1.1,1.3,1.5]
a = int(input("Pick the number of the beverage you want:"))
b = a-1
c = int(input("put your coins inside the machine:"))
d = c - y[b]
print("Here is your", x[b])
print("Your change is $",d)
#GC25
