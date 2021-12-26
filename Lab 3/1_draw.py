import pygame
from pygame.draw import *
from random import randint

pygame.init()


# Colors
black = 0, 0, 0
white = 255, 255, 255
light_grey = 220, 220, 220
grey = 192, 192, 192
dark_grey = 60, 60, 60
red = 255, 0, 0
purple = 160, 35, 255
pink = 255, 96, 208
light_green = 96, 255, 128
green = 0, 255, 0
light_blue = 80, 208, 255
blue = 0, 0, 255
yellow = 225, 225, 0
orange = 255, 160, 20
brown = 160, 130, 100


# Window settings
FPS = 30
SIZE_X = 1000
SIZE_Y = 500

win = pygame.display.set_mode((SIZE_X, SIZE_Y))


# Background
rect(win, (light_blue),(0, 0, SIZE_X, (SIZE_Y // 3) * 2 - 10))
rect(win, (blue),(0, 0 + (SIZE_Y // 3) *2, SIZE_X, SIZE_Y))


# Just to practice
def window_center_aim():    # Sized for window width 1000pix
    test = 310

    for i in range(20):
        rect(win, (black), (test, SIZE_Y//2 + 20, 10, 10))
        test += 20

    rect(win, (black), (SIZE_X//2, SIZE_Y//2 + 20, 10, 100))    


# Main defines
def draw_clouds(x, y):
    r= (SIZE_X + SIZE_Y) // 50

    for i in range(randint(2, 4)):
        cloud_size = randint(r, r+10)

        circle(win, (white), (x, y), cloud_size, 0)
        circle(win, (light_blue), (x, y), cloud_size, 4)

        y-=30
        x+=30
        cloud_size = randint(r, r+10)

        circle(win, (white), (x, y), cloud_size, 0)
        circle(win, (light_blue), (x, y), cloud_size, 4)

        y-=30
        x+=30
        cloud_size = randint(r, r+10)

        circle(win, (white), (x, y), cloud_size, 0)
        circle(win, (light_blue), (x, y), cloud_size, 4)
        y+=60

    cloud_size = randint(r, r+10)

    circle(win, (white), (x, y), cloud_size, 0)
    circle(win, (light_blue), (x, y), cloud_size, 4)


def vertical_parallel_lines(lines_color, coordinate_x, coordinate_y, width,
                            height, parts_count, line_width):
    """ Drawing verical paralel lines in rectangle
        coordinate_x - coordinate x where rectangle begin 
        coordinate_y - coordinate y where rectangle begin
        width - width of rectangle
        height - height of rectangle
        parts_count - number of parts what rectangle divided
        line_width - lines width
    """
    step = ((width + (parts_count + line_width)) - coordinate_x) // parts_count
    first_line_x = coordinate_x + step
    
    for i in range(parts_count - 1):
        line(win, lines_color, (first_line_x, coordinate_y), 
            (first_line_x, coordinate_y + height), line_width)
        
        first_line_x += step


def horisontal_parallel_lines(lines_color, coordinate_x, coordinate_y, width,
                              height, parts_count, line_width):
    """ Drawing horisontal paralel lines in rectangle:
        coordinate_x - coordinate x where rectangle begin 
        coordinate_y - coordinate y where rectangle begin
        width - width of rectangle
        height - height of rectangle
        parts_count - number of parts what rectangle divided
        line_width - lines width
    """
    step = ((height + (parts_count + line_width)) - coordinate_y) // (parts_count )
    first_line_y = coordinate_y + step - 5

    
    for i in range(parts_count - 1):
        line(win, lines_color, (coordinate_x, first_line_y),
            (coordinate_x + width, first_line_y + 10), line_width)
        
        first_line_y += step


def draw_boat_frame(frame_color, x, y, width, height):
    """Drawing boat frame"""
   
    #Boat frame
    global boat_frame 
    boat_frame = height // 5
    
    rect(win, (frame_color), (x - width//2, y, width, boat_frame))
    rect(win, (black), (x - width//2, y, width, boat_frame),2)
    
    #Boat frame backside circle
    circle(win, (frame_color), (x - width//2, y), boat_frame, 0, False, False, True)
    circle(win, (black), (x - width//2, y), boat_frame, 2, False, False, True)
    
    #Boat frame frontside triangle
    point_1 = x + width//2, y
    point_2 = x + width, y 
    point_3 = x + width//2, y+boat_frame
    point_4 = x + width//2, y 
    
    polygon(win, frame_color, (point_1, point_2, point_3, point_4), 0)
    polygon(win, black, (point_1, point_2, point_3, point_4), 2)
    
    #Boat frame front window
    point_5x = (x + width//2) + ((width//2) / 7)
    point_5y = y + boat_frame / 2

    circle(win, (white), (point_5x, point_5y), boat_frame//4, )
    circle(win, (black), (point_5x, point_5y), boat_frame//4, 4)
    
    #Boat frame windows
    point_6x = x - (width // 8) * 3 
    point_6y = y + boat_frame / 2
    
    for i in range(7):
        circle(win, (white), (point_6x, point_6y), boat_frame//4)
        circle(win, (black), (point_6x, point_6y), boat_frame//4, 4)
        point_6x += width//8

    #Line from frame to backside circle
    line_start = x - width//2, y
    line_end = x - (width//2 + boat_frame), y

    line(win, (black), line_start, line_end, 2)


def draw_boat_macht( macht_color, x, y, width, height):
    """Drawing boat macht"""
    macht_x = x - width//6
    macht_y = y - height//5 * 4
    macht_height = height - height // 5
    macht_width = width // 20

    rect(win, (macht_color), (macht_x, macht_y, macht_width, macht_height))
    rect(win, (black), (macht_x, macht_y, macht_width, macht_height), 2)

    horisontal_parallel_lines(brown, macht_x, macht_y, macht_width,
                              y, 8, 3)


def draw_boat_sail(sail_color,  x, y, width, height):
    """Drawing boat sail"""
    point_1= x - width//6 + width // 20, y - height // 5 * 4
    point_2= x + width // 3, y - height // 3
    point_3= x - width//6 + width // 20, y 
    point_4= x, y - height // 3
    
    polygon(win, sail_color, (point_1, point_2, point_3, point_4, point_1),0)
    polygon(win, black, (point_1, point_2,  point_4, point_1),1)
    polygon(win, black, (point_2, point_3, point_4, point_2),1)


def draw_boat(frame_color, macht_color, sail_color, x, y, width, height):
    draw_boat_frame(frame_color, x, y, width, height)
    draw_boat_macht(macht_color, x, y, width, height)
    draw_boat_sail(sail_color,  x, y, width, height)


def draw_sun(x, y, sun_radius):   # TODO: maded just 1 ray.
        point_1= x - sun_radius // 2, y
        point_2= x, y - sun_radius // 40
        point_3= x + sun_radius // 2, y 
        point_4= x, y + sun_radius // 40 
                
        for i in range(4):
            polygon(win, yellow, (point_1, point_2, point_3, point_4, point_1 ), 0)
            polygon(win, black, (point_1, point_2,  point_4, ), 2)
            polygon(win, black, (point_2, point_3, point_4, point_2), 2)

           
# Main window picture
window_center_aim() 

draw_sun(SIZE_X // 2, SIZE_Y // 2, 500)

draw_clouds(100, 150)
draw_clouds(600, 150)
draw_boat(brown, orange, light_green, 300, 450, 300, 300)


# Main cicle
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    
    pygame.display.update()

pygame.display.update()

pygame.quit()