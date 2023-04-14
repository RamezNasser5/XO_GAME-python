checkTurn = True
playerInput = ""
firstPlayer = input("entre first player name ")
secondPlayer = input("entre first player name ")
linesDraw = [' --- --- --- ','| 1 | 2 | 3 |',' --- --- --- ',
             '| 4 | 5 | 6 |',' --- --- --- ','| 7 | 8 | 9 |',' --- --- --- ']
for lines in linesDraw:
    print(lines)
while playerInput != "exit":
    if checkTurn == True:
        print(f"{firstPlayer}'s turn")
        checkTurn = False
    else:
        print(f"{secondPlayer}'s turn")
        checkTurn = True
    playerInput = input("entre your piece ")
    indexSquare = playerInput[0]
    if indexSquare == '1' or indexSquare == '2' or indexSquare == '3':
        linesDraw[1].replace(indexSquare,playerInput[2])
    elif indexSquare == '4' or indexSquare == '5' or indexSquare == '6':
        linesDraw[3].replace(indexSquare,playerInput[2])
    else:
        linesDraw[5].replace(indexSquare,playerInput[2])
    for lines in linesDraw:
        print(lines)    

