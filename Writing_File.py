with open("counter.txt","w") as new_file:
    for i in range(11,0,-1):
        new_line = str(i-1)+"\n"
        new_file.write(new_line)
