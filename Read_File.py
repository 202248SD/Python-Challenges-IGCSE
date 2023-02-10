import time

a = input("Would you like to read mam.txt or rudyard.txt choose r or m to choose:")
if a =="r":
  with open("rudyard.txt","r") as whole_file:
   for line in whole_file:
     time.sleep(0.5)
     print(line,end="")
elif a =="m":
  with open("mam.txt") as whole_file:
   for line in whole_file:
     time.sleep(0.5)
     print(line,end="")
else:
  print("error")
  
