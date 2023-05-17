#importing of modules and shit
import pygame,sys

#pygame setup
pygame.init()

#image loading shit
WindowLogo=pygame.image.load('./assets/1.png')
playerimage=pygame.image.load('./assets/player.png')

#initializations
clock=pygame.time.Clock()                           #game clock
WindowName=pygame.display.set_caption('game')
running=True
WindowSize=(600,400)
displaySize=(300,200)
window=pygame.display.set_mode(WindowSize,0,32)
display=pygame.Surface(displaySize)

movingRight=False
movingLeft=False
playerLocation=[50,50]
playerYmomentum=0

tilemap=[
        [],
        [],
        [],
        []
]

#main loop
while running:        
    display.fill((0,0,0))
    display.blit(playerimage,playerLocation)                              #game loop    
    
    #movement thing
    if movingRight==True:  
        playerLocation[0]+=4
    if movingLeft==True: 
        playerLocation[0]-=4
    
    # #falling down thing
    # if playerLocation[1]>WindowSize[1]-playerimage.get_height():
    #     playerYmomentum=-playerYmomentum
    # if playerLocation[1]<WindowSize[1]-playerimage.get_height():
    #     playerYmomentum+=1
    # playerLocation[1]+=playerYmomentum

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
    
    window.blit(pygame.transform.scale(display,WindowSize),(0,0))
    pygame.display.set_icon(WindowLogo)
    pygame.display.update()
    clock.tick(60)
