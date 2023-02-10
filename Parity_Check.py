count = 0
my_byte = str(input("Input your byte:"))
for i in my_byte:
    if i =="1": count = count +1
print(count)

if count%2 == 0:
  print(my_byte +"1")
else:
  print(my_byte +"0")
#TU23
