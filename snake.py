import pygame
import time
import random
pygame.init()
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
block=20
FPS=10
blue=(0,0,255)
game_width=800
game_height=600
gameWindow=pygame.display.set_mode((game_width,game_height))
pygame.display.set_caption("snake game")
pygame.display.update()
clk=pygame.time.Clock()
font=pygame.font.SysFont(None,30)
def snake(block,snakelist):
    for xny in snakelist:
        pygame.draw.rect(gameWindow,blue,[xny[0],xny[1],block,block])
def message_to_screen(msg,color):
    screen_text=font.render(msg,True,color)
    gameWindow.blit(screen_text,[game_width/4,game_height/2])
def loop():
    gameClose=False
    block1=10
    gameOver=False
    start_x=game_width/2
    start_y=game_height/2
    update_x=0
    update_y=0
    rApplex=int(round(random.randrange(0,game_width-block)/20.0)*20.0)
    rAppley=int(round(random.randrange(0,game_height-block)/20.0)*20.0)
    snakeList=[]
    snakeLength=1
    while not gameClose:
        while gameOver==True:
            gameWindow.fill(white)
            message_to_screen("you loose !!!!! press r to reply or q to quit",red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        gameClose=True
                        gameOver=False
                    if event.key==pygame.K_r:
                        loop()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameClose=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    update_x=-block
                    update_y=0
                if event.key==pygame.K_RIGHT:
                    update_x=+block
                    update_y=0
                if event.key==pygame.K_UP:
                    update_y=-block
                    update_x=0
                if event.key==pygame.K_DOWN:
                    update_y=+block
                    update_x=0
        if start_x>=game_width or start_x<=0 or start_y<=0 or start_y>=game_height:
            gameOver=True
        start_x+=update_x
        start_y+=update_y
        gameWindow.fill(green)
        pygame.draw.circle(gameWindow,red,[rApplex,rAppley],block1)
       # pygame.draw.rect(gameWindow,blue,[start_x,start_y,block,block])


        snakeHead=[]
        snakeHead.append(start_x)
        snakeHead.append(start_y)
        snakeList.append(snakeHead)
        if len(snakeList)>snakeLength:
            del (snakeList[0])
        for i in snakeList[:-1]:
            if i==snakeHead:
                gameOver=True



                
        snake(block,snakeList)
        pygame.display.update()
        if start_x==rApplex and start_y==rAppley:
            rApplex=int(round(random.randrange(0,game_width-block)/20.0)*20.0)
            rAppley=int(round(random.randrange(0,game_height-block)/20.0)*20.0)
            snakeLength+=1
        clk.tick(FPS)
    #time.sleep(5)
    pygame.quit()
    quit()
loop()
