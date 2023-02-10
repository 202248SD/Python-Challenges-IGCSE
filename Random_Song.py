import random
a = int(input("How many songs in the playlist do you want?"))
playlist = []
for i in range(a):
  x = "Song",i
  playlist.append(x)
randint = random.randint(0,a-1)
print(playlist[randint])
