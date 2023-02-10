x = int(input("Do you want to find the file size of a sound file[1], or a image file[2]"))
if x == 1:
  s = int(input("What is the length(seconds):"))
  b = int(input("What is the sample resolution(bits):"))
  h = int(input("What is the sample rate(Hz):"))
  y=s*b*h
  if y < 8:
    a = y
    print("Your file size is", a, "bits")
  elif 8<y<1024*8:
    a = y/8
    print("Your file size is", a, "Bytes")    
  elif 1024*8<y<8*1024**2:
    a = y/(1024*8)
    print("Your file size is", a, "KiB")
  elif 8*1024**2<y<8*1024**3:
    a = y/(8*1024**2)
    print("Your file size is", a, "MiB")
  elif 8*1024**3<y<8*1024**4:
    a = y/(8*1024**3)
    print("Your file size is", a, "GiB")
  elif y > 8*1024**4:
    a = y/(8*1024**4)
    print("Your file size is", a, "TiB")
elif x == 2:
  s = int(input("What is the width:"))
  b = int(input("What is the height:"))
  h = int(input("What is the colour depth(bits):"))
  y=s*b*h
  if y < 8:
    a = y
    print("Your file size is", a, "bits")
  elif 8<y<1024*8:
    a = y/8
    print("Your file size is", a, "Bytes")    
  elif 1024*8<y<8*1024**2:
    a = y/(1024*8)
    print("Your file size is", a, "KiB")
  elif 8*1024**2<y<8*1024**3:
    a = y/(8*1024**2)
    print("Your file size is", a, "MiB")
  elif 8*1024**3<y<8*1024**4:
    a = y/(8*1024**3)
    print("Your file size is", a, "GiB")
  elif y > 8*1024**4:
    a = y/(8*1024**4)
    print("Your file size is", a, "TiB")
else:
  print("Invalid, input 1 or 2")
