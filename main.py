#importing of modules and shit
import pygame,sys

#pygame setup
pygame.init()

#image loading shit
WindowLogo=pygame.image.load('./assets/1.png')
playerimage=pygame.image.load('./assets/player.png')
tile1=pygame.image.load('./assets/tile1.png')
tile2=pygame.image.load('./assets/tile2.png')


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

playerYmomentum=0
airTimer=0

tiledim=tile1.get_height()
playerrect=pygame.Rect(50,50,playerimage.get_width(),playerimage.get_height())

tilemap=[
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['0','0','0','0','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['1','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
        ['2','2','1','0','0','0','0','1','1','0','0','0','0','0','0','0','0','0','0',],
        ['2','2','2','1','1','1','1','2','2','1','1','1','1','1','1','1','1','1','1',],
        ['2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2',],
        ['2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2',],
        ['2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2',],
        ['2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2',],
        ['2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2',]
]

def collisionTest(rect,tiles):
    hitlist=[]
    for tile in tiles :
        if rect.colliderect(tile):
            hitlist.append(tile)
    return hitlist

def move(rect,movement,tiles):
    collision_types={'top':False,'bottom':False,'right':False,'left':False}
    rect.x+=movement[0]
    hitlist=collisionTest(rect,tiles)
    for tile in hitlist:
        if movement[0]>0:
            rect.right=tile.left
            collision_types['right']=True
        if movement[0]<0:
            rect.left=tile.right
            collision_types['left']=True
    rect.y+=movement[1]
    hitlist=collisionTest(rect,tiles)
    for tile in hitlist:
        if movement[1]>0:
            rect.bottom=tile.top
            collision_types['bottom']=True
        if movement[1]<0:
            rect.top=tile.bottom
            collision_types['top']=True
    return rect, collision_types

#main loop
while running:        
    display.fill((0,0,0))
    
    tilerect=[]

    y=0
    for row in tilemap:
        x=0
        for tile in row:
            if tile=='1':
                display.blit(tile1,(x*tiledim,y*tiledim))
            if tile=='2':
                display.blit(tile2,(x*tiledim,y*tiledim))
            if tile!='0':
                tilerect.append(pygame.Rect(x*tiledim,y*tiledim,tiledim,tiledim))
            x+=1
        y+=1


    playerMovement=[0,0]
    if movingRight==True:
        playerMovement[0]+=2
    if movingLeft==True:
        playerMovement[0]-=2
    playerMovement[1]+=playerYmomentum
    playerYmomentum+=0.2
    if playerYmomentum>3:
        playerYmomentum=3

    playerrect,collisions=move(playerrect,playerMovement,tilerect)
    if collisions['bottom'] or collisions['top']:
        playerYmomentum=0
        airTimer=0
    else:
        airTimer+=1
    
    display.blit(playerimage,(playerrect.x,playerrect.y))    

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
            if event.key==pygame.K_UP:
                if airTimer<6:
                    playerYmomentum=-5
            if event.key==pygame.K_DOWN:
                playerYmomentum=10
    
    window.blit(pygame.transform.scale(display,WindowSize),(0,0))
    pygame.display.set_icon(WindowLogo)
    pygame.display.update()
    clock.tick(60)
