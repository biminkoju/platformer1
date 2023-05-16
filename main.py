import pygame,sys
#pygame setup
clock=pygame.time.Clock()                           #game clock
pygame.init()
running=True
WindowSize=(400,400)
WindowName=pygame.display.set_caption('game')
# WindowLogo=pygame.display.set_icon()
screen=pygame.display.set_mode(WindowSize,0,32)

#main loop

while running:                                      #game loop    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    clock.tick(60)
    pygame.display.update()
