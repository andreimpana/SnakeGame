import pygame
from random import randint, randrange


WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

dis_width = 800
dis_height = 600


dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.update()
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15
score = 0

score_font = pygame.font.SysFont("Helvetica", 20)


def dis_Score(score):
    val = score_font.render("Score: " + str(score), True, BLACK)
    dis.blit(val, [0, 0])


def draw_snake(snake_block, snake_body):
    for x in snake_body:
        pygame.draw.rect(dis, BLACK, [x[0], x[1], snake_block, snake_block])


def gameLoop():
    x1 = dis_width/2
    y1 = dis_height/2

    currentTime = 0

    deltaX = 0
    deltaY = 0

    game_over = False
    game_close = False

    snake_body = []
    Length_snake = 1
    # SuperPower Attributes
    superPowerActive = False
    superStartTime = 0

    # SuperPower init Location
    superPowerx = round(randrange(0, dis_width - snake_block) / 10.0) * 10.0
    superPowerY = round(randrange(0, dis_height - snake_block) / 10.0) * 10.0

    # Initiate the first set of cords for first food
    foodX = round(randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foodY = round(randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over and not game_close:

        for event in pygame.event.get():
            # If quit is clicked
            if event.type == pygame.QUIT:
                game_close = True
            # User input
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and deltaX != snake_block:
                    deltaX = -snake_block
                    deltaY = 0
                elif event.key == pygame.K_d and deltaX != -snake_block:
                    deltaX = snake_block
                    deltaY = 0
                elif event.key == pygame.K_s and deltaY != -snake_block:
                    deltaX = 0
                    deltaY = snake_block
                elif event.key == pygame.K_w and deltaY != snake_block:
                    deltaX = 0
                    deltaY = -snake_block
                elif event.key == pygame.K_q:
                    game_close = True

        # if snake hits wall
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_over = True

        # update snakes delta
        x1 += deltaX
        y1 += deltaY
        dis.fill(WHITE)

        # draw food
        pygame.draw.rect(dis, RED, [foodX, foodY, snake_block, snake_block])
        if(superPowerActive == False):
            pygame.draw.rect(dis, BLUE, [superPowerx, superPowerY, snake_block, snake_block])

        # Snake Length
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_body.append(snake_head)

        if len(snake_body) > Length_snake:
            del snake_body[0]

        # Snake body hit detection
        for x in snake_body[:-1]:
            if x == snake_head:
                game_close = True

        # Draws snake
        draw_snake(snake_block, snake_body)

        # If snake eats food
        if x1 == foodX and y1 == foodY:
            foodX = round(randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foodY = round(randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_snake += 1

        # If snake eats super power
        if x1 == superPowerx and y1 == superPowerY:
            superPowerx = round(randrange(0, dis_width - snake_block) / 10.0) * 10.0
            superPowerY = round(randrange(0, dis_width - snake_block) / 10.0) * 10.0
            superStartTime = currentTime
            Length_snake += 5
            superPowerActive = True

        # If Truns off super power after 10 seconds
        if superPowerActive == True and currentTime == superStartTime + 1000:
            superPowerActive = False

        # Display score
        dis_Score(Length_snake - 1)

        pygame.display.update()

        if superPowerActive:
            clock.tick(snake_speed*1.8)
        else:
            clock.tick(snake_speed)

        currentTime += 1

    pygame.quit()
    quit()


gameLoop()
