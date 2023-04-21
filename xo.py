import functions

checkTurn = True
playerInput = ""
firstPlayer = input("entre first player name ")
secondPlayer = input("entre first player name ")

while playerInput != "exit":
    if checkTurn == True:
        print(f"{firstPlayer}'s turn")
        checkTurn = False
    else:
        print(f"{secondPlayer}'s turn")
        checkTurn = True
    playerInput = input("entre your piece ")
    functions.checkPiece(playerInput)
    functions.drawShape()
    if functions.checkWins(firstPlayer,secondPlayer):
        break

