import turtle
import math
import sys
import time
import winsound
import keyboard
import random
import IA_mimo as AI

#initialize window
fereastra = turtle.Screen()
fereastra.setup(900,700,startx=200,starty=-20)

#store images for later use
imagini = ["./imagini/soricel.gif","./imagini/zid1.gif","./imagini/cascaval.gif",
"./imagini/soricel_stanga.gif","./imagini/zid2.gif","./imagini/zid3.gif",
"./imagini/vieti.gif","./imagini/ceas.gif","./imagini/mutari_icon.gif","./imagini/castig.gif","./imagini/esc.gif",
"./imagini/sageti.gif","./imagini/tasta_p.gif","./imagini/pisica_stanga.gif","./imagini/pisica_dreapta.gif"
]

for imagine in imagini:
    turtle.register_shape(imagine)

#Interface

def interfata():
    #interface design
    fereastra.title('Mimo')
    fereastra.bgpic("./imagini/fundal_interfata.png")
    fereastra.bgcolor("black")

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
interfata()

#Define instruction function
def intstructiuni():
    fereastra.bgpic("./imagini/fundal_labirint.gif")

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
    pen2.shape('./imagini/sageti.gif')
    pen2.stamp()
    pen2.up()
    pen2.shape(None)
    pen2.color("yellow")
    pen2.goto(-260,50)
    pen2.write(" - Move up,down,left,right", font=("Chiller",25,"normal"),align="left")

    pen2.up()
    pen2.goto(-300,-5)
    pen2.shape('./imagini/esc.gif')
    pen2.stamp()
    pen2.up()
    pen2.shape(None)
    pen2.color("yellow")
    pen2.goto(-265,-20)
    pen2.write("- Back to menu", font=("Chiller",25,"normal"),align="left")
    

    pen2.up()
    pen2.goto(-300,-80)
    pen2.shape('./imagini/tasta_p.gif')
    pen2.stamp()
    pen2.up()
    pen2.shape(None)
    pen2.color("yellow")
    pen2.goto(-265,-95)
    pen2.write("- Pause", font=("Chiller",25,"normal"),align="left")


    pen2.up()
    pen2.goto(-300,-145)
    pen2.shape('./imagini/vieti.gif')
    pen2.color("yellow")
    pen2.stamp()
    pen2.up()
    pen2.shape(None)
    pen2.goto(-260,-160)
    pen2.write("- Lives", font=("Chiller",25,"normal"),align="left")

    pen2.up()
    pen2.goto(-300,-200)
    pen2.shape('./imagini/mutari_icon.gif')
    pen2.color("yellow")
    pen2.stamp()
    pen2.up()
    pen2.shape(None)
    pen2.goto(-265,-220)
    pen2.write("- Moves", font=("Chiller",25,"normal"),align="left")

    pen2.up()
    pen2.goto(-300,-250)
    pen2.shape('./imagini/ceas.gif')
    pen2.color("yellow")
    pen2.stamp()
    pen2.up()
    pen2.shape(None)
    pen2.goto(-265,-270)
    pen2.write("- Time", font=("Chiller",25,"normal"),align="left")

    pen2.up()
    pen2.goto(100,70)
    pen2.shape('./imagini/pisica_stanga.gif')
    pen2.color("yellow")
    pen2.stamp()
    pen2.up()
    pen2.shape(None)
    pen2.goto(140,55)
    pen2.write("- Enemy", font=("Chiller",25,"normal"),align="left")

    pen2.up()
    pen2.goto(100,10)
    pen2.shape('./imagini/cascaval.gif')
    pen2.color("yellow")
    pen2.stamp()
    pen2.up()
    pen2.shape(None)
    pen2.goto(140,-5)
    pen2.write("- Goal", font=("Chiller",25,"normal"),align="left")

    pen2.up()
    pen2.goto(100,-60)
    pen2.shape('./imagini/soricel.gif')
    pen2.color("yellow")
    pen2.stamp()
    pen2.up()
    pen2.shape(None)
    pen2.goto(140,-80)
    pen2.write("- Player", font=("Chiller",25,"normal"),align="left")



#Global variabile for game pause
pe_pauza = False


#Game logic and functionality

def labirint_mimo():
    
    #background image
    fereastra.bgpic("./imagini/fundal_labirint.gif")
    fereastra.bgcolor("black")

    #Mouse class
    class Soricel(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape("./imagini/soricel.gif")
            self.penup()
            self.speed(0)
            self.vieti = 3
            self.nivel = 1
            self.startx = 0
            self.starty = 0
            self.ruleaza = True

        def misca_sus(self):
            #moving spot calculate
            muta_la_x = self.xcor()
            muta_la_y = self.ycor() + 50

            #Check if there's a wall
            if (muta_la_x, muta_la_y) not in ziduri:
                winsound.PlaySound("./sunete/muta.wav", winsound.SND_ASYNC)
                self.goto(muta_la_x, muta_la_y)
                stilou.mutari += 1

        def misca_jos(self):
            
            #moving spot calculate
            muta_la_x = soricel.xcor()
            muta_la_y = soricel.ycor() - 50

            #Check if there's a wall
            if (muta_la_x, muta_la_y) not in ziduri:
                winsound.PlaySound("./sunete/muta.wav", winsound.SND_ASYNC)
                self.goto(muta_la_x, muta_la_y)
                stilou.mutari += 1

        def misca_stanga(self):
            #moving spot calculate
            muta_la_x = soricel.xcor() - 50
            muta_la_y = soricel.ycor()
            self.shape("./imagini/soricel_stanga.gif")
            #Check if there's a wall
            if (muta_la_x, muta_la_y) not in ziduri:
                winsound.PlaySound("./sunete/muta.wav", winsound.SND_ASYNC)
                self.goto(muta_la_x, muta_la_y)
                stilou.mutari += 1

        def misca_dreapta(self):
            #moving spot calculate
            muta_la_x = soricel.xcor() + 50
            muta_la_y = soricel.ycor()
            self.shape("./imagini/soricel.gif")
            #Check if there's a wall
            if (muta_la_x, muta_la_y) not in ziduri:
                winsound.PlaySound("./sunete/muta.wav", winsound.SND_ASYNC)
                self.goto(muta_la_x, muta_la_y)
                stilou.mutari += 1

        def coliziune(self, alt_obiect):
            a = self.xcor()-alt_obiect.xcor()
            b = self.ycor()-alt_obiect.ycor()
            distanta = math.sqrt((a ** 2) + (b ** 2))

            if distanta < 10 :
                return True
            else:
                return False
        
        def urmatorul_nivel(self):
            self.up()
            self.goto(10,1)
            self.color("yellow")
            self.write(f"Level {soricel.nivel-1} completed!", font=("Colonna MT",40,"bold"),align="center")
            keyboard.block_key("Up")
            keyboard.block_key("Down")
            keyboard.block_key("Left")
            keyboard.block_key("Right")
            time.sleep(2)
            keyboard.unhook_all()
            self.clear()
            nivele.pop(1)
            turtle.clearstamps()
            ziduri.clear()
            coordonate_inamici.clear()
            try:
                incarcare_nivel(nivele[1])
                if soricel.nivel==2:
                    for inamic in coordonate_inamici:
                        Inamic.miscare(inamic)
                if soricel.nivel==3:
                    for inamic in coordonate_inamici:
                        Inamic.miscare(inamic)
            except:
                IndexError
                soricel.ruleaza = False
                fereastra.clearscreen()
                fereastra.bgcolor("black")
                self.goto(0,100)
                self.shape("./imagini/castig.gif")
                self.stamp()
                self.up()
                self.goto(0,-200)
                self.color("yellow")
                self.write("You won all levels!\nCongratulations!!", font=("Colonna MT",40,"bold"),align="center")
                time.sleep(2)
                fereastra.clearscreen()
                interfata()
                fereastra.onscreenclick(mouse_click,1)
                turtle.done()
                
    #Enemy class
    class Inamic(turtle.Turtle):
        def __init__(self,x,y):
            turtle.Turtle.__init__(self)
            self.shape("./imagini/pisica_stanga.gif")
            self.penup()
            self.startx = x
            self.starty = y
            self.speed(0)
            self.goto(x,y)
            self.directie = random.choice(["sus","jos","stanga","dreapta"])
    
        def miscare(self):
            if soricel.ruleaza:
                for pisica in coordonate_inamici:
                    if soricel.coliziune(pisica):
                        self.goto(self.startx,self.starty)
                        soricel.goto(soricel.startx,soricel.starty)
                if self.directie == "sus":
                    x  = 0
                    y = 50
                elif self.directie == "jos":
                    x = 0
                    y = -50
                elif self.directie == "stanga":
                    x = -50
                    y = 0
                elif self.directie == "dreapta":
                    x = 50
                    y = 0
                else:
                    x = 0
                    y = 0
                
                muta_x = self.xcor() + x
                muta_y = self.ycor() + y

                if (muta_x,muta_y) not in ziduri:
                    self.goto(muta_x,muta_y)
                else:
                    self.directie = random.choice(["sus","jos","stanga","dreapta"])
                    if self.directie == "dreapta":
                        self.shape("./imagini/pisica_dreapta.gif")
                    elif self.directie == "stanga":
                        self.shape("./imagini/pisica_stanga.gif")
                turtle.ontimer(self.miscare,t = random.randint(100,300))

        def distruge(self):
            self.goto(2000,2000)
            self.hideturtle()

        def restart(self):
            self.goto(self.startx,self.starty)
    
    #Time class
    class Timp(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.hideturtle()
            self.penup()
            self.timp = 10
    
        def contor_timp(self):
            if soricel.ruleaza:
                fereastra.ontimer(self.clear,1000)
                min, sec = divmod(self.timp, 60)
                formatimp = '{:02d}:{:02d}'.format(min, sec)
                self.goto(405,310)
                self.color("cyan")
                self.write(f'{formatimp}', font=("Kristen ITC",20,"normal"),align="center")
                self.timp -= 1
            fereastra.ontimer(self.contor_timp,1000)
            

        def viata_pierduta(self):
                self.goto(0,0)
                self.color("yellow")
                self.write("Time is out...\nYou lost a life!",font=("Kristen ITC",35,"normal"),align="center")
                fereastra.update()
                winsound.PlaySound("./sunete/viata_pierduta.wav", winsound.SND_ASYNC)
                keyboard.block_key('p')
                keyboard.block_key("Up")
                keyboard.block_key("Down")
                keyboard.block_key("Left")
                keyboard.block_key("Right")
                time.sleep(2)
                keyboard.unhook_all()
                self.timp = 10
                for _ in range(stilou.mutari):
                    soricel.undo()
                fereastra.update()
                pix.update_vieti()
                stilou.mutari=0
    #Pen class
    class Pix(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.hideturtle()
            self.penup()
            self.mutari=0

        def update_vieti(self):
            self.clear()
            self.goto(-390,312)
            self.color("cyan")
            self.write(f'{soricel.vieti}', font=("Kristen ITC",20,"normal"),align="center")
        
        def update_mutari(self):
            self.clear()
            self.goto(-335,312)
            self.color("cyan")
            self.write(f'{self.mutari}', font=("Kristen ITC",20,"normal"),align="center")
        
        def pierdere_viata(self):
            self.penup()
            self.goto(0,0)
            self.color("yellow")
            self.write('\t      OH, NO!!\nThe cat caught you! You lost a life', font=("Kristen ITC",30,"normal"),align="center")
            fereastra.update()
            winsound.PlaySound("./sunete/viata_pierduta.wav", winsound.SND_ASYNC)
            keyboard.block_key('p')
            keyboard.block_key("Up")
            keyboard.block_key("Down")
            keyboard.block_key("Left")
            keyboard.block_key("Right")
            time.sleep(2)
            keyboard.unhook_all()
            timp.timp = 10
            stilou.mutari=0
            pix.update_vieti()

        def fara_vieti(self):
                soricel.ruleaza = False
                stilou.update_mutari()
                self.penup()
                self.goto(0,0)
                self.color("yellow")
                self.write('Out of lives..\nGame Over!', font=("Kristen ITC",30,"normal"),align="center")
                fereastra.update()
                
                keyboard.block_key('p')
                keyboard.block_key("Up")
                keyboard.block_key("Down")
                keyboard.block_key("Left")
                keyboard.block_key("Right")
                time.sleep(2)
                fereastra.clearscreen()
                interfata()
                keyboard.unhook_all()
                fereastra.onscreenclick(mouse_click,1)
                fereastra.listen()
                turtle.done()
    
    #Goal class
    class Cascaval(turtle.Turtle):
        def __init__(self,x,y):
            turtle.Turtle.__init__(self)
            self.shape("./imagini/cascaval.gif")
            self.penup()
            self.speed(0)
            self.goto(x,y)
        
        def distruge(self):
            self.goto(2000,2000)
            self.hideturtle()

    #Store levels
    nivele = [""]

    #First level
    nivel1 = [
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
    nivel2 = [
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
    nivel3 = [
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
    coordonate_iesire = []

    #list with coordinates coordiantes 

    coordonate_inamici = []

    #list with walls coordinates
    ziduri = []

    #Add the level to the list of levels
    nivele.append(nivel1)
    nivele.append(nivel2)
    nivele.append(nivel3)
    
    #Levels load
    def incarcare_nivel(nivel):
        for y in range(len(nivel)):
            for x in range(len(nivel[y])):

                caracter = nivel[y][x]

                coordonata_x = -425 + (x*50)
                coordonata_y = 285 - (y*50)

                if caracter == "X":
                    turtle.penup()
                    turtle.speed(0)
                    turtle.goto(coordonata_x,coordonata_y)
                    turtle.shape("./imagini/zid1.gif")
                    if soricel.nivel==2:
                        turtle.shape("./imagini/zid2.gif")
                    elif soricel.nivel==3:
                        turtle.shape("./imagini/zid3.gif")
                    turtle.stamp()

                    ziduri.append((coordonata_x,coordonata_y))
                
                if caracter == "S":
                    soricel.goto(coordonata_x,coordonata_y)
                    soricel.startx = coordonata_x
                    soricel.starty = coordonata_y

                if caracter == "C":
                    coordonate_iesire.append(Cascaval(coordonata_x,coordonata_y))

                if caracter == "P":
                    coordonate_inamici.append(Inamic(coordonata_x,coordonata_y))
                    timp.inamic_startx = coordonata_x
                    timp.inamic_starty = coordonata_y

        creion = turtle.Turtle()
        creion.shape("./imagini/vieti.gif")
        creion.penup()
        creion.goto(-422,330)
        creion.stamp()
        creion.penup()
        creion.goto(350,330)
        creion.shape("./imagini/ceas.gif")
        creion.stamp()
        creion.penup()
        creion.goto(-364,330)
        creion.shape("./imagini/mutari_icon.gif")
        creion.stamp()

    #mouse object
    soricel = Soricel()

    timp = Timp()
    pix = Pix()
    stilou = Pix()

    #call list of levels function with first level

    incarcare_nivel(nivele[1])

    timp.contor_timp()

    pix.update_vieti()
    
    pic = turtle.Turtle()
    pic.hideturtle()

    def pune_pauza():
        global pe_pauza
        if pe_pauza == True:
            pe_pauza = False
            pic.clear()
            soricel.ruleaza = True
            fereastra.onkey(soricel.misca_stanga,"Left")
            fereastra.onkey(soricel.misca_dreapta,"Right")
            fereastra.onkey(soricel.misca_sus,"Up")
            fereastra.onkey(soricel.misca_jos,"Down")
            for inamic in coordonate_inamici:
                Inamic.miscare(inamic)
        else:
            pe_pauza = True
            pic.penup()
            pic.goto(10,1)
            pic.color("yellow")
            pic.write("Game paused!", font=("Colonna MT",40,"bold"),align="center")
            soricel.ruleaza=False
            fereastra.onkey(None, "Up")
            fereastra.onkey(None, "Down")
            fereastra.onkey(None, "Left")
            fereastra.onkey(None, "Right")

    #Asteptarea unei taste
    fereastra.listen()
    fereastra.onkey(soricel.misca_stanga,"Left")
    fereastra.onkey(soricel.misca_dreapta,"Right")
    fereastra.onkey(soricel.misca_sus,"Up")
    fereastra.onkey(soricel.misca_jos,"Down")
    fereastra.onkey(pune_pauza,"p")

    for inamic in coordonate_inamici:
        Inamic.miscare(inamic)

    while True:
        if soricel.ruleaza:
            stilou.update_mutari()
            for cascaval in coordonate_iesire:
                if soricel.coliziune(cascaval):
                    Cascaval.distruge(cascaval)
                    fereastra.update()
                    soricel.nivel += 1
                    for inamic in coordonate_inamici:
                        Inamic.distruge(inamic)
                    soricel.urmatorul_nivel()
                    timp.timp = 10
                    stilou.mutari = 0
            
            for inamic in coordonate_inamici:
                if soricel.coliziune(inamic):
                    soricel.vieti -=1
                    pix.pierdere_viata()

            if timp.timp < 0 :
                soricel.vieti -= 1
                for inamic in coordonate_inamici:
                    Inamic.restart(inamic)
                if soricel.vieti >= 1:
                    timp.viata_pierduta()

            if soricel.vieti == 0:
                pix.update_vieti()
                pix.fara_vieti()

            if keyboard.is_pressed('Escape'):
                soricel.ruleaza = False
                fereastra.clearscreen()
                interfata()
                fereastra.onscreenclick(mouse_click,1)
                turtle.done()
                break
        fereastra.update()

#Check mouse click
def mouse_click(x,y):
    
    if x <= 136 and x >=-117 and y >= 100 and y <= 150:
        fereastra.clearscreen()     
        #reduce animation
        fereastra.tracer(0)
        labirint_mimo()

    elif x <= 125 and x >= -101 and y >= 16 and y <= 65:
        fereastra.clearscreen()
        while True:    
            AI.ruleaza_IA()
            break
        interfata()
        fereastra.onscreenclick(mouse_click,1)
        turtle.done()
    
    elif x <= 105 and x >= -82 and y >= -70 and y <= -20:
        fereastra.clearscreen()
        intstructiuni()
        while True:
            if keyboard.is_pressed('Escape'):
                fereastra.clearscreen()
                interfata()
                fereastra.onscreenclick(mouse_click,1)
                turtle.done()
                break
            fereastra.update()
                
    elif x>=-62 and x <= 91 and y  <=-98 and y >= -149:
        sys.exit(0)

fereastra.onscreenclick(mouse_click,1)
fereastra.listen()

turtle.done()
