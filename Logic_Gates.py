def OR(A,B):
  if A==1 or B==1:
    return True
  else:
    return False

def AND(A,B):
  if A==1 and B==1:
    return True
  else:
    return False

def NOT(A):
  if A==1:
    return False
  else:
    return True

def NAND(A,B):
  if A==1 and B==1:
    return False
  else:
    return True

def NOR(A,B):
  if A==1 or B==1:
    return False
  else:
    return True

def XOR(A,B):
  if A==B:
    return False
  else:
    return True

def TTable(A):
  if A == OR:
    print("A B Output")
    print(0,0,+OR(0,0))
    print(1,0,+OR(1,0))
    print(0,1,+OR(0,1))
    print(1,1,+OR(1,1))
    print(0,0,+OR(0,0))
  elif A == AND:
    print("A B Output")
    print(0,0,+AND(0,0))
    print(1,0,+AND(1,0))
    print(0,1,+AND(0,1))
    print(1,1,+AND(1,1))
    print(0,0,+AND(0,0))
  elif A == NOT:
    print("A B Output")
    print(0,0,+NOT(0,0))
    print(1,0,+NOT(1,0))
    print(0,1,+NOT(0,1))
    print(1,1,+NOT(1,1))
    print(0,0,+NOT(0,0))
  elif A == NAND:
    print("A B Output")
    print(0,0,+NAND(0,0))
    print(1,0,+NAND(1,0))
    print(0,1,+NAND(0,1))
    print(1,1,+NAND(1,1))
    print(0,0,+NAND(0,0))
  elif A == NOR:
    print("A B Output")
    print(0,0,+NOR(0,0))
    print(1,0,+NOR(1,0))
    print(0,1,+NOR(0,1))
    print(1,1,+NOR(1,1))
    print(0,0,+NOR(0,0))
  elif A == XOR:
    print("A B Output")
    print(0,0,+XOR(0,0))
    print(1,0,+XOR(1,0))
    print(0,1,+XOR(0,1))
    print(1,1,+XOR(1,1))
    print(0,0,+XOR(0,0))
  
print ("Boolean in 0 or 1")
print(OR(1,1))
print(AND(0,1))
print(NOT(0))
print(NAND(1,1))
print(NOR(1,0))
print(XOR(0,0))
TTable(OR)
a = True
