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


def game_loop():
    snake_x = dis_width / 2
    snake_y = dis_height / 2

    current_time = 0

    delta_x = 0
    delta_y = 0

    # Handling quit
    game_over = False
    game_close = False

    # Snake array
    snake_body = []
    length_snake = 1

    # SuperPower Attributes
    super_power_active = False
    super_start_time = 0

    # SuperPower init Location
    super_power_x = round(randrange(0, dis_width - snake_block) / 10.0) * 10.0
    super_power_y = round(randrange(0, dis_height - snake_block) / 10.0) * 10.0

    # Initiate the first set of cords for first food
    food_x = round(randrange(0, dis_width - snake_block) / 10.0) * 10.0
    food_y = round(randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over and not game_close:

        for event in pygame.event.get():
            # If quit is clicked
            if event.type == pygame.QUIT:
                game_close = True
            # User input
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and delta_x != snake_block:
                    delta_x = -snake_block
                    delta_y = 0
                elif event.key == pygame.K_d and delta_x != -snake_block:
                    delta_x = snake_block
                    delta_y = 0
                elif event.key == pygame.K_s and delta_y != -snake_block:
                    delta_x = 0
                    delta_y = snake_block
                elif event.key == pygame.K_w and delta_y != snake_block:
                    delta_x = 0
                    delta_y = -snake_block
                elif event.key == pygame.K_q:
                    game_close = True

        # if snake hits wall
        if snake_x >= dis_width or snake_x < 0 or snake_y >= dis_height or snake_y < 0:
            game_over = True

        # update snakes delta
        snake_x += delta_x
        snake_y += delta_y
        dis.fill(WHITE)

        # draw food
        pygame.draw.rect(dis, RED, [food_x, food_y, snake_block, snake_block])
        if super_power_active == False:
            pygame.draw.rect(
                dis, BLUE, [super_power_x, super_power_y, snake_block, snake_block]
            )

        # Snake Length
        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake_body.append(snake_head)

        if len(snake_body) > length_snake:
            del snake_body[0]

        # Snake body hit detection
        for part in snake_body[:-1]:
            if part == snake_head:
                game_close = True

        # Draws snake
        draw_snake(snake_block, snake_body)

        # If snake eats food
        if snake_x == food_x and snake_y == food_y:
            food_x = round(randrange(0, dis_width - snake_block) / 10.0) * 10.0
            food_y = round(randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_snake += 1

        # If snake eats super power
        if snake_x == super_power_x and snake_y == super_power_y:
            super_power_x = round(randrange(0, dis_width - snake_block) / 10.0) * 10.0
            super_power_y = round(randrange(0, dis_width - snake_block) / 10.0) * 10.0
            super_start_time = current_time
            length_snake += 5
            super_power_active = True

        # If Truns off super power after 10 seconds
        if super_power_active == True and current_time == super_start_time + 1000:
            super_power_active = False

        # Display score
        dis_Score(length_snake - 1)

        pygame.display.update()

        if super_power_active:
            clock.tick(snake_speed * 1.8)
        else:
            clock.tick(snake_speed)

        current_time += 1

    pygame.quit()
    quit()


game_loop()
