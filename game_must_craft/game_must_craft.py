#The aim of this game is to get the woman (player character) to reach the craft supplies (prize character).
#If the woman touches the housework (enemy characters) the user loses the game.

#First, we import the pygame and random modules.
#This will allow us to use the pygame functions and use random numbers.
import pygame
import random

#This code initialises the game.
pygame.init()

#This code creates the screen for our game to appear in.
#We set the width and height of the screen in pixels.
screen_width = 1080
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

#This code will set the name of the game in the window.
pygame.display.set_caption("Must Craft")

#This code imports the images for each of the characters in the game.
player = pygame.image.load("player_forward.png")
enemy1 = pygame.image.load("enemy1.png")
enemy2 = pygame.image.load("enemy2.png")
enemy3 = pygame.image.load("enemy3.png")
prize = pygame.image.load("prize.png")

#This code will get the width and height of each of the images for the different characters.
player_height = player.get_height()
player_width = player.get_width()

enemy1_height = enemy1.get_height()
enemy1_width = enemy1.get_width()

enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()

enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()

prize_height = prize.get_height()
prize_width = prize.get_width()

#This code positions the characters on the screen.
#Some of the characters will be positioned randomly within the screen.
#The positions are set so that the enemy and prize characters do not collide with the player character immediately once the game begins.
playerXPosition = 100
playerYPosition = 50

enemy1XPosition =  screen_width
enemy1YPosition =  random.randint(0, screen_height - enemy1_height)

enemy2XPosition =  0
enemy2YPosition =  random.randint(1 + player_height, screen_height - enemy2_height)

enemy3XPosition =  screen_width
enemy3YPosition =  random.randint(0, screen_height - enemy3_height)

prizeXPosition =  random.randint(1 + player_width, screen_width - prize_width)
prizeYPosition =  random.randint(1 + player_height, screen_height - prize_height)

#This initialises the key movement variables.
keyUp = False
keyDown = False
keyRight = False
keyLeft = False

#This is the main loop for the game.

while 1:

    #This fills the screen. The colour is currently set to white.
    screen.fill((255, 255, 255)) 

    #This draws the character images to the screen at the postion specfied. I.e. (100, 50).
    screen.blit(player, (playerXPosition, playerYPosition))
    screen.blit(enemy1, (enemy1XPosition, enemy1YPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))

    #This updates the screen.
    pygame.display.flip()
    
    #This code will exit the game if the user quits.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
            
        #This code checks if the directional keys have been pressed or released.        
        if event.type == pygame.KEYDOWN:
        
            if event.key == pygame.K_UP:
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
                player = pygame.image.load("player_forward.png") #If the player character moves right, the image will face to the right.
            if event.key == pygame.K_LEFT:
                keyLeft = True
                player = pygame.image.load("player_backward.png") #If the player character moves left, the image will face to the left.
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
    
    #If the movement variables are True, the position of the player character will move.
    if keyUp == True:
        if playerYPosition > 0 :
            playerYPosition -= 1
            
    if keyDown == True:
        if playerYPosition < screen_height - player_height:
            playerYPosition += 1
            
    if keyRight == True:
        if playerXPosition > 0 :
            playerXPosition += 1
            
    if keyLeft == True:
        if playerXPosition < screen_width - player_width:
            playerXPosition -= 1  
            
    #This code creates a bounding box for each character
    #and updates its position as the character moves.
    playerBox = pygame.Rect(player.get_rect())
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    enemy1Box = pygame.Rect(enemy1.get_rect())
    enemy1Box.top = enemy1YPosition
    enemy1Box.left = enemy1XPosition
    
    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition
    
    enemy3Box = pygame.Rect(enemy3.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition
    
    prizeBox = pygame.Rect(prize.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition
        
    #This code tells the user they have lost if the player character collides with an enemy character.
    #The game will then exit.
    if playerBox.colliderect(enemy1Box) or playerBox.colliderect(enemy2Box) or playerBox.colliderect(enemy3Box): 
        print("You lose!")
        pygame.quit()
        exit(0)
    
    #This code tells the user they have one if the player character collides with the prize.
    #The game will then exit.
    if playerBox.colliderect(prizeBox):
        print("You win!")
        pygame.quit()
        exit(0)
        
    #This makes the enemy characters move across the screen.
    enemy1XPosition -= 0.15
    enemy2XPosition += 0.15
    enemy3XPosition -= 0.15
