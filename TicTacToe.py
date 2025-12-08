def sum(a,b,c):
    return a+b+c

def Board(xState,zState):
    zero='X' if xState[0] else ('O' if zState[0] else 0)
    one='X' if xState[1] else ('O' if zState[1] else 1)
    two='X' if xState[2] else ('O' if zState[2] else 2)

    three='X' if xState[3] else ('O' if zState[3] else 3)
    four='X' if xState[4] else ('O' if zState[4] else 4)
    five='X' if xState[5] else ('O' if zState[5] else 5)

    six='X' if xState[6] else ('O' if zState[6] else 6)
    seven='X' if xState[7] else ('O' if zState[7] else 7)
    eight='X' if xState[8] else ('O' if zState[8] else 8)
    
    print(f"{zero} | {one} | {two} ")
    print(f"{three} | {four} | {five} ")
    print(f"{six} | {seven} | {eight} ")

def Winner(xState,zState):
    wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if (sum(xState[win[0]], xState[win[1]], xState[win[2]])==3):
            print("\nX won the Match")
            return 1
        if (sum(zState[win[0]], zState[win[1]], zState[win[2]])==3):
            print("\n0 won the Match")
            return 0
    return -1

if __name__=="__main__":
    print("Hello")
    xState=[0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState=[0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn=1
    while(True):
        Board(xState,zState)
        if(turn ==1):
            print("\nPlayer 1's Turn")
            val=int(input("Please enter a value: "))
            xState[val]=1
        else:
            print("\nPlayer 2's Turn")
            val=int(input("Please enter a value: "))
            zState[val]=1

        check=Winner(xState,zState)
        if(check != -1):
            Board(xState,zState)
            print("\nMatch Over")
            break

        turn = 1-turn
        
