
def Board(xState, zState):
    # Prepare the board cells
    def cell(i):
        if xState[i]: return 'X'
        if zState[i]: return 'O'
        return str(i)

    print(f"\n{cell(0)} | {cell(1)} | {cell(2)}")
    print(f"{cell(3)} | {cell(4)} | {cell(5)}")
    print(f"{cell(6)} | {cell(7)} | {cell(8)}")


def isDraw(xState, zState):
    # If all 9 positions are filled and no winner:
    return sum(xState) + sum(zState) == 9

def Winner(xState, zState):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]

    for a, b, c in wins:
        if xState[a] + xState[b] + xState[c] == 3:
            print("\nX won the match!")
            return 1
        if zState[a] + zState[b] + zState[c] == 3:
            print("\nO won the match!")
            return 0
    return -1

def Restart():
    again = input("\nDo you want to play again? (y/n): ").lower()

    if again != 'y':
        print("\nThanks for playing!")
    else:
        print("\nRestarting game...\n")
        playGame()
    

def playGame():
    print("Tic Tac Toe Game\n")

    xState = [0] * 9
    zState = [0] * 9
    turn = 1  # 1 => X, 0 => O

    while True:
        Board(xState, zState)

        while True:
            if turn == 1:
                print("\nPlayer X's Turn") 
            elif turn== 0 :
                print("\nPlayer O's Turn")

            val = int(input("Choose a position (0–8): "))

            if xState[val] == 1 or zState[val] == 1:
                print("!!! Position already filled! Choose another one.")
            else:
                break
        if turn ==1:
            xState[val] = 1
        else:
            zState[val] = 1


        result = Winner(xState, zState)
        if result != -1:
            Board(xState, zState)
            print("\nGame Over!")
            break

        if isDraw(xState, zState):
            Board(xState, zState)
            print("\nMatch Draw!")
            break
        
        turn = 1 - turn

if __name__=="__main__":
    playGame()
    Restart()
