import pygame, sys
from Visual_And_Sound import music, setup_window

#Define which tile to use
L = 0 #LAVA
R = 1 #ROCK
F = 2 #FOREST
S = 3 #SANDYSAND

#Associating Color and Tiles
TileColour = { L : pygame.image.load("data/texture/Lava_45pix.png"),
               R : pygame.image.load("data/texture/Rock_45pix.png"),
               F : pygame.image.load("data/texture/Forest_45pix.png"),
               S : pygame.image.load("data/texture/Sand_45pix.png")
               }

#Map Creation

map1 = [[S,S,S,S,S,R,S,F,F,F,F,F,F,F],      #14*14
        [S,L,L,S,S,R,S,S,F,F,F,F,F,F],
        [S,L,L,S,S,S,S,S,F,S,F,F,F,F],
        [S,S,S,R,S,S,S,S,S,S,S,S,S,F],
        [S,S,S,S,S,S,S,S,S,S,S,S,S,S],
        [S,R,S,S,S,R,S,S,S,S,S,R,S,S],
        [S,S,S,S,S,S,R,S,S,S,S,S,S,S],
        [S,S,S,S,S,S,S,S,S,S,S,S,S,S],
        [S,S,S,S,S,S,S,S,S,S,S,S,S,S],
        [S,L,S,S,S,S,S,S,S,R,L,S,S,S],
        [S,L,L,S,S,R,S,S,L,L,L,S,S,S],
        [S,S,S,S,S,S,S,S,S,L,L,S,S,S],
        [S,R,R,S,S,S,S,S,S,S,S,S,R,S],
        [S,S,R,S,S,S,S,S,S,S,S,S,S,S],
        ]

#Map Size
TILESIZE = 45
MAPWIDTH = 14
MAPHEIGHT = 14

#Display
pygame.init()
DISPLAY = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))

#Title and Icon
setup_window()

#Music
music()

#Player
playerImg = pygame.image.load("data/texture/player2.png")
playerX = 350
playerY = 520
playerX_change = 0
playerY_change = 0
def player(x,y):
    DISPLAY.blit(playerImg, (x, y))
    
#Basic HUD
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
         #Player Movement   
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1.25
            if event.key == pygame.K_RIGHT:                
                playerX_change = 1.25
            if event.key == pygame.K_UP:                
                playerY_change = -1.25
            if event.key == pygame.K_DOWN:                
                playerY_change = 1.25
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
               playerX_change = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                playerY_change = 0
            
    for row in range(MAPHEIGHT):
        for col in range(MAPWIDTH):
            DISPLAY.blit(TileColour[map1[row][col]],(col*TILESIZE,row*TILESIZE))
            
            
    playerX += playerX_change
    playerY += playerY_change
    if playerX <=0:
        playerX = 0
    elif playerX >= 575:
        playerX = 575
    if playerY <=0:
        playerY = 0
    elif playerY >= 575:
        playerY = 575
    player(playerX, playerY)
    pygame.display.update()
    


