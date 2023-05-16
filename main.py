import pygame,sys
#pygame setup
clock=pygame.time.Clock()                           #game clock
pygame.init()
running=True
WindowSize=(400,400)
WindowName=pygame.display.set_caption('game')
# WindowLogo=pygame.display.set_icon()
screen=pygame.display.set_mode(WindowSize,0,32)
playerimage=pygame.image.load('1.png')
movingRight=False
movingLeft=False
playerLocation=[50,50]
playerYmomentum=0
#main loop
while running:        
    screen.fill((0,0,0))
    screen.blit(playerimage,playerLocation)                              #game loop    
    #movement thing
    if movingRight==True:  
        playerLocation[0]+=4
    if movingLeft==True: 
        playerLocation[0]-=4
    
    #falling down thing
    if playerLocation[1]>WindowSize[1]-playerimage.get_height():
        playerYmomentum=-playerYmomentum
    if playerLocation[1]<WindowSize[1]-playerimage.get_height():
        playerYmomentum+=1
    playerLocation[1]+=playerYmomentum

    #event loop    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()                           #stop pygame
            sys.exit()                              #quits the script
        
        #keyevent
        if event.type==pygame.KEYUP:                #keyup(keypress is falce)
            if event.key==pygame.K_RIGHT:
                movingRight=False
            if event.key==pygame.K_LEFT:
                movingLeft=False
        if event.type==pygame.KEYDOWN:              #keydown(keypress is true)
            if event.key==pygame.K_RIGHT:
                movingRight=True
            if event.key==pygame.K_LEFT:
                movingLeft=True
    clock.tick(60)
    pygame.display.update()
