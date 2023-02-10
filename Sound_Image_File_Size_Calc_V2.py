import random
import time
score = 0
core = 0
g = input("Do you want to work on sound or image questions?")
w = int(input("how many questions do you want?(Don't ask for too many)"))
if g == "sound":#code for sound questions
  for i in range(w):
    rate = [4000,44100,48000,96000]
    res = [8,16,24,32]

#code for choosing values
    a = random.choice(rate)
    b = random.choice(res)
    c = random.randint(30,240)
    d = random.randint(1,5)
    print("\n\n\033[36mQuestion",i+1,)

    print ("\033[37mThe sample rate of the soundtrack is\033[35m",a,"\033[37mhz")
    print ("The sample resolution of the soundtrack is\033[35m",b,"\033[37mbits")
    print ("The length of the sountrack is\033[35m",c,"\033[37mseconds")
    print ("Number of channels\033[35m",d,)

    x = ((((a*b*c*d)/8)/1024)/1024)
    y = round(x)
    z = int(input("\n\033[32mPut your answer in MiB here:(nearest whole number)"))

    if y == z:
      print("\033[37mYou are correct \033[1m:D\033[0m")
      score = score + 1

    else:
      print("\033[37mYou are wrong :<")
      print(a,"x",b,"x",c,"x",d,"=",a*b*c*d)
      print("/\This is the file size in bits\n")

      print(a*b*c*d,"/8/1024/1024 =~",y,)
      print("/\Convert bits to MiB\n")
    print("Your score is",score)
    print("The file size of the image is:", y, "MiB\n")
    print("-----------------------------------------------")
    time.sleep(0.5)
  print("Your total score is",score,"/",w)
elif g == "image":#code for image questions
  for i in range(w):
    width = [4000,44100,48000,96000]
    height = [8,16,24,332]
    colour_depth = [8,16,24,32,64]

#code for choosing values
    a = random.choice(width)
    b = random.choice(height)
    c = random.choice(colour_depth)
    print("\n\n\033[36mQuestion",i+1,)

    print ("\033[37mThe width of the image is\033[35m",a,"\033[37mpixels")
    print ("The height of the image is\033[35m",b,"\033[37mpixels")
    print ("The colour depth of the image is\033[35m",c,"\033[37mbits")

    x = ((((a*b*c)/8)/1024)/1024)
    y = round(x)
    z = int(input("\n\033[32mPut your answer in MiB here:(nearest whole number)"))

    if y == z:
      print("\033[37mYou are correct \033[1m:D\033[0m")
      score = score + 1
#working out
    else:
      print("\033[37mYou are wrong :<")
      print(a,"x",b,"x",c,"=",a*b*c)
      print("/\This is the file size in bits\n")
      print(a*b*c,"/8/1024/1024 =~",y,)
      print("/\Convert bits to MiB\n")
    print("\033[37mYour score is",score)
    print("The file size of the image is:", y, "MiB\n")
    print("-----------------------------------------------")
    time.sleep(0.5)
  print("Your total score is",score,"/",w)
  #Thanks to everybody who tested my code!, 
