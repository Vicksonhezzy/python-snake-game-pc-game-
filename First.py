import pygame
import random
pygame.init()

white = (255, 255, 255,)
black = (0, 0, 0,)
red = (255, 0, 0)
green = (0, 155, 0)

display_width = 800
display_height = 600
block_size = 10
applethickness = 20
obstructX = 200
obstructY = 350
obstructX2 = 230
obstructY2 = 410
obstructT = 470
obstructZ = 40
obstructT2 = 400
obstructZ2 = 100

gamedisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Bite')

icon = pygame.image.load('apple.png')
pygame.display.set_icon(icon)

# obstruction = pygame.image.load('obstruction.png')
img = pygame.image.load('SnakeHead2.png')
img2 = pygame.image.load('apple.png')


clock = pygame.time.Clock()

font = pygame.font.SysFont('comicsansms', 40, bold=1, italic=0)
font2 = pygame.font.SysFont('comicsansms', 20, bold=1, italic=1)
font3 = pygame.font.SysFont('comicsansms', 15, bold=0, italic=1)
scorefont = pygame.font.SysFont(None, 20, 1, 1)


def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    gameIntro()
                    quit()

        #gamedisplay.fill(white)
        message_display('Game Paused', red, -100)
        message_display2('Press C to continue or Q to quit', black, 25)
        pygame.display.update()
        clock.tick(5)


def master_level():
    master = True
    while master:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or pygame.K_RIGHT or pygame.K_DOWN or pygame.K_UP:
                    master = False
                else:
                    if event.key == pygame.K_q:
                        gameIntro()
                        pygame.display.update()

        #gamedisplay.fill(white)
        message_display2('Congratulations! you are now a Snake-Master', red, -50)
        message_display4('Press any direction key to continue or Q to quit', black, 10)
        pygame.display.update()
        clock.tick(5)


def score(score):
    text = scorefont.render('Score: '+str(score), True, black)
    gamedisplay.blit(text, [0, 0])


def applePosition():
    global lead_x
    applePositionX = round(random.randrange(0, display_width - applethickness) / 10) * 10
    applePositionY = round(random.randrange(0, display_height - applethickness) / 10) * 10
    return applePositionX, applePositionY


direction = 'right'
def snake(block_size, snakelist ):
    if direction == 'right':
        head = pygame.transform.rotate(img, 270)
    elif direction == 'left':
        head = pygame.transform.rotate(img, -270)
    elif direction == 'up':
        head = img
    elif direction == 'down':
        head = pygame.transform.rotate(img, 180)
    gamedisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gamedisplay, green, [XnY[0], XnY[1], block_size, block_size])


def textObject(text, color):
    textSurf = font.render(text, True, color)
    return textSurf, textSurf.get_rect()


def textObject2(text, color):
    textSurf2 = font2.render(text, True, color)
    return textSurf2, textSurf2.get_rect()


def textObject3(text, color):
    textSurf3 = font3.render(text, True, color)
    return textSurf3, textSurf3.get_rect()



def message_display(msg, color, Ydisplays = 0):
    textSurface, textRect = textObject(msg, color)
    #screen_text = font.render(msg, True, color)
    #gamedisplay.blit(screen_text, [display_width/3.29, display_height/2.49])
    textRect.center = (display_width/2), (display_height/2) + Ydisplays
    gamedisplay.blit(textSurface, textRect)



def message_display4(msg, color, Ydisplays = 0):
    textSurface, textRect = textObject3(msg, color)
    #screen_text = font.render(msg, True, color)
    #gamedisplay.blit(screen_text, [display_width/3.29, display_height/2.49])
    textRect.center = (display_width/2), (display_height/2) + Ydisplays
    gamedisplay.blit(textSurface, textRect)


def message_display2(msg, color, Ydisplays = 0):
    textSurface, textRect = textObject2(msg, color)
    #screen_text = font.render(msg, True, color)
    #gamedisplay.blit(screen_text, [display_width/3.29, display_height/2.49])
    textRect.center = (display_width/2), (display_height/2) + Ydisplays
    gamedisplay.blit(textSurface, textRect)


def message_display3(msg, color, Ydisplays = 0):
    textSurface, textRect = textObject2(msg, color)
    #screen_text = font.render(msg, True, color)
    #gamedisplay.blit(screen_text, [display_width/3.29, display_height/2.49])
    textRect = display_width/3, (display_height/2) + Ydisplays
    gamedisplay.blit(textSurface, textRect)


def endScore(text, color):
    textSurf2 = scorefont.render(text, True, color)
    return textSurf2, textSurf2.get_rect()


def endScore_display(msg, color, Ydisplays = 0):
    textSurface, textRect = endScore(msg, color)
    #screen_text = font.render(msg, True, color)
    #gamedisplay.blit(screen_text, [display_width/3.29, display_height/2.49])
    textRect.center = (display_width/2), (display_height/2) + Ydisplays
    gamedisplay.blit(textSurface, textRect)


def level_1():
    global direction
    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = 0
    lead_y_change = 0

    gameExit = False
    gameOver = False

    snakelist = []
    snakelenght = 0

    applePositionX, applePositionY = applePosition()
    #applePositionX = round(random.randrange(0, display_width - applethickness) / 10) * 10
    #applePositionY = round(random.randrange(0, display_height - applethickness) / 10) * 10

    while not gameExit:
        while gameOver is True:
            gamedisplay.fill(white)
            message_display('Game Over!', red)
            endScore_display('Score: ' + str(snakelenght * 2), green, 30)
            message_display2('press c to continue or q to quit', black, 50)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        gameIntro()
                    elif event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = 'left'
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = 'right'
                    lead_x_change = block_size
                    lead_y_change = 0

                elif event.key == pygame.K_UP:
                    direction = 'up'
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = 'down'
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key == pygame.K_p:
                    pause()

        if lead_x >= display_width or lead_x < -10 or lead_y < -10 or lead_y >= display_height:
            gameOver = True


        lead_x += lead_x_change
        lead_y += lead_y_change

        gamedisplay.fill(white)
        '''       
        pygame.draw.rect(gamedisplay, black, [0, 0, 800, 10])
        pygame.draw.rect(gamedisplay, black, [0, 590, 800, 10])
        pygame.draw.rect(gamedisplay, black, [790, 0, 10, 600])
        pygame.draw.rect(gamedisplay, black, [0, 0, 10, 600])
        '''

        #pygame.draw.rect(gamedisplay, red, [applePositionX, applePositionY, applethickness, applethickness])
        #pygame.draw.circle(gamedisplay, red, [applePositionX, applePositionY], applethickness, applethickness)
        gamedisplay.blit(img2, (applePositionX, applePositionY))

        snakehead = []
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)
        snake(block_size, snakelist)

        if len(snakelist) > snakelenght:
            del snakelist[0]

        for eachsegment in snakelist[:-1]:
            if snakehead == eachsegment:
                gameOver = True

        score(snakelenght * 2)
        pygame.display.update()

        #scores = 0
#        while lead_x == applePositionX and lead_y == applePositionY:
#            applePositionX = round(random.randrange(0, display_width - 10) / 10) * 10
#            applePositionY = round(random.randrange(0, display_height - 10) / 10) * 10
#            snakelenght += 1
            #print(scores)
        #scores += 1

        if applePositionX + applethickness > lead_x >= applePositionX and applePositionY + applethickness > lead_y >= applePositionY:
            applePositionX, applePositionY = applePosition()
            #applePositionX = round(random.randrange(0, display_width - applethickness) / 10) * 10
            #applePositionY = round(random.randrange(0, display_height - applethickness) / 10) * 10
            snakelenght += 1

        # if snakelenght <= n*4:
        #     clock.tick(15)
        # else:
        #     if snakelenght > 7:
        #         clock.tick(15*n)
        # n += 2
        clock.tick(8)

    pygame.quit()
    quit()


def level_2():
    global direction
    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = 0
    lead_y_change = 0

    gameExit = False
    gameOver = False

    snakelist = []
    snakelenght = 0

    applePositionX, applePositionY = applePosition()
    #applePositionX = round(random.randrange(0, display_width - applethickness) / 10) * 10
    #applePositionY = round(random.randrange(0, display_height - applethickness) / 10) * 10

    n = 2
    while not gameExit:
        while gameOver is True:
            gamedisplay.fill(white)
            message_display('Game Over!', red)
            endScore_display('Score: ' + str(snakelenght * 3), green, 30)
            message_display2('press c to continue or q to quit', black, 50)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        gameIntro()
                    elif event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = 'left'
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = 'right'
                    lead_x_change = block_size
                    lead_y_change = 0

                elif event.key == pygame.K_UP:
                    direction = 'up'
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = 'down'
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key == pygame.K_p:
                    pause()

        if lead_x >= display_width or lead_x < -10 or lead_y < -10 or lead_y >= display_height:
            gameOver = True


        lead_x += lead_x_change
        lead_y += lead_y_change

        gamedisplay.fill(white)
        '''       
        pygame.draw.rect(gamedisplay, black, [0, 0, 800, 10])
        pygame.draw.rect(gamedisplay, black, [0, 590, 800, 10])
        pygame.draw.rect(gamedisplay, black, [790, 0, 10, 600])
        pygame.draw.rect(gamedisplay, black, [0, 0, 10, 600])
        '''

        #pygame.draw.rect(gamedisplay, red, [applePositionX, applePositionY, applethickness, applethickness])
        #pygame.draw.circle(gamedisplay, red, [applePositionX, applePositionY], applethickness, applethickness)
        gamedisplay.blit(img2, (applePositionX, applePositionY))

        snakehead = []
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)
        snake(block_size, snakelist)

        if len(snakelist) > snakelenght:
            del snakelist[0]

        for eachsegment in snakelist[:-1]:
            if snakehead == eachsegment:
                gameOver = True

        score(snakelenght * 3)
        pygame.display.update()

        #scores = 0
#        while lead_x == applePositionX and lead_y == applePositionY:
#            applePositionX = round(random.randrange(0, display_width - 10) / 10) * 10
#            applePositionY = round(random.randrange(0, display_height - 10) / 10) * 10
#            snakelenght += 1
            #print(scores)
        #scores += 1

        if applePositionX + applethickness > lead_x >= applePositionX and applePositionY + applethickness > lead_y >= applePositionY:
            applePositionX, applePositionY = applePosition()
            #applePositionX = round(random.randrange(0, display_width - applethickness) / 10) * 10
            #applePositionY = round(random.randrange(0, display_height - applethickness) / 10) * 10
            snakelenght += 1

        # if snakelenght <= n*4:
        #     clock.tick(15)
        # else:
        #     if snakelenght > 7:
        #         clock.tick(15*n)
        # n += 2
        clock.tick(16)

    pygame.quit()
    quit()


def level_3():
    global direction
    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = 0
    lead_y_change = 0

    gameExit = False
    gameOver = False

    snakelist = []
    snakelenght = 0

    applePositionX, applePositionY = applePosition()
    #applePositionX = round(random.randrange(0, display_width - applethickness) / 10) * 10
    #applePositionY = round(random.randrange(0, display_height - applethickness) / 10) * 10

    n = 2
    while not gameExit:
        while gameOver is True:
            gamedisplay.fill(white)
            message_display('Game Over!', red)
            endScore_display('Score: ' + str(snakelenght * 4), green, 30)
            message_display2('press c to continue or q to quit', black, 50)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        gameIntro()
                    elif event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = 'left'
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = 'right'
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = 'up'
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = 'down'
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key == pygame.K_p:
                    pause()

        if lead_x >= display_width or lead_x < -10 or lead_y < -10 or lead_y >= display_height:
            gameOver = True


        lead_x += lead_x_change
        lead_y += lead_y_change

        gamedisplay.fill(white)
        '''       
        pygame.draw.rect(gamedisplay, black, [0, 0, 800, 10])
        pygame.draw.rect(gamedisplay, black, [0, 590, 800, 10])
        pygame.draw.rect(gamedisplay, black, [790, 0, 10, 600])
        pygame.draw.rect(gamedisplay, black, [0, 0, 10, 600])
        '''

        #pygame.draw.rect(gamedisplay, red, [applePositionX, applePositionY, applethickness, applethickness])
        #pygame.draw.circle(gamedisplay, red, [applePositionX, applePositionY], applethickness, applethickness)
        gamedisplay.blit(img2, (applePositionX, applePositionY))

        snakehead = []
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)
        snake(block_size, snakelist)

        if len(snakelist) > snakelenght:
            del snakelist[0]

        for eachsegment in snakelist[:-1]:
            if snakehead == eachsegment:
                gameOver = True

        score(snakelenght * 4)
        pygame.display.update()

        #scores = 0
#        while lead_x == applePositionX and lead_y == applePositionY:
#            applePositionX = round(random.randrange(0, display_width - 10) / 10) * 10
#            applePositionY = round(random.randrange(0, display_height - 10) / 10) * 10
#            snakelenght += 1
            #print(scores)
        #scores += 1

        if applePositionX + applethickness > lead_x >= applePositionX and applePositionY + applethickness > lead_y >= applePositionY:
            applePositionX, applePositionY = applePosition()
            #applePositionX = round(random.randrange(0, display_width - applethickness) / 10) * 10
            #applePositionY = round(random.randrange(0, display_height - applethickness) / 10) * 10
            snakelenght += 1

        # if snakelenght <= n*4:
        #     clock.tick(15)
        # else:
        #     if snakelenght > 7:
        #         clock.tick(15*n)
        # n += 2
        clock.tick(24)

    pygame.quit()
    quit()


def level_4():
    global direction
    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = 0
    lead_y_change = 0

    gameExit = False
    gameOver = False

    snakelist = []
    snakelenght = 0

    applePositionX, applePositionY = applePosition()
    #applePositionX = round(random.randrange(0, display_width - applethickness) / 10) * 10
    #applePositionY = round(random.randrange(0, display_height - applethickness) / 10) * 10

    n = 2
    while not gameExit:
        while gameOver is True:
            gamedisplay.fill(white)
            message_display('Game Over!', red)
            endScore_display('Score: ' + str(snakelenght * 5), green, 30)
            message_display2('press c to continue or q to quit', black, 50)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        gameIntro()
                    elif event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = 'left'
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = 'right'
                    lead_x_change = block_size
                    lead_y_change = 0

                elif event.key == pygame.K_UP:
                    direction = 'up'
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = 'down'
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key == pygame.K_p:
                    pause()

        if lead_x >= display_width or lead_x < -10 or lead_y < -10 or lead_y >= display_height:
            gameOver = True


        lead_x += lead_x_change
        lead_y += lead_y_change

        gamedisplay.fill(white)
        '''       
        pygame.draw.rect(gamedisplay, black, [0, 0, 800, 10])
        pygame.draw.rect(gamedisplay, black, [0, 590, 800, 10])
        pygame.draw.rect(gamedisplay, black, [790, 0, 10, 600])
        pygame.draw.rect(gamedisplay, black, [0, 0, 10, 600])
        '''

        #pygame.draw.rect(gamedisplay, red, [applePositionX, applePositionY, applethickness, applethickness])
        #pygame.draw.circle(gamedisplay, red, [applePositionX, applePositionY], applethickness, applethickness)
        gamedisplay.blit(img2, (applePositionX, applePositionY))

        snakehead = []
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)
        snake(block_size, snakelist)

        if len(snakelist) > snakelenght:
            del snakelist[0]

        for eachsegment in snakelist[:-1]:
            if snakehead == eachsegment:
                gameOver = True

        score(snakelenght * 5)
        pygame.display.update()

        #scores = 0
#        while lead_x == applePositionX and lead_y == applePositionY:
#            applePositionX = round(random.randrange(0, display_width - 10) / 10) * 10
#            applePositionY = round(random.randrange(0, display_height - 10) / 10) * 10
#            snakelenght += 1
            #print(scores)
        #scores += 1

        if applePositionX + applethickness > lead_x >= applePositionX and applePositionY + applethickness > lead_y >= applePositionY:
            applePositionX, applePositionY = applePosition()
            #applePositionX = round(random.randrange(0, display_width - applethickness) / 10) * 10
            #applePositionY = round(random.randrange(0, display_height - applethickness) / 10) * 10
            snakelenght += 1

        # if snakelenght <= n*4:
        #     clock.tick(15)
        # else:
        #     if snakelenght > 7:
        #         clock.tick(15*n)
        # n += 2
        clock.tick(32)

    pygame.quit()
    quit()


def level_5():
    global direction
    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = 0
    lead_y_change = 0

    gameExit = False
    gameOver = False

    snakelist = []
    snakelenght = 0

    applePositionX, applePositionY = applePosition()
    #applePositionX = round(random.randrange(0, display_width - applethickness) / 10) * 10
    #applePositionY = round(random.randrange(0, display_height - applethickness) / 10) * 10

    n = 2
    while not gameExit:
        while gameOver is True:
            gamedisplay.fill(white)
            message_display('Game Over!', red)
            endScore_display('Score: ' + str(snakelenght * 6), green, 30)
            message_display2('press c to continue or q to quit', black, 50)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        gameIntro()
                    elif event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = 'left'
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = 'right'
                    lead_x_change = block_size
                    lead_y_change = 0

                elif event.key == pygame.K_UP:
                    direction = 'up'
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = 'down'
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key == pygame.K_p:
                    pause()

        if lead_x >= display_width or lead_x < -10 or lead_y < -10 or lead_y >= display_height:
            gameOver = True


        lead_x += lead_x_change
        lead_y += lead_y_change

        gamedisplay.fill(white)
        '''       
        pygame.draw.rect(gamedisplay, black, [0, 0, 800, 10])
        pygame.draw.rect(gamedisplay, black, [0, 590, 800, 10])
        pygame.draw.rect(gamedisplay, black, [790, 0, 10, 600])
        pygame.draw.rect(gamedisplay, black, [0, 0, 10, 600])
        '''

        #pygame.draw.rect(gamedisplay, red, [applePositionX, applePositionY, applethickness, applethickness])
        #pygame.draw.circle(gamedisplay, red, [applePositionX, applePositionY], applethickness, applethickness)
        gamedisplay.blit(img2, (applePositionX, applePositionY))

        snakehead = []
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)
        snake(block_size, snakelist)

        if len(snakelist) > snakelenght:
            del snakelist[0]

        for eachsegment in snakelist[:-1]:
            if snakehead == eachsegment:
                gameOver = True

        score(snakelenght * 6)
        pygame.display.update()

        #scores = 0
#        while lead_x == applePositionX and lead_y == applePositionY:
#            applePositionX = round(random.randrange(0, display_width - 10) / 10) * 10
#            applePositionY = round(random.randrange(0, display_height - 10) / 10) * 10
#            snakelenght += 1
            #print(scores)
        #scores += 1

        if applePositionX + applethickness > lead_x >= applePositionX and applePositionY + applethickness > lead_y >= applePositionY:
            applePositionX, applePositionY = applePosition()
            #applePositionX = round(random.randrange(0, display_width - applethickness) / 10) * 10
            #applePositionY = round(random.randrange(0, display_height - applethickness) / 10) * 10
            snakelenght += 1

        # if snakelenght <= n*4:
        #     clock.tick(15)
        # else:
        #     if snakelenght > 7:
        #         clock.tick(15*n)
        # n += 2
        clock.tick(40)

    pygame.quit()
    quit()


def level_6():
    global direction
    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = 0
    lead_y_change = 0

    gameExit = False
    gameOver = False

    snakelist = []
    snakelenght = 0

    applePositionX, applePositionY = applePosition()

    #applePositionX = round(random.randrange(0, display_width - applethickness) / 10) * 10
    #applePositionY = round(random.randrange(0, display_height - applethickness) / 10) * 10

    while not gameExit:
        while gameOver is True:
            gamedisplay.fill(white)
            message_display('Game Over!', red)
            endScore_display('Score: ' + str(snakelenght * 8), green, 30)
            message_display2('press c to continue or q to quit', black, 50)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        gameIntro()
                    elif event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = 'left'
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = 'right'
                    lead_x_change = block_size
                    lead_y_change = 0

                elif event.key == pygame.K_UP:
                    direction = 'up'
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = 'down'
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key == pygame.K_p:
                    pause()

        if lead_x >= display_width or lead_x < -10 or lead_y < -10 or lead_y >= display_height:
            gameOver = True

        # if lead_x >= obstructionX and lead_y >= obstructionY:
        #     gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        gamedisplay.fill(white)
        '''       
        pygame.draw.rect(gamedisplay, black, [0, 0, 800, 10])
        pygame.draw.rect(gamedisplay, black, [0, 590, 800, 10])
        pygame.draw.rect(gamedisplay, black, [790, 0, 10, 600])
        pygame.draw.rect(gamedisplay, black, [0, 0, 10, 600])
        '''

        #pygame.draw.rect(gamedisplay, red, [applePositionX, applePositionY, applethickness, applethickness])
        #pygame.draw.circle(gamedisplay, red, [applePositionX, applePositionY], applethickness, applethickness)
        # gamedisplay.blit(obstruction, (obstructionX, obstructionY))
        pygame.draw.rect(gamedisplay, black, [obstructX, obstructY, 30, 90])
        pygame.draw.rect(gamedisplay, black, [obstructX2, obstructY2, 70, 30])

        pygame.draw.rect(gamedisplay, black, [obstructT, obstructZ, 30, 90])
        pygame.draw.rect(gamedisplay, black, [obstructT2, obstructZ2, 70, 30])

        if (obstructX + 30 + applethickness > applePositionX >= obstructX and obstructY + 90 + applethickness > applePositionY >= obstructY) or (obstructX2 + 70 + applethickness > applePositionX >= obstructX2 and obstructY2 + 30 + applethickness > applePositionY >= obstructY2):
            if (obstructT + 30 + applethickness > applePositionX >= obstructT and obstructZ + 90 + applethickness > applePositionY >= obstructZ) or (obstructT2 + 70 + applethickness > applePositionX >= obstructT2 and obstructZ2 + 30 + applethickness > applePositionY >= obstructZ2):
                gamedisplay.blit(img2, (applePositionX, applePositionY))
        else:
            gamedisplay.blit(img2, (applePositionX, applePositionY))

        snakehead = []
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)
        snake(block_size, snakelist)

        if len(snakelist) > snakelenght:
            del snakelist[0]

        for eachsegment in snakelist[:-1]:
            if snakehead == eachsegment:
                gameOver = True

        score(snakelenght * 8)

        pygame.display.update()

        #scores = 0
#        while lead_x == applePositionX and lead_y == applePositionY:
#            applePositionX = round(random.randrange(0, display_width - 10) / 10) * 10
#            applePositionY = round(random.randrange(0, display_height - 10) / 10) * 10
#            snakelenght += 1
            #print(scores)
        #scores += 1

        if applePositionX + applethickness > lead_x >= applePositionX and applePositionY + applethickness > lead_y >= applePositionY:
            applePositionX, applePositionY = applePosition()
            #applePositionX = round(random.randrange(0, display_width - applethickness) / 10) * 10
            #applePositionY = round(random.randrange(0, display_height - applethickness) / 10) * 10
            snakelenght += 1
        if (obstructX + 30 > lead_x >= obstructX and obstructY + 90 > lead_y >= obstructY) or (obstructX2 + 70 > lead_x >= obstructX2 and obstructY2 + 30 > lead_y >= obstructY2):
            gameOver = True
        if (obstructT + 30 > lead_x >= obstructT and obstructZ + 90 > lead_y >= obstructZ) or (obstructT2 + 70 > lead_x >= obstructT2 and obstructZ2 + 30 > lead_y >= obstructZ2):
            gameOver = True

            #applePositionX = round(random.randrange(0, display_width - applethickness) / 10) * 10
            #applePositionY = round(random.randrange(0, display_height - applethickness) / 10) * 10

        if (snakelenght * 8) == 400:
            master_level()
            snakelenght += 1

        # if snakelenght <= n*4:
        #     clock.tick(15)
        # else:
        #     if snakelenght > 7:
        #         clock.tick(15*n)
        # n += 2
        clock.tick(56)

    pygame.quit()
    quit()


def gameIntro():
    global gameOver, gameExit
    intro = True
    gameExit = False
    while intro and not gameExit:
        gamedisplay.fill(white)
        message_display('Welcome to SnakeBite', green, -200)
        message_display2('The objectives is to eat the red apples', black, -130)
        message_display2('The more apples you eat the longer you get', black, -90)
        message_display2('If you run into yourself, or cross the edges, you die!', black, -50)
        message_display3('1:: Level one', green, 10)
        message_display3('2:: Level two', green, 30)
        message_display3('3:: Level three', green, 50)
        message_display3('4:: Level four', green, 70)
        message_display3('5:: Level five', green, 90)
        message_display3('6:: Level impossible!', green, 110)
        message_display2("\n \n .....don't bite yourself........!!", black, 160)
        message_display2("Press 1,2,3,4,5 or 6 to choose level and P to pause or Q TO Quit", black, -10)
        message_display4('copyright@ 2019. A game developed by CoolestDude.python', black, 285)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                gameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    level_1()
                elif event.key == pygame.K_2:
                    level_2()
                elif event.key == pygame.K_3:
                    level_3()
                elif event.key == pygame.K_4:
                    level_4()
                elif event.key == pygame.K_5:
                    level_5()
                elif event.key == pygame.K_6:
                    level_6()
                elif event.key == pygame.K_q:
                    gameExit = True
                    gameOver = True
        pygame.display.update()


gameIntro()
