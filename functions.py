linesDraw = [' --- --- --- ','| 1 | 2 | 3 |',' --- --- --- ',
             '| 4 | 5 | 6 |',' --- --- --- ','| 7 | 8 | 9 |',' --- --- --- ']

fileOpen = open('D:\programers\material\level 3\Artifituial intiligance\python projects\XO_GAME\XO_GAME-python\outputFile.txt','w')


def drawShape():
    for lines in linesDraw:
        print(lines)
        fileOpen.write(lines+'\n')


def checkPiece(playerInput):
    indexSquare = playerInput[0]
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



def checkWins(firstPlayer,secondPlayer):
    if linesDraw[1] == '| x | x | x |':
        print("{} has win".format(firstPlayer))
        fileOpen.write("{} has win".format(firstPlayer)+'\n')
        return True
    elif linesDraw[1] == '| y | y | y |':
        print("{} has win".format(secondPlayer))
        fileOpen.write("{} has win".format(secondPlayer)+'\n')
        return True
    elif linesDraw[3] == '| x | x | x |':
        print("{} has win".format(firstPlayer))
        fileOpen.write("{} has win".format(firstPlayer)+'\n')
        return True
    elif linesDraw[3] == '| y | y | y |':
        print("{} has win".format(secondPlayer))
        fileOpen.write("{} has win".format(secondPlayer)+'\n')
        return True
    elif linesDraw[5] == '| x | x | x |':
        print("{} has win".format(firstPlayer))
        fileOpen.write("{} has win".format(firstPlayer)+'\n')
        return True
    elif linesDraw[5] == '| y | y | y |':
        print("{} has win".format(secondPlayer))
        fileOpen.write("{} has win".format(secondPlayer)+'\n')
        return True
