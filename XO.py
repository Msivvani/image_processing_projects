import numpy as np
import cv2

board=["#"," "," "," "," "," "," "," "," "," "]

print("Player 1 is assigned O\nplayer 2 is assigned X")

image=np.zeros((512,512,3),np.uint8)
cv2.line(image,(100,200),(400,200),(255,255,255),3)           #grid for the game
cv2.line(image,(100,300),(400,300),(255,255,255),3)
cv2.line(image,(200,100),(200,400),(255,255,255),3)
cv2.line(image,(300,100),(300,400),(255,255,255),3)

def draw_circle(event,x,y,flags,param):                       #drawing circle with the point clicked as centre
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(image,(x,y),30,(255,0,0),3)
        index1=board_index(x,y)
        board[index1]="0"

def draw_x(event,x,y,flags,param):                            #drawing X with the point clicked as centre
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.line(image,(x-30,y+30),(x+30,y-30),(255,0,0),3)
        cv2.line(image, (x+30, y+30), (x-30, y-30), (255, 0, 0), 3)
        index2=board_index(x,y)
        board[index2]="x"

cv2.namedWindow("Tic_Tac_Toe")

def check_win():
    if ((board[1]==board[2]==board[3]=="x") or (board[4]==board[5]==board[6]=="x") or (board[7]==board[8]==board[9]=="x") or (board[1] == board[4] == board[7] =="x") or (board[5] == board[2] == board[8] =="x") or (board[6] == board[9] == board[3] == "x") or (board[1] == board[5] == board[9] =="x") or (board[5] == board[7] == board[3] =="x")):
        print("player 2 wins ")
        return False
    elif ((board[1]==board[2]==board[3]=="0") or (board[4]==board[5]==board[6]=="0") or (board[7]==board[8]==board[9]=="0") or (board[1] == board[4] == board[7] == "0") or (board[5] == board[2] == board[8] == "0") or (board[6] == board[9] == board[3] == "0") or (board[1] == board[5] == board[9] == "0") or (board[5] == board[7] == board[3] == "0")):
        print("player 1 wins ")
        return False
    elif " " not in board:
        print("its a tie ")
        return False
    else:
        return True

def board_index(x,y):
    if 100<x<200 and 100<y<200:
        index=1
    elif 200<x<300 and 100<y<200:
        index=2
    elif 300 < x < 400 and 100 < y < 200:
        index=3
    elif 100 < x < 200 and 200 < y < 300:
        index=4
    elif 200 < x < 300 and 200 < y < 300:
        index=5
    elif 300 < x < 400 and 200 < y < 300:
        index=6
    elif 100 < x < 200 and 300 < y < 400:
        index=7
    elif 200 < x < 300 and 300 < y < 400:
        index=8
    elif 300 < x < 400 and 300 < y < 400:
        index=9
    else :
        index=0
    return index

def player_input(turn):
    if turn%2==0:
        cv2.setMouseCallback("Tic_Tac_Toe",draw_circle)
    else:
        cv2.setMouseCallback("Tic_Tac_Toe", draw_x)


count=0
while check_win():
    player_input(count)
    print(board)
    cv2.imshow("Tic_Tac_Toe", image)
    count = count + 1

    if cv2.waitKey(0) & ord("q"):
        break

cv2.destroyAllWindows()








