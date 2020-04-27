import pygame
from pygame.locals import *
import random
import time
scores = []
pygame.init()
file = open('highscorer.txt', 'a')
readfile =  open('highscorer.txt')
for i in readfile:
	i = int(i.replace('\n',''))
	scores.append(i)

scores.sort(reverse=True)
print(scores[0])

bge = pygame.image.load('mr.png')
end = pygame.image.load('end.png')
font = pygame.font.SysFont('Comic Sans MS',30)
#font = pygame.font.SysFont('Lucida',30)
black = [0,0,0]
def scoreboard(msg, color):
    text = font.render("YOUR SCORE = "+str(msg), True,color)
    display.blit(text, [100,80])

def scoreboard2(msg1, msg, color):
    text = font.render(msg1 +str(msg), True,color)
    display.blit(text, [500,80])


def scoreboard3(msg, color):
    text = font.render(str(msg), True,color)
    display.blit(text, [500,300])
clock = pygame.time.Clock()
pygame.mixer.music.load('pluck.wav')
m = pygame.mouse.get_pos()
'''colors'''
black =[0,0,0]
red = [255,0,0]
white=[255,255,255]
green = [0,255,0]
displayW = 600
displayH = 800
pygame.display.set_caption('flappy cop')
display = pygame.display.set_mode((displayH,displayW))


def gameloop():
    foodcordinatechange = 3
    change = 0.2
    gameover = False
    score = 0
    cop = pygame.image.load('cop.png').convert_alpha()
    bg = pygame.image.load('gasa.png')
    leadx = displayH / 1.1
    leady = displayW / 1.8
    bawasir = round(int(leady + 125))
    foodcordinate = 0
    randomfoodcordinate = random.randrange(100, 400)
    box = pygame.image.load('box.png')

    game_going = True

    food = pygame.image.load('Untitled.png')
    foody = random.randrange(foodcordinate, 400)
    foodx = random.randrange(displayW - randomfoodcordinate, 700)
    leadxChange = 0
    m = pygame.mouse.get_pos()
    lifepoint = 0
	
    while game_going:
        life = int(score // 25) + lifepoint
        for event in pygame.event.get():
            m = pygame.mouse.get_pos()
            if event.type == QUIT:
                game_going = False
            if event.type == KEYDOWN:
                if event.key == K_UP:

                    leadxChange = -0.8
                if event.key == K_SPACE:
                    leadxChange = 0
                if event.key == K_DOWN:

                    leadxChange = 1.6
            if event.type == MOUSEBUTTONDOWN:
                if event.button == BUTTON_LEFT:
                    leadxChange = -0.8
                if event.button == BUTTON_RIGHT:
                    leadxChange = 1.6
            if event.type == MOUSEBUTTONUP:
                    leady -=20
            if event.type == KEYUP:
                    leady -=20

        #leady += 0.3
        foodx += foodcordinatechange/3
        foodcordinate += foodcordinatechange
        display.fill(black)
        #display.blit(bg, [0,0])
        display.fill(red,rect=[leadx, leady, 20, 20])
        display.fill(red,rect=[foodcordinate,600-randomfoodcordinate,80,randomfoodcordinate])
      
    #    display.fill(red,rect=[foodcordinate,0,80,randomfoodcordinate])
        display.fill(red,rect=[10,10,800,10])
        display.fill(red,rect=[790,590,800,600])
        display.fill(red,rect=[foodx,foody,20,20])

        if foodcordinate >= 1200:
            #foodcordinate = random.randrange(0,bawasir)
            randomfoodcordinate = random.randrange(100, 500)
            foodcordinate = 0

       # display.blit(bge, [0, 0])
        display.blit(cop,[leadx,leady])
        display.blit(box, [foodcordinate,600-randomfoodcordinate])
      #  display.blit(box,[foodcordinate,0])
        display.blit(food,[foodx,foody])
        scoreboard(score,green)
       # scoreboard2('Highscore = ', scores[0], green)
        leadx = m[0] +50
        leady = m[1] +50
        if leadx > foodcordinate and leadx < foodcordinate + 80:
            if leady > 600 - randomfoodcordinate and leady < 600:


                if life <= 0:
                    time.sleep(1)
                    file.write(str(score) + '\n')
                    print(scores)
                    gameover = True
                else:
                    lifepoint -= 1
                    foodcordinate = 700
                    time.sleep(2)
                  # leady = 600 - randomfoodcordinate - 50




        while gameover == True:
        	#file.write(str(score))
            display.fill(black)
          #  m = pygame.mouse.get_pos()
            scoreboard(str(score),red)
            scoreboard2('Highscore = ', scores[0], green)
            display.blit(end,[displayH/4,displayW/4])

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN :
                	
                    if event.key == K_c:

                        gameloop()
                    if event.key == K_q:
                        game_going = False
                        pygame.quit()
                        quit()
                    else:

                        game_going = True
                        gameloop()
               



        if leadx > foodx and foodx +20 >leadx or foodx > leadx and leadx +20>foodx:
            if leady > foody and foody+20>leady:
                pygame.mixer.music.play(1)
                foody = random.randrange(0, 400)
                foodx = random.randrange(displayW - randomfoodcordinate, 600)
                score +=5
                change -=0.1
                foodcordinatechange +=0.1

        if foodx >= 800:
            foody = random.randrange(0, 400)
            foodx = random.randrange(displayW - randomfoodcordinate, 600)
        if leady >= 590 or leady<=10:
            if life <= 0:
                gameover = True
            else:
               # leady = 600 - randomfoodcordinate - 50
               time.sleep(2)
               lifepoint -= 1
        if leady <10 or leady>=580:
            clock.tick(999)


        leady +=leadxChange
        leady +=change
        scoreboard2('Life = ',str(life),red)


        pygame.display.update()
        clock.tick(500)
gameloop()
quit()
