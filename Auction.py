Auction_Board = [
["Item No.", "Name", "No of bids","Description", "Start bid k$", "Current Bid k$"],
["1     ","Artwork     ",0,"     Art piece","         ",11,"            ",0],
["2     ","Ferrari     ",0,"     Made 2018","         ",99,"            ",0],
["3     ","Laptop      ",0,"       Mac Pro","         ",10,"            ",0],
["4     ","Rolex       ",0,"    Submariner","         ",13,"            ",0],
["5     ","Mansion     ",0,"  In North Cal","         ",80,"            ",0],
["6     ","Wristwatch  ",0,"  Cassio Watch","         ",32,"            ",0],
["7     ","VanGogh Art ",0,"        Scream","         ",54,"            ",0],
["8     ","BMW         ",0,"       Vintage","         ",21,"            ",0],
["9     ","Gold Bar    ",0,"     50 ounces","         ",14,"            ",0],
["10    ","Diamond Ring",0,"      13 carat","         ",78,"            ",0],]
y = "y"
def print_Board():
  for i in range(11):
    print(*Auction_Board[i])
def Total():
  Total = 0
  for i in range(10):
    Total = Total + Auction_Board[i+1][7]
  print("Total money spent:", Total*1000, "$")
  
while y == "y":
  print_Board()
  a = int(input("Which item no. do you want to bid on?"))
  print(*Auction_Board[0])
  print(*Auction_Board[a])
  b = int(input("How much do you want to bid?"))
  if b>Auction_Board[a][7] and b>Auction_Board[a][5]: 
    Auction_Board[a][7] = b
    Auction_Board[a][2] = Auction_Board[a][2] + 1
  else:
    print("Your bid is too small!")
  y = input("Do you still want to bid y/n:")
else:
  print("The bid has ended!")
  Total()
  
