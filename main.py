import math
import random

import pygame
from pygame import mixer

#Initailize pygame
pygame.init()

#Creating display
screen =pygame.display.set_mode((800,600))
score=0
#background
background=pygame.image.load("background.png")
#Title and icon
pygame.display.set_caption("Space Invaders")
icon=pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

#Player
playerImg=pygame.image.load("space-invaders.png")
playerX=370
playerY=480
playerX_change=0



def player(x,y):
    screen.blit(playerImg,(x,y))

#Enemy
enemyImg =[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
num_of_enemy=6

for i in range(num_of_enemy):
    enemyImg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(4)
    enemyY_change.append(40)

def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))

#Bullet
#ready that you can't see the bullet
#fire you can see the bullet on the screen
bulletImg=pygame.image.load("bullet.png")
bulletX=0
bulletY=480
bulletX_change=0
bulletY_change=10
bullet_state="ready"

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16 , y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False

#Game loop
running =True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change=-5
            if event.key == pygame.K_RIGHT:
               playerX_change=5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX=playerX
                    fire_bullet(bulletX,bulletY)
                    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerX_change=0

    #check the boundary of player
    playerX += playerX_change
    if playerX <=0:
        playerX = 0
    elif playerX >=736:
        playerX = 736

    #Moving the enemy in the boundary
    for i in range(num_of_enemy):
        enemyX[i]+=enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i]=4
            enemyY[i]+=enemyY_change[i]
        elif enemyX[i] >=736:
            enemyX_change[i]=-4
            enemyY[i]+=enemyY_change[i]

        #collision
        collision=isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision :
            bulletY = 480
            bullet_state = "ready"
            score += 1
            enemyX[i]=random.randint(0,735)
            enemyY[i]=random.randint(50,150)

        enemy(enemyX[i],enemyY[i],i)
    
    #Bullet Movement
    if bulletY <= 0:
        bulletY=480
        bullet_state="ready"

    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change
        
    #collision
    collision=isCollision(enemyX,enemyY,bulletX,bulletY)
    if collision :
        bulletY = 480
        bullet_state = "ready"
        score += 1
        enemyX=random.randint(0,735)
        enemyY=random.randint(50,150)
    
    
    player(playerX,playerY)
    
    pygame.display.update()