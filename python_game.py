import pygame
from pygame.locals import *
"""this is tic tac toe game"""

pygame.init()

screen_width=300
screen_height=300

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Tic Tac Toe!")

#event handlers

#defining variables
line_width=5
markers=[]
clicked=False
pos=[]
players=1
winner=0
game_over=False

#defining colors
green=(0,255,0)
red=(255,0,0)
blue=(0,0,255)

#defining font
font = pygame.font.SysFont(None,40)
#create play again rectangle
again_rect=Rect(screen_width // 2 -80,screen_height // 2,160,50)


def game_grid():
    bg=(255,255,200)
    grid =(50,50,50)
    screen.fill(bg)
    for X in range(1,3):
        pygame.draw.line(screen,grid,(0,X*100),
                         (screen_width,X*100),line_width)
        pygame.draw.line(screen, grid, (X * 100,0),
                         (X * 100, screen_height),line_width)

for x in range(3):
    row=[0]*3
    markers.append(row)

print(markers)


def draw_markers():
    x_pos=0
    for x in markers:
        y_pos=0
        for y in x:
            if y==1:
                pygame.draw.line(screen,green,(x_pos*100+15,y_pos*100+15),
                                 (x_pos*100+85,y_pos*100+85),line_width)
                pygame.draw.line(screen, green, (x_pos * 100 + 15, y_pos * 100 + 85),
                                 (x_pos * 100 + 85, y_pos * 100 + 15),line_width)
            if y==-1:
                pygame.draw.circle(screen,red,(x_pos*100+50,y_pos*100+50),
                                   38,line_width)
            y_pos+=1
        x_pos+=1

def winner_check():
    global winner
    global game_over
    y_pos=0
    for x in markers:
        #check through columns
        if sum(x)==3:
            winner=1
            game_over=True
        if sum(x)==-3:
            winner=2
            game_over=True
        #check through rows
        if  markers[0][y_pos] + markers[2][y_pos]==3:
            winner=1
            game_over=True
        if  markers[0][y_pos] + markers[2][y_pos]==-3:
            winner=2
            game_over=True
        y_pos +=1
        #check cross
    if (markers[0][0]+ markers[1][1]+markers[2][2]==3 or
            markers[2][0]+ markers[1][1]+markers[0][2]==3):
        winner=1
        game_over=True

    if (markers[0][0]+ markers[1][1]+markers[2][2]==-3 or
            markers[2][0]+ markers[1][1]+markers[0][2]==-3):
        winner=2
        game_over=True

def draw_winner(winner):
    win_text=(f'player {winner} wins!')
    win_img= font.render(win_text,True,blue)
    pygame.draw.rect(screen,green,
                     (screen_width//2-100,screen_height//2-60,200,50))
    screen.blit(win_img,(screen_width//2-100,screen_height//2-50))

    again_text="Play Again?"
    again_img= font.render(again_text,True,blue)
    pygame.draw.rect(screen,green,again_rect)
    screen.blit(again_img,(screen_width // 2 -80, screen_height // 2 + 10))

run= True
while run:
    game_grid()
    draw_markers()

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            run = False
        if game_over==0:

            if event.type==pygame.MOUSEBUTTONDOWN and clicked==False:
                clicked=True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                cell_X=pos[0]
                cell_Y=pos[1]
                if markers[cell_X//100][cell_Y//100]==0:
                    markers[cell_X // 100][cell_Y // 100] = players
                    players *= -1
                    winner_check()

    if game_over==True:
        draw_winner(winner)
        #check for mouseclick tonsee if the user has clicked on playagain
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            if again_rect.collidepoint(pos):
                #reset the variables
                markers = []
                pos = []
                players = 1
                winner = 0
                game_over = False

                for x in range(3):
                    row = [0] * 3
                    markers.append(row)

    pygame.display.update()
pygame.quit()



