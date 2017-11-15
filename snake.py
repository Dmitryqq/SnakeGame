import pygame,sys,random
from pygame.locals import*
from gamelogic import*
from colors import*

UP=1
DOWN=2
LEFT=3
RIGHT=4
    
def MainLoop():
    Move=RIGHT
    anim=0
    angle=0
    count=0
    done = True
    GameOver = False
    tail=[]
    head = Sprite(WIDTH//2*BLOCK_SIZE,HEIGHT//2*BLOCK_SIZE,'snake.png')
    apple = Sprite(random.randint(1,WIDTH)*BLOCK_SIZE,random.randint(1,HEIGHT)*BLOCK_SIZE,'apple.png')
    x=30
    for i in range(4):
        tail.append(i)
        tail[i] = Sprite(WIDTH//2*BLOCK_SIZE-x,HEIGHT//2*BLOCK_SIZE,'tail_part.png')
        x+=30
    TailUpdate(tail,head)
    while done:
        if GameOver==False:
            for e in pygame.event.get():
                 if e.type==QUIT or (e.type==pygame.KEYDOWN and e.key==K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                 if e.type==pygame.KEYDOWN:
                     if e.key==K_DOWN and Move!=UP:
                         Move=DOWN
                         angle=270
                     if e.key==K_UP and Move!=DOWN:
                         Move=UP
                         angle=90
                     if e.key==K_RIGHT and Move!=LEFT:
                         Move=RIGHT
                         angle=0
                     if e.key==K_LEFT and Move!=RIGHT:
                         Move=LEFT
                         angle=180
            #print(head.x,head.y,apple.x,apple.y,anim)
            screen.fill(BLACK)
            wormMove(Move, head)
            if anim<6:
                if anim==1:
                    apple.x+=5
                    apple.y+=5
                apple.bitmap=pygame.image.load('apple2.png')
            elif anim>=6 and anim<=12:
                if anim==6:
                    apple.x-=5
                    apple.y-=5
                apple.bitmap=pygame.image.load('apple.png')
            else:
                anim=0
            anim+=1
            if intersect(head.x,head.y,apple.x,apple.y):
                count+=1
                apple.x=int(random.randint(1,WIDTH)*BLOCK_SIZE)
                apple.y=int(random.randint(1,HEIGHT)*BLOCK_SIZE)
                tail.append(len(tail))
                tail[len(tail)-1]=Sprite(tail[len(tail)-2].x,tail[len(tail)-2].y,'tail_part.png')
                
            pygame.time.Clock().tick(8)
            head.bitmap=pygame.transform.rotate(pygame.image.load('snake.png'),angle)
            apple.render()
            head.render()
            if head.x>WIDTH*BLOCK_SIZE:head.x=BLOCK_SIZE
            if head.x<BLOCK_SIZE:head.x=WIDTH*BLOCK_SIZE
            if head.y>HEIGHT*BLOCK_SIZE:head.y=BLOCK_SIZE
            if head.y<BLOCK_SIZE:head.y=HEIGHT*BLOCK_SIZE
            for part in tail:
                part.render()
            GameOver=IsGameOver(tail,head)
            TailUpdate(tail,head)            
            drawWalls(screen)
            window.blit(screen,(0,0))
            pygame.display.flip()
            pygame.time.wait(10)
        else:
            for e in pygame.event.get():
                 if e.type==QUIT or (e.type==pygame.KEYDOWN and e.key==K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                 if e.type==pygame.KEYDOWN:
                     if e.key==K_r:
                         MainLoop()
            screen.fill(WHITE)
            Text=font.render("GAME OVER",True,BLACK)
            screen.blit(Text,(WIDTH,HEIGHT))
            Text=font.render("Score: " + str(count), True, BLACK)
            screen.blit(Text,(WIDTH,HEIGHT+100))
            Text=font2.render('"R" to play again',True,BLACK)
            screen.blit(Text,(WIDTH,HEIGHT+200))
            Text=font2.render('"ESC" to quit',True,BLACK)
            screen.blit(Text,(WIDTH,HEIGHT+270))
            window.blit(screen,(0,0))
            pygame.display.flip()
            pygame.time.wait(10)
MainLoop()
