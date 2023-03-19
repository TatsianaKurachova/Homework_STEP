import pygame
import random
import math
import time
 
from display import * 
from player import *
from enemy import *
from bullet import *

pygame.init()

display = pygame.display.set_mode((display_width,
                                  display_height))
display_icon = pygame.image.load("image/alien.png")
pygame.display.set_icon(display_icon)
bg_img = pygame.image.load("image/background.png")  
pygame.display.set_caption("Welcome to Space")
clock = pygame.time.Clock()

score_val = 0
score_x = 5
score_y = 5
font = pygame.font.Font('freesansbold.ttf', 20)
 
game_over_font = pygame.font.Font('freesansbold.ttf', 64)
  
def show_score(x, y):
    score = font.render("Points: " + str(score_val),
                        True, white)
    display.blit(score, (x , y ))
 
def game_over():
    game_over_text = game_over_font.render("GAME OVER",
                                           True, white)
    display.blit(game_over_text, (190, 250))
 
 
playerImage = pygame.image.load('image/spaceship.png')
  
for num in range(no_of_enemys):
    enemyImage.append(pygame.image.load('image/enemy.png'))
    enemy_x.append(random.randint(64, 737))
    enemy_y.append(random.randint(30, 180))
    enemy_x_change.append(1.2)
    enemy_y_change.append(50)
  
bulletImage = pygame.image.load('image/bullet.png')
 
def isCollision(x1, x2, y1, y2):
    distance = math.sqrt((math.pow(x1 - x2,2)) +
                         (math.pow(y1 - y2,2)))
    if distance <= 50:
        return True
    else:
        return False
 
def player(x, y):
    display.blit(playerImage, (x - 16, y + 10))
 
def enemy(x, y, i):
    display.blit(enemyImage[i], (x, y))
 
def bullet(x, y):
    global bullet_state
    display.blit(bulletImage, (x, y))
    bullet_state = "fire"
 
 
running = True
while running:
 
    display.fill((0, 0, 0))
    display.blit(bg_img, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -2
            if event.key == pygame.K_RIGHT:
                player_x_change = 2
            if event.key == pygame.K_SPACE:
               
 
                if bullet_state == "rest":
                    bullet_x = player_x
                    bullet(bullet_x, bullet_y)
 
        if event.type == pygame.KEYUP:
            player_x_change = 0
 
    player_x += player_x_change
    for i in range(no_of_enemys):
        enemy_x[i] += enemy_x_change[i]
 
 
    if bullet_y <= 0:
        bullet_y = 600
        bullet_state = "rest"
    if bullet_state == "fire":
        bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change
 
    for i in range(no_of_enemys):
        if enemy_y[i] >= 450:
            if abs(player_x-enemy_x[i]) < 80:
                for j in range(no_of_enemys):
                    enemy_y[j] = 2000
 
                game_over()
                break
 
        if enemy_x[i] >= 735 or enemy_x[i] <= 0:
            enemy_x_change[i] *= -1
            enemy_y[i] += enemy_y_change[i]

        # Collision
        collision = isCollision(bullet_x, enemy_x[i],
                                bullet_y, enemy_y[i])
        if collision:
            score_val += 1
            bullet_y = 600
            bullet_state = "rest"
            enemy_x[i] = random.randint(64, 736)
            enemy_y[i] = random.randint(30, 200)
            enemy_x_change[i] *= -1
 
        enemy(enemy_x[i], enemy_y[i], i)
 
 
    if player_x <= 16:
        player_x = 16
    elif player_x >= 750:
        player_x = 750
 
 
    player(player_x, player_y)
    show_score(score_x, score_y)
    pygame.display.update()
