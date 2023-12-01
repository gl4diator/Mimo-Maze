import turtle
import math
import sys
import time
import winsound
import keyboard
import random
import IA_mimo as AI

#initialize window
window = turtle.Screen()
window.setup(900,700,startx=200,starty=-20)

#store images for later use
images = ["./images/mouse.gif","./images/wall1.gif","./images/cheese.gif",
"./images/mouse_left.gif","./images/wall2.gif","./images/wall3.gif",
"./images/lives.gif","./images/clock.gif","./images/moves_icon.gif","./images/win.gif","./images/esc.gif",
"./images/arrows.gif","./images/key_p.gif","./images/cat_left.gif","./images/cat_right.gif"
]

for image in images:
    turtle.register_shape(image)

#Interface

def interface():
    #interface design
    window.title('Mimo')
    window.bgpic("./images/background_interface.png")
    window.bgcolor("black")

    #turtle object for easy work
    pen = turtle.Turtle()
    pen.hideturtle()
    #reduce animation
    pen._tracer(0)

    #Game title
    pen.up()
    pen.goto(20,200)
    pen.color("white")
    pen.write("Mimo Maze", font=("Fire Brathers Personal Use",70,"normal"),align="center")

    #Drawing buttons

    #button1 1 "Play Mimo"
    pen.up()
    pen.goto(-115,100)
    pen.color("black")
    pen.down()
    pen.begin_fill()
    pen.fillcolor("cyan")
    for _ in range(2):
        pen.pensize(5)
        pen.forward(250)
        pen.left(90)
        pen.forward(50)
        pen.left(90)
    pen.end_fill()

    pen.up()
    pen.goto(10,101)
    pen.color("black")
    pen.write("Play Mimo", font=("Fire Brathers Personal Use",35,"normal"),align="center")

    #button 2 "Mimo AI"
    pen.up()
    pen.goto(-100,15)
    pen.down()
    pen.begin_fill()
    pen.fillcolor("cyan")
    for _ in range(2):
        pen.pensize(5)
        pen.forward(225)
        pen.left(90)
        pen.forward(50)
        pen.left(90)
    pen.end_fill()

    pen.up()
    pen.goto(10,10)
    pen.color("black")
    pen.write("Mimo AI", font=("Fire Brathers Personal Use",35,"normal"),align="center")

    #button 3 "Instructions"

    pen.up()
    pen.goto(-80,-70)
    pen.down()
    pen.begin_fill()
    pen.fillcolor("cyan")
    for _ in range(2):
        pen.pensize(5)
        pen.forward(185)
        pen.left(90)
        pen.forward(50)
        pen.left(90)
    pen.end_fill()

    pen.up()
    pen.goto(10,-70)
    pen.color("black")
    pen.write("Instructions", font=("Fire Brathers Personal Use",35,"normal"),align="center")

    #button 2 "Quit"
    pen.up()
    pen.goto(-60,-150)
    pen.down()
    pen.begin_fill()
    pen.fillcolor("cyan")
    for _ in range(2):
        pen.pensize(5)
        pen.forward(150)
        pen.left(90)
        pen.forward(50)
        pen.left(90)
    pen.end_fill()

    pen.up()
    pen.goto(11,-150)
    pen.color("black")
    pen.write("Quit", font=("Fire Brathers Personal Use",35,"normal"),align="center")

#Call interface funtion()
interface()

#Define instruction function
def instructions():
    window.bgpic("./images/background_maze.gif")

    pen2 = turtle.Turtle()
    pen2.hideturtle()
    pen2._tracer(0)
    pen2.penup()

    pen2.up()
    pen2.goto(20,200)
    pen2.color("lime")
    pen2.write("Instructions", font=("Chiller",70,"normal"),align="center")

    pen2.up()
    pen2.goto(-350,160)
    pen2.color("cyan")
    pen2.down()
    for _ in range(2):
        pen2.pensize(5)
        pen2.forward(700)
        pen2.right(90)
        pen2.forward(450)
        pen2.right(90)

    pen2.up()
    pen2.goto(-300,80)
    pen2.shape('./images/arrows.gif')
    pen2.stamp()
    pen2.up()
    pen2.shape(None)
    pen2.color("yellow")
    pen2.goto(-260,50)
    pen2.write(" - Move up,down,left,right", font=("Chiller",25,"normal"),align="left")

    pen2.up()
    pen2.goto(-300,-5)
    pen2.shape('./images/esc.gif')
    pen2.stamp()
    pen2.up()
    pen2.shape(None)
    pen2.color("yellow")
    pen2.goto(-265,-20)
    pen2.write("- Back to menu", font=("Chiller",25,"normal"),align="left")
    

    pen2.up()
    pen2.goto(-300,-80)
    pen2.shape('./images/key_p.gif')
    pen2.stamp()
    pen2.up()
    pen2.shape(None)
    pen2.color("yellow")
    pen2.goto(-265,-95)
    pen2.write("- Pause", font=("Chiller",25,"normal"),align="left")


    pen2.up()
    pen2.goto(-300,-145)
    pen2.shape('./images/lives.gif')
    pen2.color("yellow")
    pen2.stamp()
    pen2.up()
    pen2.shape(None)
    pen2.goto(-260,-160)
    pen2.write("- Lives", font=("Chiller",25,"normal"),align="left")

    pen2.up()
    pen2.goto(-300,-200)
    pen2.shape('./images/moves_icon.gif')
    pen2.color("yellow")
    pen2.stamp()
    pen2.up()
    pen2.shape(None)
    pen2.goto(-265,-220)
    pen2.write("- Moves", font=("Chiller",25,"normal"),align="left")

    pen2.up()
    pen2.goto(-300,-250)
    pen2.shape('./images/clock.gif')
    pen2.color("yellow")
    pen2.stamp()
    pen2.up()
    pen2.shape(None)
    pen2.goto(-265,-270)
    pen2.write("- Time", font=("Chiller",25,"normal"),align="left")

    pen2.up()
    pen2.goto(100,70)
    pen2.shape('./images/cat_left.gif')
    pen2.color("yellow")
    pen2.stamp()
    pen2.up()
    pen2.shape(None)
    pen2.goto(140,55)
    pen2.write("- Enemy", font=("Chiller",25,"normal"),align="left")

    pen2.up()
    pen2.goto(100,10)
    pen2.shape('./images/cheese.gif')
    pen2.color("yellow")
    pen2.stamp()
    pen2.up()
    pen2.shape(None)
    pen2.goto(140,-5)
    pen2.write("- Goal", font=("Chiller",25,"normal"),align="left")

    pen2.up()
    pen2.goto(100,-60)
    pen2.shape('./images/mouse.gif')
    pen2.color("yellow")
    pen2.stamp()
    pen2.up()
    pen2.shape(None)
    pen2.goto(140,-80)
    pen2.write("- Player", font=("Chiller",25,"normal"),align="left")


def block_keys():
    keyboard.block_key('p')
    keyboard.block_key("Up")
    keyboard.block_key("Down")
    keyboard.block_key("Left")
    keyboard.block_key("Right")
    time.sleep(1)
    keyboard.unhook_all()

#Global variabile for game pause
on_pause = False


#Game logic and functionality

def mimo_maze():
    
    #background image
    window.bgpic("./images/background_maze.gif")
    window.bgcolor("black")

    #Mouse class
    class Mouse(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape("./images/mouse.gif")
            self.penup()
            self.speed(0)
            self.lives = 3
            self.level = 1
            self.startx = 0
            self.starty = 0
            self.running = True

        def move_up(self):
            #moving spot calculate
            move_to_x = self.xcor()
            move_to_y = self.ycor() + 50

            #Check if there's a wall
            if (move_to_x, move_to_y) not in walls and mouse.running:
                winsound.PlaySound("./sounds/move.wav", winsound.SND_ASYNC)
                self.goto(move_to_x, move_to_y)
                pencile.moves += 1

        def move_down(self):
            
            #moving spot calculate
            move_to_x = mouse.xcor()
            move_to_y = mouse.ycor() - 50

            #Check if there's a wall
            if (move_to_x, move_to_y) not in walls and mouse.running:
                winsound.PlaySound("./sounds/move.wav", winsound.SND_ASYNC)
                self.goto(move_to_x, move_to_y)
                pencile.moves += 1

        def move_left(self):
            #moving spot calculate
            move_to_x = mouse.xcor() - 50
            move_to_y = mouse.ycor()
            #Check if there's a wall
            if (move_to_x, move_to_y) not in walls and mouse.running:
                self.shape("./images/mouse_left.gif")
                winsound.PlaySound("./sounds/move.wav", winsound.SND_ASYNC)
                self.goto(move_to_x, move_to_y)
                pencile.moves += 1

        def move_right(self):
            #moving spot calculate
            move_to_x = mouse.xcor() + 50
            move_to_y = mouse.ycor()
            #Check if there's a wall
            if (move_to_x, move_to_y) not in walls and mouse.running:
                self.shape("./images/mouse.gif")
                winsound.PlaySound("./sounds/move.wav", winsound.SND_ASYNC)
                self.goto(move_to_x, move_to_y)
                pencile.moves += 1

        def collision(self, another_obj):
            a = self.xcor()-another_obj.xcor()
            b = self.ycor()-another_obj.ycor()
            distance = math.sqrt((a ** 2) + (b ** 2))

            if distance < 10 :
                return True
            else:
                return False
        
        def next_level(self):
            self.up()
            self.goto(10,1)
            self.color("yellow")
            self.write(f"Level {mouse.level-1} completed!", font=("Colonna MT",40,"bold"),align="center")
            self.clear()
            levels.pop(1)
            turtle.clearstamps()
            walls.clear()
            enemies_coords.clear()
            block_keys()
            try:
                load_level(levels[1])
                if mouse.level==2:
                    for enemy in enemies_coords:
                        Enemy.movement(enemy)
                if mouse.level==3:
                    for enemy in enemies_coords:
                        Enemy.movement(enemy)
            except:
                IndexError
                mouse.running = False
                window.clearscreen()
                window.bgcolor("black")
                self.goto(0,100)
                self.shape("./images/win.gif")
                self.stamp()
                self.up()
                self.goto(0,-200)
                self.color("yellow")
                self.write("You won all levels!\nCongratulations!!", font=("Colonna MT",40,"bold"),align="center")
                time.sleep(2)
                window.clearscreen()
                interface()
                window.onscreenclick(mouse_click,1)
                turtle.done()
                
    #Enemy class
    class Enemy(turtle.Turtle):
        def __init__(self,x,y):
            turtle.Turtle.__init__(self)
            self.shape("./images/cat_left.gif")
            self.penup()
            self.startx = x
            self.starty = y
            self.speed(0)
            self.goto(x,y)
            self.direction = random.choice(["up","down","left","right"])
    
        def movement(self):
            if mouse.running:
                for cat in enemies_coords:
                    if mouse.collision(cat):
                        self.goto(self.startx,self.starty)
                        mouse.goto(mouse.startx,mouse.starty)
                if self.direction == "up":
                    x  = 0
                    y = 50
                elif self.direction == "down":
                    x = 0
                    y = -50
                elif self.direction == "left":
                    x = -50
                    y = 0
                elif self.direction == "right":
                    x = 50
                    y = 0
                else:
                    x = 0
                    y = 0
                
                move_x = self.xcor() + x
                move_y = self.ycor() + y

                if (move_x,move_y) not in walls:
                    self.goto(move_x,move_y)
                else:
                    self.direction = random.choice(["up","down","left","right"])
                    if self.direction == "right":
                        self.shape("./images/cat_right.gif")
                    elif self.direction == "left":
                        self.shape("./images/cat_left.gif")
                turtle.ontimer(self.movement,t = random.randint(100,300))

        def destroy(self):
            self.goto(2000,2000)
            self.hideturtle()

        def restart(self):
            self.goto(self.startx,self.starty)
    
    #Time class
    class Time(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.hideturtle()
            self.penup()
            self.time = 10
            self.blinkings_number = 100
    
        def counter(self):
            if mouse.running:
                window.ontimer(self.clear,1000)
                min, sec = divmod(self.time, 60)
                format_time = '{:02d}:{:02d}'.format(min, sec)
                self.goto(405,310)
                self.color("cyan")
                self.write(f'{format_time}', font=("Kristen ITC",20,"normal"),align="center")
                self.time -= 1
                window.ontimer(self.counter,1000)
            else:
                for turtle_obj in turtle.Screen()._turtles:
                    if turtle_obj is mouse:
                        min, sec = divmod(0, 60)
                        format_time = '{:02d}:{:02d}'.format(min, sec)
                        self.goto(405,310)
                        self.color("cyan")
                        self.write(f'{format_time}', font=("Kristen ITC",20,"normal"),align="center")

        def lost_life(self):
                self.goto(0,0)
                self.color("yellow")
                self.write("Time is out...\nYou lost a life!",font=("Kristen ITC",35,"normal"),align="center")
                window.update()
                winsound.PlaySound("./sounds/life_lost.wav", winsound.SND_ASYNC)
                block_keys()
                self.time = 10
                for _ in range(pencile.moves):
                    mouse.undo()
                window.update()
                pen.update_lives()
                pencile.moves=0
                keyboard.unhook_all()
    #Pen class
    class Pen(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.hideturtle()
            self.penup()
            self.moves=0

        def update_lives(self):
            self.clear()
            self.goto(-390,312)
            self.color("cyan")
            self.write(f'{mouse.lives}', font=("Kristen ITC",20,"normal"),align="center")
        
        def update_moves(self):
            self.clear()
            self.goto(-335,312)
            self.color("cyan")
            self.write(f'{self.moves}', font=("Kristen ITC",20,"normal"),align="center")
        
        def life_lost(self):
            self.penup()
            self.goto(0,0)
            self.color("yellow")
            winsound.PlaySound("./sounds/life_lost.wav", winsound.SND_ASYNC)
            self.write('\t      OH, NO!!\nThe cat caught you! You lost a life', font=("Kristen ITC",30,"normal"),align="center")
            window.update()
            block_keys()
            pen_time.time = 10
            pencile.moves=0
            pen.update_lives()

        def out_of_lives(self):
                mouse.running = False
                pencile.update_moves()
                self.penup()
                self.goto(0,0)
                self.color("yellow")
                self.write('Out of lives..\nGame Over!', font=("Kristen ITC",30,"normal"),align="center")
                window.update()
                block_keys()
                blinking_text()
                window.listen()
                window.onkey(back_to_interaface,"Return")
                
    
    #Goal class
    class Cheese(turtle.Turtle):
        def __init__(self,x,y):
            turtle.Turtle.__init__(self)
            self.shape("./images/cheese.gif")
            self.penup()
            self.speed(0)
            self.goto(x,y)
        
        def destroy(self):
            self.goto(2000,2000)
            self.hideturtle()

    #Store levels
    levels = [""]

    #First level
    level1 = [
    "XXXXXXXXXXXXXXXXXX",
    "XS XXXXXXX       X",
    "X  XXXXXXX  XXXXXX",
    "X       XX  XXXXXX",
    "X           P   CX",
    "XXXXXX  XX  XXXXXX",
    "XXXXXX  XX  XXXXXX",
    "XXXXXX  XX   XXXXX",
    "X  XXX        XXXX",
    "X  XXX  XXXXXXXXXX",
    "X                X",
    "XXXXXXXXXXXX     X",
    "XXXXXXXXXXXXXXXXXX",
    ]

    #Second level
    level2 = [
    "XXXXXXXXXXXXXXXXXX",
    "XXXX XXXXXXXX XXXX",
    "XXXX XXXXXXXX XXXX",
    "XS            P  X",
    "XXXX XXXXXXXX XXXX",
    "XXXX XXXXXXXX XXXX",
    "XXXX XXXXXXXX XXXX",
    "XXXX XXXXXXXX XXXX",
    "XXXX XXXXXXXX XXXX",
    "X           P    X",
    "XXXX XXXXXXXX XXXX",
    "XXXX XXXXXXXXCXXXX",
    "XXXXXXXXXXXXXXXXXX",
    ]

    #Third level
    level3 = [
    "XXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXX",
    "XXXX  P       XXXX",
    "XXXX       P  XXXX",
    "XXXX XXXXXXXX XXXX",
    "XXXX X  XX  X XXXX",
    "XXXX XXXXXXXX XXXX",
    "XS               X",
    "XXXX XXXXXXXX XXXX",
    "XXXX       P  XXXX",
    "XXXX    P     CXXX",
    "XXXXXXXXXXXXXXXXXX",
    "XXXXXXXXXXXXXXXXXX",
    ]

    #Goal coordinates
    exit_coords = []

    #list with coordinates coordiantes 

    enemies_coords = []

    #list with walls coordinates
    walls = []

    #Add the level to the list of levels
    levels.append(level1)
    levels.append(level2)
    levels.append(level3)
    
    #Levels load
    def load_level(level):
        for y in range(len(level)):
            for x in range(len(level[y])):

                character = level[y][x]

                coord_x = -425 + (x*50)
                coord_y = 285 - (y*50)

                if character == "X":
                    turtle.penup()
                    turtle.speed(0)
                    turtle.goto(coord_x,coord_y)
                    turtle.shape("./images/wall1.gif")
                    if mouse.level==2:
                        turtle.shape("./images/wall2.gif")
                    elif mouse.level==3:
                        turtle.shape("./images/wall3.gif")
                    turtle.stamp()

                    walls.append((coord_x,coord_y))
                
                if character == "S":
                    mouse.goto(coord_x,coord_y)
                    mouse.startx = coord_x
                    mouse.starty = coord_y

                if character == "C":
                    exit_coords.append(Cheese(coord_x,coord_y))

                if character == "P":
                    enemies_coords.append(Enemy(coord_x,coord_y))

        creion = turtle.Turtle()
        creion.shape("./images/lives.gif")
        creion.penup()
        creion.goto(-422,330)
        creion.stamp()
        creion.penup()
        creion.goto(350,330)
        creion.shape("./images/clock.gif")
        creion.stamp()
        creion.penup()
        creion.goto(-364,330)
        creion.shape("./images/moves_icon.gif")
        creion.stamp()

    #mouse object
    mouse = Mouse()

    pen_time = Time()
    pen = Pen()
    pencile = Pen()
    #keep referrence to turtles you want to keep
    turtles_to_keep = [pen_time]

    #function to get back in the interface
    def back_to_interaface():
        for turtle_obj in turtle.Screen()._turtles:
            if turtle_obj not in turtles_to_keep:
                turtle_obj.reset()
                turtle_obj.hideturtle()
                turtle_obj.getscreen()._turtles.remove(turtle_obj)
        window.clearscreen()
        interface()
        window.onscreenclick(mouse_click,1)
        window.listen()
        turtle.done()

    #call list of levels function with first level

    load_level(levels[1])

    pen_time.counter()

    pen.update_lives()
    
    pic = turtle.Turtle()
    pic.hideturtle()


    blinking_turtle = turtle.Turtle()
    blinking_turtle.hideturtle()

    def blinking_text():
        for turtle_obj in turtle.Screen()._turtles:
            if turtle_obj is mouse and pen_time.blinkings_number > 0:
                window.ontimer(blinking_turtle.clear,600)
                blinking_turtle.penup()
                blinking_turtle.goto(0,window.window_height()/2-40)
                blinking_turtle.color("yellow")
                blinking_turtle.write(f'{"Press enter key to exit"}', font=("Kristen ITC",20,"normal"),align="center")
                pen_time.blinkings_number -= 1
                blinking_turtle.hideturtle()
                time.sleep(0.3)
                window.ontimer(blinking_text,600)

    def pause():
        global on_pause
        if on_pause == True:
            on_pause = False
            pic.clear()
            mouse.running = True
            window.onkey(mouse.move_left,"Left")
            window.onkey(mouse.move_right,"Right")
            window.onkey(mouse.move_up,"Up")
            window.onkey(mouse.move_down,"Down")
            for enemy in enemies_coords:
                Enemy.movement(enemy)
        else:
            on_pause = True
            pic.penup()
            pic.goto(10,1)
            pic.color("yellow")
            pic.write("Game paused!", font=("Colonna MT",40,"bold"),align="center")
            mouse.running=False
            window.onkey(None, "Up")
            window.onkey(None, "Down")
            window.onkey(None, "Left")
            window.onkey(None, "Right")

    #Waiting for a key
    window.listen()
    window.onkey(mouse.move_left,"Left")
    window.onkey(mouse.move_right,"Right")
    window.onkey(mouse.move_up,"Up")
    window.onkey(mouse.move_down,"Down")
    window.onkey(pause,"p")

    for enemy in enemies_coords:
        Enemy.movement(enemy)

    while True:
        if mouse.running:
            pencile.update_moves()
            for cheese in exit_coords:
                if mouse.collision(cheese):
                    Cheese.destroy(cheese)
                    window.update()
                    mouse.level += 1
                    for enemy in enemies_coords:
                        Enemy.destroy(enemy)
                    mouse.next_level()
                    pen_time.time = 10
                    pencile.moves = 0
            
            for enemy in enemies_coords:
                if mouse.collision(enemy):
                    mouse.lives -=1
                    pen.life_lost() 
                    #time.sleep(1.5)

            if pen_time.time < 0 :
                mouse.lives -= 1
                for enemy in enemies_coords:
                    Enemy.restart(enemy)

                if mouse.lives >= 1:
                    pen_time.lost_life()

            if mouse.lives == 0:
                pen.update_lives()
                pen.out_of_lives()

            if keyboard.is_pressed('Escape'):
                mouse.running = False
                window.clearscreen()
                interface()
                window.onscreenclick(mouse_click,1)
                turtle.done()
                break
        window.update()

#Check mouse click
def mouse_click(x,y):
    
    if x <= 136 and x >=-117 and y >= 100 and y <= 150:
        window.clearscreen()     
        #reduce animation
        window.tracer(0)
        mimo_maze()

    elif x <= 125 and x >= -101 and y >= 16 and y <= 65:
        window.clearscreen()
        while True:
            AI.run_AI()
            break
        interface()
        window.onscreenclick(mouse_click,1)
        turtle.done()
    
    elif x <= 105 and x >= -82 and y >= -70 and y <= -20:
        window.clearscreen()
        instructions()
        while True:
            if keyboard.is_pressed('Escape'):
                window.clearscreen()
                interface()
                window.onscreenclick(mouse_click,1)
                turtle.done()
                break
            window.update()
                
    elif x>=-62 and x <= 91 and y  <=-98 and y >= -149:
        turtle.bye()

window.onscreenclick(mouse_click,1)
window.listen()

turtle.done()
