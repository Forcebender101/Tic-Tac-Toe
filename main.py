import replit
gameEnd=0
tieCheck = 0
playAgain = 0
marker = ["1","2","3","4","5","6","7","8","9"]
def drawBoard():
  replit.clear()
  print("\n"*3)
  print("   |   |  ")
  print(" " + marker[0] + " | "+marker[1] +" | "+marker[2] +" ")
  print ("___|___|___")
  print ("   |   |  ")
  print(" " + marker[3] + " | "+ marker[4] + " | "+ marker[5] + " ")
  print ("___|___|___")
  print ("   |   |  ")
  print(" "+ marker[6] +" | " + marker[7] +" | " + marker[8] +" ")
  print("   |   |  ")
  return()
def player1Choose():
  player1ValidMove = 0
  while player1ValidMove == 0:
    player1Choice = int(input("Player 1, pick where you want to go\n"))
    player1Choice = player1Choice-1
    if marker[player1Choice] not in ["o","x"]:
      marker[player1Choice] = "x"
      player1ValidMove = 1
    elif marker[player1Choice] in ["o","x"]:
      print("Theres already a mark there, try again.")
    else:
      print ("that doesnt seem to be a valid postition")
def player2Choose():
 player2ValidMove = 0
 while player2ValidMove == 0:
  player2Choice = int(input("Player 2, pick where you want to go\n"))
  player2Choice = player2Choice-1
  if marker[player2Choice] not in ["o","x"]:
    marker[player2Choice] = "o"
    player2ValidMove = 1
  elif marker[player2Choice] in ["o","x"]:
    print("Theres already a mark there, try again.")
  else:
   print ("that doesnt seem to be a valid postition")
def checkWin():
  gameEnd = 0
  #Columns
  if marker[0] == marker[3] == marker[6]:
    if marker[0] == "o":
      print ("Player 2 wins!!")
    elif marker[0] == "x":
      print("Player 1 wins!")
    gameEnd = 1
  elif marker[1]==marker[4] == marker[7]:
    if marker[1] == "o":
      print ("Player 2 wins!")
    elif marker[1] == "x":
      print("Player 1 wins!")
    gameEnd = 1
  elif marker[2] == marker[5] == marker[8]:
    if marker[2] == "o":
      print ("Player 2 wins!")
    elif marker[2] == "x":
      print("Player 1 wins!")
    gameEnd = 1
  #Rows
  elif marker[0]==marker[1]==marker[2]:
    if marker[0] == "o":
      print ("Player 2 wins!")
    elif marker[0] == "x":
      print("Player 1 wins!")
    gameEnd = 1
  elif marker[3]==marker[4]==marker[5]:
    if marker[3] == "o":
      print ("Player 2 wins!")
    elif marker[3] == "x":
      print("Player 1 wins!")
    gameEnd = 1
  elif marker[6]==marker[7]==marker[8]:
    if marker[6] == "o":
      print ("Player 2 wins!")
    elif marker[6] == "x":
      print("Player 1 wins!")
    gameEnd = 1
  #diagonals
  elif marker[0]==marker[4]==marker[8]:
    if marker[0] == "o":
      print ("Player 2 wins!")
    elif marker[0] == "x":
      print("Player 1 wins!")
    gameEnd = 1
  elif marker[2]==marker[4]==marker[6]:
    if marker[2] == "o":
      print ("Player 2 wins!")
    elif marker[2] == "x":
      print("Player 1 wins!")
    gameEnd = 1
  elif marker.count("x") + marker.count("o") == 9:
    print("You Tied!")
    gameEnd = 1
  return(gameEnd)
while 1==1:
  while gameEnd==0:
    drawBoard()
    player1Choose()
    drawBoard()
    gameEnd = checkWin()
    if gameEnd == 1:
      break
    player2Choose()
    drawBoard()
    gameEnd = checkWin()

  playAgain = input("Would you like to play again?\nY/N\n").lower()
  if playAgain in ["y","yes"]:
    marker = ["1","2","3","4","5","6","7","8","9"]
    gameEnd = 0
  elif playAgain in ["n","no"]:
    print("Goodbye!")
    exit()

  