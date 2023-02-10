next_letter_lower=True
a = input("Input your string:")
text = a.upper()
b = ""
for lettersintext in text:
  if next_letter_lower == True:
    b=b+lettersintext.lower() 

  else:
    b=b+lettersintext.upper()

  if lettersintext == " ":
    b+= " "
    next_letter_lower = True
  else:
    next_letter_lower = False
print(b)
