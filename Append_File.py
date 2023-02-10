a=0
with open("counter.txt","r") as existing_file:
  for line in existing_file:
    a+=1
with open("counter.txt","w") as existing_file:
    for i in range(1,a+11):
        line_to_write = str(i)+"\n"
        existing_file.write(line_to_write)
