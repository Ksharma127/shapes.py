import pgzrun

#setting output windows width and height of screen 

WIDTH= 500
HEIGHT=600

#title of the output window 
TITLE = "First shapes project"

#adding or putting the things on the screen 
def draw():
    corner1 =(0,0)
    corner2 =(150,130)
    rectangle=Rect(corner1,corner2)
    #adding the created rectangle on screen 
    screen.draw.filled_rect(rectangle,(0,255,0))#0,255,0 is rgb value of the colour of green
    #drawing a line
    #start point,end point, color
    screen.draw.line((300,300),(500,500),(255,0,0))






pgzrun.go()
