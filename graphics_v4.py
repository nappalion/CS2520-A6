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


def fill_stars(star_range):
    for n in range(star_range):
        x = random.randrange(0, star_range*4)
        y = random.randrange(0, star_range)
        r = random.randrange(1, 2)
        stars.append([x, y, r, r])


def fill_clouds(cloud_range):
    for i in range(cloud_range):
        x = random.randrange(-100, cloud_range*80)
        y = random.randrange(0, 150)
        clouds.append([x, y])
        
def clouds_stars(s_range, c_range):
    fill_stars(s_range)
    fill_clouds(c_range)
        
        
def draw_out_of_bounds(surf, clr, width, x, y, z):
    #out of bounds lines
    w = z-80
    pygame.draw.line(surf, clr, [0, x], [y, x], width)
    #left
    pygame.draw.line(surf, clr, [0, x-z], [w, z], width)
    pygame.draw.line(surf, clr, [w, z], [y-w, z], width - 2)
    #right
    pygame.draw.line(surf, clr, [y-w, z], [y, x-z], width)


def draw_safety_circle(surf, clr, width, x, z):
    #safety circle
    pygame.draw.ellipse(surf, clr, [z+20, x-80, z+100, z-60], width)



def draw_yard_line(surf, clr, width, x, z):
    #18 yard line goal box
    w = 40
    pygame.draw.line(surf, clr, [z+w, z], [z-w, z+80], width)
    pygame.draw.line(surf, clr, [z-w, z+80], [x+w, z+80], width - 2)
    pygame.draw.line(surf, clr, [x+w, z+80], [x-w, z], width)
 
    
def draw_arc(surf, clr, width, z):
    #arc at the top of the goal box
    pygame.draw.arc(surf, clr, [z+110, z+60, z-80, 40], math.pi, 2 * math.pi, width)
    
    
def draw_scoreboard(w, x, y, z):
    #score board pole
    pygame.draw.rect(screen, GRAY, [w, x, y, z])

    #score board
    v = w-90
    h = w-x-z
    pygame.draw.rect(screen, BLACK, [v, y+y, h, z+y])
    pygame.draw.rect(screen, WHITE, [v+2, y+22, h-2, z+18], 2)


def draw_field_details(surf, clr, width, x, y, z):
    draw_out_of_bounds(surf, clr, width, x, y, z)
    draw_safety_circle(surf, clr, width, x, z)
    draw_yard_line(surf, clr, width, x, z)
    draw_arc(surf, clr, width, z)


def draw_goal_frame(left, top, w, h):
    # middle line coordinates
    ml_y = top + (h - 20)
    ml_left_point = [left + 20, ml_y] 
    ml_right_point = [left + w - 20, ml_y]
            
    pygame.draw.rect(screen, WHITE, [left, top, w, h], 5)
    pygame.draw.line(screen, WHITE, [ml_left_point[0], ml_y], ml_right_point, 3)
    pygame.draw.line(screen, WHITE, [left, top + h], ml_left_point, 3)
    pygame.draw.line(screen, WHITE, [left + w, top + h], ml_right_point, 3)
    pygame.draw.line(screen, WHITE, [left, top], ml_left_point, 3)
    pygame.draw.line(screen, WHITE, [left + w, top], ml_right_point, 3)


def draw_middle_net(left, top, w, h):
    # Draw Vertical Lines
    # goal frame middle line coordinates
    ml_y = top + (h - 20)
    ml_left_point = [left + 20, ml_y] 

    # Right diagonal nets start here
    right_diag_x = 0

    # Start and end points for each net line
    start_x = left + 5
    end_x = ml_left_point[0] + 1

    # Draw the vertical lines that slant left
    while start_x < end_x:
        pygame.draw.line(screen, WHITE, [start_x, top], [end_x, ml_y], 1)
        start_x += 5
        end_x += 3
        right_diag_x = (left + w) - (start_x - left + 5)

    # Draw straight vertical lines
    while start_x <= right_diag_x:
        pygame.draw.line(screen, WHITE, [start_x, top], [end_x, ml_y], 1)
        start_x += 4
        end_x += 4

    # Draw the vertical lines that slant right
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


def draw_goal(left, top, w, h):
    draw_goal_frame(left, top, w, h)
    draw_middle_net(left, top, w, h)
    draw_left_right_net(left, top, w, h)

#270, 270, 260
def draw_six_yard_line(x, y, w, h):
    pygame.draw.line(screen, WHITE, [x + 40, y - h], [x, y], 3)
    pygame.draw.line(screen, WHITE, [x, y], [x + w, y], 2)
    pygame.draw.line(screen, WHITE, [x + w, y], [x + w - 40, y - h], 3)

def draw_light_pole(x, y):
    pygame.draw.rect(screen, GRAY, [x, y, 20, 140])
    pygame.draw.ellipse(screen, GRAY, [x, y + 135, 20, 10])

    start_x = x - 40
    end_x = x + 60
    
    pygame.draw.line(screen, GRAY, [start_x, y], [end_x, y], 2)
    for i in range(1,3):
        curr_x = start_x
        for j in range(5):
            pygame.draw.ellipse(screen, light_color, [curr_x, y-20*i, 20, 20])
            curr_x += 20
        pygame.draw.line(screen, GRAY, [start_x, y-20*i], [end_x, y-20*i], 2)
    
def draw_stands(x, y, direction = 1):
    #draws stand, direction controls what direction the stand (white and red polygons) faces
    pygame.draw.polygon(screen, RED, [[x, y], [x+120*direction, y+120], [x+120*direction, y+70], [x, y-40]])
    pygame.draw.polygon(screen, WHITE, [[x, y-40], [x+120*direction, y-120], [x+120*direction, y+70]])

def draw_corner_flag(x, y, direction = 1):
    #draws corner flag, direction controls what direction the flag (both line and triangle) faces
    pygame.draw.line(screen, BRIGHT_YELLOW, [x, y], [x+5*direction, y-30], 3)
    pygame.draw.polygon(screen, RED, [[x+8*direction, y-30], [x+15*direction, y-24], [x+5*direction, y-15]])

def draw_fence(x_start, x_end, y_start, y_end):
    #draws components of fence (grid, back, poles)
    y = y_start
    for x in range(x_start, x_end, 30):
        pygame.draw.polygon(screen, NIGHT_GRAY, [[x + 2, y], [x + 2, y + 15], [x, y + 15], [x, y]])
    for x in range(x_start, x_end, 3):
        pygame.draw.line(screen, NIGHT_GRAY, [x, y], [x, y + 15], 1)

    x = 0
    for y in range(y_start, y_end, 4):
        pygame.draw.line(screen, NIGHT_GRAY, [x, y], [x + 800, y], 1)    


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

    #fence
    draw_fence(5, 800, 170, 185)


    if day:
        pygame.draw.ellipse(screen, BRIGHT_YELLOW, [520, 50, 40, 40])
    else:
        pygame.draw.ellipse(screen, WHITE, [520, 50, 40, 40]) 
        pygame.draw.ellipse(screen, sky_color, [530, 45, 40, 40])

    for c in clouds:
        draw_cloud(c[0], c[1])
    screen.blit(SEE_THROUGH, (0, 0)) 
    
    clouds_stars(s_range=200, c_range=20) 

    draw_field_details(surf=screen, clr=WHITE, width=5, x=580, y=800, z=220)

    draw_scoreboard(w=390, x=120, y=20, z=70)

    draw_goal(left=320, top=140, w=160, h=80)

    #left light pole
    draw_light_pole(150, 60)

    draw_six_yard_line(270, 270, 260, 50)

    #right light pole
    draw_light_pole(630, 60)

    #stands right
    draw_stands(680, 220, direction = 1)

    #stands left
    draw_stands(120, 220, direction = -1)

    #left corner flag
    draw_corner_flag(140, 220, -1)
    #right corner flag
    draw_corner_flag(660, 220, 1)

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