multiplier = 1 #alternates between 1 and 3
total = 0
isbn = "978-0-545-01022-1"
#isbn = input("Input an ISBN-13") User can input instead.

#This removes dashes
isbn=isbn.replace("-","")

#the last digit is the check digit
check_digit=int(isbn[12])
print("check digit",check_digit)

for i in range(12):
	total = total + (int(isbn[i])*multiplier)
	if multiplier == 1:
		multiplier = 3
	else:
		multiplier = 1

remainder = total % 10
print("remainder",remainder)

if (10-remainder) == check_digit:
	print("ISBN Validated")
else:
	print("ISBN not valid")
#GC13
