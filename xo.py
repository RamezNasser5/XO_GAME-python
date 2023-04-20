def drawShape(linesDraw):
    fileOpen = open('D:\programers\material\level 3\Artifituial intiligance\python projects\XO_GAME\XO_GAME-python\outputFile.txt','w')
    for lines in linesDraw:
        print(lines)
        fileOpen.write(lines+'\n')
    fileOpen.close()    

def checkPiece():
    match indexSquare:
        case '1':
            linesDraw[1] = linesDraw[1][:2]+playerInput[2]+linesDraw[1][3:]
        case '2':
            linesDraw[1] = linesDraw[1][:6]+playerInput[2]+linesDraw[1][7:]
        case '3':
            linesDraw[1] = linesDraw[1][:10]+playerInput[2]+linesDraw[1][11:]
        case '4':
            linesDraw[3] = linesDraw[3][:2]+playerInput[2]+linesDraw[3][3:]
        case '5':
            linesDraw[3] = linesDraw[3][:6]+playerInput[2]+linesDraw[3][7:]
        case '6':
            linesDraw[3] = linesDraw[3][:10]+playerInput[2]+linesDraw[3][11:]
        case '7':
            linesDraw[5] = linesDraw[5][:2]+playerInput[2]+linesDraw[5][3:]
        case '8':
            linesDraw[5] = linesDraw[5][:6]+playerInput[2]+linesDraw[5][7:]
        case '9':
            linesDraw[5] = linesDraw[5][:10]+playerInput[2]+linesDraw[5][11:]
    return linesDraw                                    

checkTurn = True
playerInput = ""
firstPlayer = input("entre first player name ")
secondPlayer = input("entre first player name ")
linesDraw = [' --- --- --- ','| 1 | 2 | 3 |',' --- --- --- ',
             '| 4 | 5 | 6 |',' --- --- --- ','| 7 | 8 | 9 |',' --- --- --- ']
while playerInput != "exit":
    if checkTurn == True:
        print(f"{firstPlayer}'s turn")
        checkTurn = False
    else:
        print(f"{secondPlayer}'s turn")
        checkTurn = True
    playerInput = input("entre your piece ")
    indexSquare = playerInput[0]
    checkPiece()
    drawShape(checkPiece())

