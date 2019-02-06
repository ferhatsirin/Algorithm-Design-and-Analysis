
def changePlayer(player) :
    if player =="Player1":
        return "Player2"
    else :
        return "Player1"

def gameNim(n,m,player ="Player1",path ="") :
    if n <= m:
        print(path,player ,"takes ",n," chips and wins")
    else :
        for i in range(1,m+1):
            newPath =path +str(player)+" takes "+str(i)+" chips, "
            gameNim(n-i,m,changePlayer(player),newPath)



if __name__ == "__main__" :
    print("Enter total number of chips in the pile : ",end="")
    n = int(input())
    print("How many chips can a player take at most? : ",end="")
    m =int(input())
    gameNim(n,m)

