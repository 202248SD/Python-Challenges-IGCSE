import random
count = 0
b = ["1010101","1010111","0110101","1101001","1011101"]
a = random.choice(b)
for i in a:
  if i =="1": count = count +1
print(count)

if count%2 == 0:
  c = a +"1"
else:
  c = a +"0"
print("You are correct")
