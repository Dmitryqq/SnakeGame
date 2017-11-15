import pygame,sys,random
from pygame.locals import*
from colors import*

WIDTH = 25
HEIGHT = 25
BLOCK_SIZE = 30
window = pygame.display.set_mode(((WIDTH+2)*BLOCK_SIZE,(HEIGHT+2)*BLOCK_SIZE))
screen = pygame.display.set_mode(((WIDTH+2)*BLOCK_SIZE,(HEIGHT+2)*BLOCK_SIZE))
pygame.display.set_caption("SnakeGame") 
wallblock = pygame.Surface((BLOCK_SIZE,BLOCK_SIZE))
wallblock.set_alpha(255)
wallblock.fill(BLUE)
wallblockdark = pygame.Surface((BLOCK_SIZE-10,BLOCK_SIZE-10))
wallblockdark.set_alpha(255)
wallblockdark.fill(DARKGRAY)

pygame.font.init()
pygame.init()
font = pygame.font.SysFont('Clear Sans', 100)
font2 = pygame.font.SysFont('Clear Sans', 50)

class Sprite:
    def __init__(self,xpos,ypos,filename):
        self.x=xpos
        self.y=ypos
        self.bitmap=pygame.image.load(filename)
        self.bitmap.set_colorkey((0,0,0))
    def render(self):
        screen.blit(self.bitmap,(self.x,self.y))

def drawWalls(surface):
	for y in range(HEIGHT+1):
		surface.blit(wallblock,(0,y*BLOCK_SIZE))
		surface.blit(wallblockdark,(5,y*BLOCK_SIZE+5))
		surface.blit(wallblock,((WIDTH+1)*BLOCK_SIZE,y*BLOCK_SIZE))
		surface.blit(wallblockdark,((WIDTH+1)*BLOCK_SIZE+5,y*BLOCK_SIZE+5))
	for x in range(WIDTH+2):
		surface.blit(wallblock,(x*BLOCK_SIZE,0))
		surface.blit(wallblockdark,(x*BLOCK_SIZE+5,5))
		surface.blit(wallblock,(x*BLOCK_SIZE,(HEIGHT+1)*BLOCK_SIZE,))
		surface.blit(wallblockdark,(x*BLOCK_SIZE+5,(HEIGHT+1)*BLOCK_SIZE+5))

def intersect(worm_x,worm_y,apple_x,apple_y):
    if((worm_x>apple_x-30) and (worm_x<apple_x+30) and (worm_y>apple_y-30) and (worm_y<apple_y+30)):
       return 1
    else:
       return 0

def wormMove(Move, head):
    if Move==1:
        head.y-=BLOCK_SIZE
    elif Move==2:
        head.y+=BLOCK_SIZE
    elif Move==3:
        head.x-=BLOCK_SIZE
    else:
        head.x+=BLOCK_SIZE
    
def TailUpdate(tail,head):
    i=1
    for i in range(len(tail)):
        tail[i-1].x,tail[i-1].y = tail[i].x,tail[i].y
    tail[0].x,tail[0].y = head.x,head.y

def IsGameOver(tail,head):
    Over=False
    i=1
    for i in range(len(tail)):
        if (head.x == tail[i].x and head.y == tail[i].y):
            Over=True
    return Over
