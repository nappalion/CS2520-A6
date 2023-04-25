# Imports
import pygame
import math
import random

# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "Major League Soccer"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
''' add colors you use as RGB values here '''
RED = (255, 0, 0)
GREEN = (52, 166, 36)
BLUE = (29, 116, 248)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125, 0)
DARK_BLUE = (18, 0, 91)
DARK_GREEN = (0, 94, 0)
GRAY = (130, 130, 130)
YELLOW = (255, 255, 110)
SILVER = (200, 200, 200)
DAY_GREEN = (41, 129, 29)
NIGHT_GREEN = (0, 64, 0)
BRIGHT_YELLOW = (255, 244, 47)
NIGHT_GRAY = (104, 98, 115)
ck = (127, 33, 33)

DARKNESS = pygame.Surface(SIZE)
DARKNESS.set_alpha(200)
DARKNESS.fill((0, 0, 0))

SEE_THROUGH = pygame.Surface((800, 180))
SEE_THROUGH.set_alpha(150)
SEE_THROUGH.fill((124, 118, 135))


# Config
lights_on = True
day = True


# Game loop
done = False

stars = []
clouds = []

def draw_cloud(x, y):
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x, y + 8, 10, 10])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 6, y + 4, 8, 8])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 10, y, 16, 16])
    pygame.draw.ellipse(SEE_THROUGH, cloud_color, [x + 20, y + 8, 10, 10])
    pygame.draw.rect(SEE_THROUGH, cloud_color, [x + 6, y + 8, 18, 10])

def fill_stars():
    for n in range(200):
        x = random.randrange(0, 800)
        y = random.randrange(0, 200)
        r = random.randrange(1, 2)
        stars.append([x, y, r, r])

def fill_clouds():
    for i in range(20):
        x = random.randrange(-100, 1600)
        y = random.randrange(0, 150)
        clouds.append([x, y])
        
def draw_out_of_bounds():
        #out of bounds lines
        pygame.draw.line(screen, WHITE, [0, 580], [800, 580], 5)
        #left
        pygame.draw.line(screen, WHITE, [0, 360], [140, 220], 5)
        pygame.draw.line(screen, WHITE, [140, 220], [660, 220], 3)
        #right
        pygame.draw.line(screen, WHITE, [660, 220], [800, 360], 5)


def draw_safety_circle():
    #safety circle
    pygame.draw.ellipse(screen, WHITE, [240, 500, 320, 160], 5)

def draw_yard_line():
    #18 yard line goal box
    pygame.draw.line(screen, WHITE, [260, 220], [180, 300], 5)
    pygame.draw.line(screen, WHITE, [180, 300], [620, 300], 3)
    pygame.draw.line(screen, WHITE, [620, 300], [540, 220], 5)
    
def draw_arc():
    #arc at the top of the goal box
    pygame.draw.arc(screen, WHITE, [330, 280, 140, 40], math.pi, 2 * math.pi, 5)
    
def draw_scoreboard():
    #score board pole
    pygame.draw.rect(screen, GRAY, [390, 120, 20, 70])

    #score board
    pygame.draw.rect(screen, BLACK, [300, 40, 200, 90])
    pygame.draw.rect(screen, WHITE, [302, 42, 198, 88], 2)


def draw_goal_frame(left, top, w, h, ml_bias):
    #goal
    # pygame.draw.rect(screen, WHITE, [320, 140, 160, 80], 5)
    # pygame.draw.line(screen, WHITE, [340, 200], [460, 200], 3)
    # pygame.draw.line(screen, WHITE, [320, 220], [340, 200], 3)
    # pygame.draw.line(screen, WHITE, [480, 220], [460, 200], 3)
    # pygame.draw.line(screen, WHITE, [320, 140], [340, 200], 3)
    # pygame.draw.line(screen, WHITE, [480, 140], [460, 200], 3)

    # middle line coordinates
    ml_y = top + (h * ml_bias)
    ml_left_point = [left + 20, ml_y] 
    ml_right_point = [left + w - 20, ml_y]
            
    pygame.draw.rect(screen, WHITE, [left, top, w, h], 5)
    pygame.draw.line(screen, WHITE, [ml_left_point[0], ml_y], ml_right_point, 3)
    pygame.draw.line(screen, WHITE, [left, top + h], ml_left_point, 3)
    pygame.draw.line(screen, WHITE, [left + w, top + h], ml_right_point, 3)
    pygame.draw.line(screen, WHITE, [left, top], ml_left_point, 3)
    pygame.draw.line(screen, WHITE, [left + w, top], ml_right_point, 3)

def draw_middle_net(left, top, w, h, ml_bias):
    # Draw Vertical Lines

    # goal frame middle line coordinates
    ml_y = top + (h * ml_bias)
    ml_left_point = [left + 20, ml_y] 

    # Right diagonal nets start here
    right_diag_x = 0

    start_x = left + 5
    end_x = ml_left_point[0] + 1

    while start_x < end_x:
        pygame.draw.line(screen, WHITE, [start_x, top], [end_x, ml_y], 1)
        start_x += 5
        end_x += 3
        right_diag_x = (left + w) - (start_x - left + 5)

    while start_x <= right_diag_x:
        pygame.draw.line(screen, WHITE, [start_x, top], [end_x, ml_y], 1)
        start_x += 4
        end_x += 4


    while start_x <= (left + w - 5):
        pygame.draw.line(screen, WHITE, [start_x, top], [end_x, ml_y], 1)
        start_x += 5
        end_x += 3

    start_x = left + 4
    end_x = left + w - 4
    y = top

    #Draw Horizontal Lines
    while y < ml_y:
        if y >= (top + (h / 2)):
            start_x = left + 15
            end_x = left + w - 10

        pygame.draw.line(screen, WHITE, [start_x, y], [end_x, y], 1)
        y += 4

def draw_left_right_net(left, top, w, h):

    start_x = left
    end_x = top + h

    #net part 2; vertical lines left
    for i in range(1,10):
        pygame.draw.line(screen, WHITE, [left, top], [(start_x + 2 * i), (end_x - 2 * i)], 1)

    start_x = left + w - 2 
    end_x = top + h - 2

    #net part 3; vertical lines right
    for i in range(1,10):
        pygame.draw.line(screen, WHITE, [left + w, top], [(start_x - 2 * i), (end_x - 2 * i)], 1)

def draw_goal(left, top, w, h, ml_bias):
    draw_goal_frame(left, top, w, h, ml_bias)
    draw_middle_net(left, top, w, h, ml_bias)
    draw_left_right_net(left, top, w, h)


    

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_l:
                lights_on = not lights_on
            elif event.key == pygame.K_d:
                day = not day

    # Game logic (Check for collisions, update points, etc.)
    ''' leave this section alone for now ''' 
    if lights_on:
        light_color = YELLOW
    else:
        light_color = SILVER

    if day:
        sky_color = BLUE
        field_color = GREEN
        stripe_color = DAY_GREEN
        cloud_color = WHITE
    else:
        sky_color = DARK_BLUE
        field_color = DARK_GREEN
        stripe_color = NIGHT_GREEN
        cloud_color = NIGHT_GRAY

    for c in clouds:
        c[0] -= 0.5

        if c[0] < -100:
            c[0] = random.randrange(800, 1600)
            c[1] = random.randrange(0, 150)
            
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(sky_color)
    SEE_THROUGH.fill(ck)
    SEE_THROUGH.set_colorkey(ck)
    
    if not day:
    #stars
        for s in stars:
            pygame.draw.ellipse(screen, WHITE, s)




    pygame.draw.rect(screen, field_color, [0, 180, 800 , 420])
    pygame.draw.rect(screen, stripe_color, [0, 180, 800, 42])
    pygame.draw.rect(screen, stripe_color, [0, 264, 800, 52])
    pygame.draw.rect(screen, stripe_color, [0, 368, 800, 62])
    pygame.draw.rect(screen, stripe_color, [0, 492, 800, 82])


    '''fence'''
    y = 170
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, NIGHT_GRAY, [[x + 2, y], [x + 2, y + 15], [x, y + 15], [x, y]])

    y = 170
    for x in range(5, 800, 3):
        pygame.draw.line(screen, NIGHT_GRAY, [x, y], [x, y + 15], 1)

    x = 0
    for y in range(170, 185, 4):
        pygame.draw.line(screen, NIGHT_GRAY, [x, y], [x + 800, y], 1)

    if day:
        pygame.draw.ellipse(screen, BRIGHT_YELLOW, [520, 50, 40, 40])
    else:
        pygame.draw.ellipse(screen, WHITE, [520, 50, 40, 40]) 
        pygame.draw.ellipse(screen, sky_color, [530, 45, 40, 40])

    
    
    for c in clouds:
        draw_cloud(c[0], c[1])
    screen.blit(SEE_THROUGH, (0, 0)) 
    
    fill_stars()
    
    fill_clouds()  

    draw_out_of_bounds()

    draw_safety_circle()

    draw_yard_line()

    draw_arc()

    draw_scoreboard()

    #320, 140, 160, 80, 0.75
    draw_goal(left=320, top=140, w=160, h=80, ml_bias=0.75)

    #6 yard line goal box
    pygame.draw.line(screen, WHITE, [310, 220], [270, 270], 3)
    pygame.draw.line(screen, WHITE, [270, 270], [530, 270], 2)
    pygame.draw.line(screen, WHITE, [530, 270], [490, 220], 3)

    #light pole 1
    pygame.draw.rect(screen, GRAY, [150, 60, 20, 140])
    pygame.draw.ellipse(screen, GRAY, [150, 195, 20, 10])

    #lights
    pygame.draw.line(screen, GRAY, [110, 60], [210, 60], 2)
    pygame.draw.ellipse(screen, light_color, [110, 40, 20, 20])
    pygame.draw.ellipse(screen, light_color, [130, 40, 20, 20])
    pygame.draw.ellipse(screen, light_color, [150, 40, 20, 20])
    pygame.draw.ellipse(screen, light_color, [170, 40, 20, 20])
    pygame.draw.ellipse(screen, light_color, [190, 40, 20, 20])
    pygame.draw.line(screen, GRAY, [110, 40], [210, 40], 2)
    pygame.draw.ellipse(screen, light_color, [110, 20, 20, 20])
    pygame.draw.ellipse(screen, light_color, [130, 20, 20, 20])
    pygame.draw.ellipse(screen, light_color, [150, 20, 20, 20])
    pygame.draw.ellipse(screen, light_color, [170, 20, 20, 20])
    pygame.draw.ellipse(screen, light_color, [190, 20, 20, 20])
    pygame.draw.line(screen, GRAY, [110, 20], [210, 20], 2)

    #light pole 2
    pygame.draw.rect(screen, GRAY, [630, 60, 20, 140])
    pygame.draw.ellipse(screen, GRAY, [630, 195, 20, 10])

    #lights
        
    pygame.draw.line(screen, GRAY, [590, 60], [690, 60], 2)
    pygame.draw.ellipse(screen, light_color, [590, 40, 20, 20])
    pygame.draw.ellipse(screen, light_color, [610, 40, 20, 20])
    pygame.draw.ellipse(screen, light_color, [630, 40, 20, 20])
    pygame.draw.ellipse(screen, light_color, [650, 40, 20, 20])
    pygame.draw.ellipse(screen, light_color, [670, 40, 20, 20])
    pygame.draw.line(screen, GRAY, [590, 40], [690, 40], 2)
    pygame.draw.ellipse(screen, light_color, [590, 20, 20, 20])
    pygame.draw.ellipse(screen, light_color, [610, 20, 20, 20])
    pygame.draw.ellipse(screen, light_color, [630, 20, 20, 20])
    pygame.draw.ellipse(screen, light_color, [650, 20, 20, 20])
    pygame.draw.ellipse(screen, light_color, [670, 20, 20, 20])
    pygame.draw.line(screen, GRAY, [590, 20], [690, 20], 2)


    #stands right
    pygame.draw.polygon(screen, RED, [[680, 220], [800, 340], [800, 290], [680, 180]])
    pygame.draw.polygon(screen, WHITE, [[680, 180], [800, 100], [800, 290]])

  
    #stands left
    pygame.draw.polygon(screen, RED, [[120, 220], [0, 340], [0, 290], [120, 180]])
    pygame.draw.polygon(screen, WHITE, [[120, 180], [0, 100], [0, 290]])
    #people
    

    #corner flag right
    pygame.draw.line(screen, BRIGHT_YELLOW, [140, 220], [135, 190], 3)
    pygame.draw.polygon(screen, RED, [[132, 190], [125, 196], [135, 205]])

    #corner flag left
    pygame.draw.line(screen, BRIGHT_YELLOW, [660, 220], [665, 190], 3)
    pygame.draw.polygon(screen, RED, [[668, 190], [675, 196], [665, 205]]) 

    # DARKNESS
    if not day and not lights_on:
        screen.blit(DARKNESS, (0, 0))    
    
    #pygame.draw.polygon(screen, BLACK, [[200, 200], [50,400], [600, 500]], 10)

    ''' angles for arcs are measured in radians (a pre-cal topic) '''
    #pygame.draw.arc(screen, ORANGE, [100, 100, 100, 100], 0, math.pi/2, 1)
    #pygame.draw.arc(screen, BLACK, [100, 100, 100, 100], 0, math.pi/2, 50)


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()