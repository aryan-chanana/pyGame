import pygame
import random
from pygame import *

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('E:\\Temp. Folder\\Programming\\Python\\Pygame space\\ufo.png')
pygame.display.set_icon(icon)
background = pygame.image.load('E:\\Temp. Folder\\Programming\\Python\\Pygame space\\background.png')

playerImage = pygame.image.load('E:\\Temp. Folder\\Programming\\Python\\Pygame space\\astronomy.png')
playerX = 370
playerY = 480
playerX_change = 0

enemyImage = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
no_of_enemies = 6
for i in range(no_of_enemies):
    enemyImage.append(pygame.image.load('E:\\Temp. Folder\\Programming\\Python\\Pygame space\\monster.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(30,130))
    enemyX_change.append(5)
    enemyY_change.append(40)

bulletImage = pygame.image.load('E:\\Temp. Folder\\Programming\\Python\\Pygame space\\bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 5
bullet_state = True
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
over_font = pygame.font.Font('freesansbold.ttf',64)
textX = 10
textY = 10

def show_score(x,y):
    score = font.render("Score: " + str(score_value), True, (255,255,255))
    screen.blit(score, (x,y))

def game_over():
    over = over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(over, (200,250))

def player(x,y):
    screen.blit(playerImage, (x,y))

def enemy(x,y,i):
    screen.blit(enemyImage[i], (x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = False
    screen.blit(bulletImage, (x+16,y+10))

def iscollision(bulletX,bulletY,enemyX,enemyY):
    distance = ((enemyX-bulletX)**2 + (enemyY-bulletY)**2)**0.5
    if distance < 27:
        return True
    else:
        return False

running = True
while running:

    screen.fill((0,0,0))
    screen.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change -= 7
            if event.key == pygame.K_RIGHT:
                playerX_change += 7
            if event.key == pygame.K_SPACE:
                if bullet_state:
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0




    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736

    for i in range(no_of_enemies):
        
        if enemyY[i] > 440:
            for j in range(no_of_enemies):
                enemyY[j] = 2000
            game_over()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -5
            enemyY[i] += enemyY_change[i]

        collision = iscollision(bulletX,bulletY,enemyX[i],enemyY[i])
        if collision:
            bulletY = 480
            bullet_state = True
            enemyX[i] = random.randint(0,735)
            enemyY[i] = random.randint(30,130)
            score_value += 1
        
        enemy(enemyX[i],enemyY[i],i)

    

    if bulletY <= 0:
        bulletY = 480
        bullet_state = True

    if bullet_state == False:
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change

    

    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()