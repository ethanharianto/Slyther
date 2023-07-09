#Imports pygame module, then initializes it
#PyGame module is a quintessential module to create a game for Python, allowing for drawings/creations on the screen 
import pygame
pygame.init()

#Imports random module, which will be utitilized to randomize distance of treat from snake
import random

#Directions for the player
print('Use the arrow keys to navigate the game!')

#Difficulty dictates how big of a field the Snake game will have
#The harder, the smaller the field
difficulty = input(str('How difficult would you like the game? \n easy\n medium\n hard\n'))

#If answer to initial question is not valid answer, the question of difficulty is asked again
while difficulty != 'easy' and difficulty != 'medium' and difficulty != 'hard':
  print('Invalid Input.')
  difficulty = input(str('How difficult would you like the game? \n easy\n medium\n hard \n'))

#A variable named size is created which dictates how big the display screen will be (it will be dictated by the difficulty)
#The variable will be comprised of width and height subvariables which will be used later
if difficulty == 'easy':
  size = width, height = (750, 400)
  winlength = 10
elif difficulty == 'medium':
  size = width, height = (500,400)
  winlength = 20
elif difficulty == 'hard':
  size = width, height = (300,300)
  winlength = 30

#The screen size is set through the size variable
screen=pygame.display.set_mode(size)

# The name of the game is set as the caption
# A homage to Harry Potter's Slytherin house, SLYTHER is the name of this snake game
pygame.display.set_caption('SLYTHER')

# Display will show
pygame.display.update()

# Creates clock for game
clock = pygame.time.Clock()

# Creates variables which will dictate when game ends
win = 'False'
loss = 'False'

# These variables count the outcomes of the games played
wins = 0
losses = 0

# Initial position of the snake is set to the middle of the game display
x = width/2
y = height/2

# Initial length of the snake is set
length = 1

# The eat variable dictates whether or not the snake has eaten or not, meaning can it expand or not
eat = 'False'

# A list of the x,y coordinates needed for the snake
list = []

# The direction in which the snake is facing
# Ex. left, right, up, down
direction = ''

# This position function dictates the position of the snake by adding/subtracting from its x and y positions
# The first list will be the container of the values put into the second list, allowing both the x and y values to be input in one position on the list
def position(cx,cy,d):
# This statement is needed so that the function uses global variables instead of local variables
 global x,y,direction,list,list2

# list 2 is set as an empty container 
 list2 = []

# The x and y variables are changed as needed 
 x += cx
 y += cy

# The x and y values are added to list2
 list2.append(x)
 list2.append(y)

# list 2, composed of the x and y values, is added to list so that x and y are in a single position
 list.append(list2)

# The direction that the snake is going is set 
 direction = d

# This statement is necessary so that the snake does not exceed its set length
 while len(list) > length:
   del list[0]

# This function kicks in when thre is no input from the user
# The snake will continue in the direction of the previous key pressed
def changedirection():
# The global direction is called
 global direction

# Using the position function and the direction variable, the snake will continue in the specified direction
 if direction == 'left':
  position (-10,0,'left')
 elif direction == 'right':
  position (10,0,'right')
 elif direction == 'up':
  position (0,-10,'up')
 elif direction == 'down':
  position (0,10,'down')

# This function creates the food that the snake eats in order to extend
def food():
# global variables are called 
 global eat, sx, sy

# Function will not kick in unless eat is false  
 if eat == 'False':

# sx and sy will be the values of the food's x and y values
  sx = x + random.randint(-100,100)
  sy = y + random.randint(-100,100)

# If the food spawns outside of the game's parameters, the x and/or y values are manipulated so that it is not
  if sx > width:
   sx = width - 10
  if sx < 0:
   sx = 10
  if sy > height:
   sy = height - 10
  if sy < 0:
   sy = 10

# screen filled with grey before food is drawn
 screen.fill((64,64,64))
 pygame.draw.rect(screen,(255,255,255),(sx,sy,10,10))

# eat is set to true until food is eaten again
 eat = 'True'

# This function draws the game board as necessary
def drawgame():
# The global variables list and loss are called
 global list, loss

# screen is filled with grey 
 screen.fill((64,64,64))

# food is drawn
 pygame.draw.rect(screen,(255,255,255),(sx,sy,10,10))

# snake head is drawn  
 pygame.draw.rect(screen,(0,255,0),(x,y,10,10))
  
# for each position in the list, a snake part is drawn  
 for i in list:
   pygame.draw.rect(screen,(0,255,0),(i[0],i[1],10,10))

# If the snake head touches any part of the snake, the game is lost  
 for i in list[:-1]:
   if i == list2:
    loss = 'True'
     
# display is updated with the new pieces
 pygame.display.update()     
     
# Game loop function
def game():
# global variables are called 
 global loss,win,length,eat,losses, wins,x,y,direction,list

# If game is neither lost nor won, game continues  
 while loss != 'True' and win != 'True':
  food()

# Snake goes in the same direction it did before in the case of no input   
  if direction == direction:
   changedirection()
   drawgame()

# 15 ticks added to clock    
   clock.tick(15)

# Using keyboard inputs the snake's position will be changed using the position function
# The direction will also be set in the case of no input after an initial input
  for i in pygame.event.get():
   if i.type == pygame.KEYDOWN:
    if i.key == pygame.K_LEFT:
     position(-10,0,'left')
    elif i.key == pygame.K_RIGHT:
     position(10,0,'right')
    elif i.key == pygame.K_UP:
     position(0,-10,'up')
    elif i.key == pygame.K_DOWN:
     position(0,10,'down')
  drawgame()
# If the snakehead is within a 5 pixel radius of the food's center, it will expand
  if abs(x-sx) <= 5 and abs(y-sy) <= 5:
   length += 1
   print('Chomp!')
   screen.fill((64,64,64))
   eat = 'False'
   food()

# If the snake exits the game's domain, the game will be lost
  if x > width or x < 0 or y > height or y < 0:
    loss = 'True'
    losses += 1
# If the snake reaches the winlengthof the difficulty, the game will be won
  if length == winlength:
    win = 'True'
    wins += 1
  clock.tick(15)
# When the game is over, the game will tell you your score and ask if you would like to play again
 print('You had a score of ' + str(length-1) + '.')
 play = input('Would you like to play again?\n' 'yes\nno\n')
# the game will reset then loop until the player does not want to play anymore
 if play == 'yes':
   loss = 'False'
   win = 'False'
   x = width/2
   y = height/2
   direction = ''
   length = 1
   list = []
   game()

# The game will tell you how many losses and wins the player has after they do not want to play anymore
 else:
   if losses != 1 and wins != 1:
    print('You had ' + str(losses) + ' losses and ' + str(wins) + ' wins.')
   if losses != 1 and wins == 1:
    print('You had ' + str(losses) + ' losses and ' + str(wins) + ' win.') 
   if losses == 1 and wins == 1:
    print('You had ' + str(losses) + ' loss and ' + str(wins) + ' win.')
   if losses == 1 and wins != 1:
    print('You had ' + str(losses) + ' loss and ' + str(wins) + ' wins.')

# The gameloop starts
game()

# The game is quit
pygame.quit()
quit()