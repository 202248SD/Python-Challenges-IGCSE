a = input("the amount of time it takes for a packet of data to be captured, transmitted, \n processed through multiple devices, then received at its destination \n and decoded.")
x = 0
if a in ["latency"]:
  print("You are correct!:")
  x += 1
else:
  print("The answer is Latency")

b = input("The maximum amount of data transmitted over an internet \n connection in a given amount of time.")

if b in ["Bandwidth"]:
  print("You are correct!")
  x += 1
else:
  print("The answer is Bandwidth")

c = input("Unit of data routed between an origin and a destination on the internet")

if c in ["packet","Packet", "Packets", "packets"]:
  print("You are correct!")
  x += 1
else:
  print("The answer is Packet")

d = input("when one or more transmitted data packets fail to arrive at their destination.")

if d in ["Packet Loss", "packet loss", ]:
  print("You are correct!")
  x += 1
else:
  print("The answer is packet loss")

e = input("Bits are sent one signal at a time over a single wire.Using fibre-optic cable, data transfer rates ranging from around 50 Megabits per second (Mbs) to 100 Gigabits per second (Gbs) can be achieved Used with USB (Universal Serial Bus) cables")

if e in ["serial","Serial" "Serial transmission"]:
  print("you are correct!")
  x += 1
else:
  print("The answer is Serial transmission")

f = input("Signals (bits) are sent simultaneously over a number of parallel wires Computer data ribbons:Known as Parallel ATA Cables Used inside the computer to connect components and drives Use 8, 16 or 32 bits sent down separate lines")

if f in ["Parallel","parallel""parallel transmission"]:
  print("You are correct!")
  x+=1
else:
  print("The answer is parallel transmission")

g = input("Data travels in one direction only")

if g in ["Simplex", "Simplex transmission"]:
  print("You are correct!")
  x+=1
else:
  print("The answer is Simplex")

h = int(input("How do you calculate the bitrate of channel \n [1] bit rate x baud rate, [2] bit rate x number of bits per channel, [3]bit rate / number of bits a channel"))
if h == 2:
  print("You are correct!")
  x+=1
else:
  print("The answer is [2]")
print("You have gotten",x,"/7 questions correct!")
