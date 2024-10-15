import time
"""This game takes two players"""

print("WELCOME! TO THE TIC-TAC-TOE GAME")
time.sleep(1) #sleep function make the next line of code to take a little time before execution
print("HOPE YOU'LL ENJOY PLAYING THE GAME :)")
time.sleep(1)

"""x,z take the player's names as input"""

x=input("Enter the name of the participant?")
z= input("Enter the name of the second participant?")

def sum(a,b,c):#coz in_built sum function take only two parameters
    y = a+b+c
    return y

def printboard(xstate,zstate):
    zero = 'X' if xstate[0] else ('O' if zstate[0] else 0)
    one = 'X' if xstate[1] else ('O' if zstate[1] else 1)
    two = 'X' if xstate[2] else ('O' if zstate[2] else 2)
    three = 'X' if xstate[3] else ('O' if zstate[3] else 3)
    four = 'X' if xstate[4] else ('O' if zstate[4] else 4)
    five = 'X' if xstate[5] else ('O' if zstate[5] else 5)
    six = 'X' if xstate[6] else ('O' if zstate[6] else 6)
    seven = 'X' if xstate[7] else ('O' if zstate[7] else 7)
    eight= 'X' if xstate[8] else ('O' if zstate[8] else 8)

    print(f"{zero} | {one} | {two}")
    print(f"--|---|--")
    print(f"{three} | {four} | {five}")
    print(f"--|---|--")
    print(f"{six} | {seven} | {eight}")
  
def check_winner(xstate,zstate):
  #possibilities where X can win
    xwins=[[0,1,2],[3,4,5],[6,7,8],[1,4,7],[0,4,8],[2,5,8],[2,4,6],[0,3,6]]
    for win in xwins:
        if (sum(xstate[win[0]],xstate[win[1]],xstate[win[2]]) == 3):
            print(f"{x} have won the match")
            time.sleep(0.5)
            print(f"Good game {x} congratulations!")
            return 1
        if (sum(zstate[win[0]],zstate[win[1]],zstate[win[2]]) == 3 ):
            print(f"{z} have won the match")
            time.sleep(0.5)
            print(f"Good game {z} congratulations!")
            return 0
    return-1

if __name__ == '__main__':
    xstate=[0,0,0,0,0,0,0,0,0]
    zstate=[0,0,0,0,0,0,0,0,0]
    turn=1 # by default the first turn would be X's
    print("welcome to the tic tac toe!")
    while True:
        printboard(xstate,zstate)
        if turn==1:
            print(f"{x}'s Turn")
            value= int(input("Please enter a value?"))
            xstate[value]=1 # replacing the user input with the index value of the xstate
        else:
            print(f"{z}'s Turn")
            value=int(input("Please enter a value?"))
            zstate[value]=1
        cwin = check_winner(xstate,zstate)

        if cwin!=-1:
            print("Game over!")
            break
        turn=1-turn
