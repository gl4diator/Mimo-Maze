import turtle
import time

#initializare fereastra
wn = turtle.Screen()

#definirea nivelelor global

nivele = [""]

nivel1 = [
"XXXXXXXXXXXXXXXXXX",
"XS XXXXXXX       X",
"X  XXXXXXX  XXXXXX",
"X       XX  XXXXXX",
"X               CX",
"XXXXXX  XX  XXXXXX",
"XXXXXX  XX  XXXXXX",
"XXXXXX  XX   XXXXX",
"X  XXX        XXXX",
"X  XXX  XXXXXXXXXX",
"X                X",
"XXXXXXXXXXXX     X",
"XXXXXXXXXXXXXXXXXX",
]

#Nivelul 2
nivel2 = [
"XXXXXXXXXXXXXXXXXX",
"XXXX XXXXXXXX XXXX",
"XXXX XXXXXXXX XXXX",
"XS               X",
"XXXX XXXXXXXX XXXX",
"XXXX XXXXXXXX XXXX",
"XXXX XXXXXXXX XXXX",
"XXXX XXXXXXXX XXXX",
"XXXX XXXXXXXX XXXX",
"X                X",
"XXXX XXXXXXXX XXXX",
"XXXX XXXXXXXXCXXXX",
"XXXXXXXXXXXXXXXXXX",
]

#Nivelul 3
nivel3 = [
"XXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXX",
"XXXX          XXXX",
"XXXX          XXXX",
"XXXX XXXXXXXX XXXX",
"XXXX X  XX  X XXXX",
"XXXX XXXXXXXX XXXX",
"XS               X",
"XXXX XXXXXXXX XXXX",
"XXXX          XXXX",
"XXXX          CXXX",
"XXXXXXXXXXXXXXXXXX",
"XXXXXXXXXXXXXXXXXX",
]

#Adaug labirintul in lista de labirinte
nivele.append(nivel1)
nivele.append(nivel2)
nivele.append(nivel3)

nivel_actual = 1

class Nod():
    def __init__(self, stare, stare_anterioara, actiune):
        self.stare = stare
        self.stare_anterioara = stare_anterioara
        self.actiune = actiune

class Frontiera_lifo():
    
    #Frontiera reprezinta o lista goala initial
    def __init__(self):
        self.frontiera = []

    #functie care adauga un nod la sfarsitul listei frontiera []
    def adauga(self, nod):
        self.frontiera.append(nod)

    #functie care verifica o stare anume/particulara
    def verifica_stare(self, stare):
        return any(nod.stare == stare for nod in self.frontiera)

    #Verific daca frontiera este goala
    def frontiera_goala(self):
        return len(self.frontiera) == 0

    #Sterge din frontiera si verific intai daca nu este goala
    def sterge(self):
        if self.frontiera_goala():
            raise Exception("Frontiera goala!")
        else:
            #LIFO-last in first out (ultimul element din lista este primul scos din lista)
            nod = self.frontiera[-1] #ultimul element din lista 
            self.frontiera = self.frontiera[:-1] #inlatur acel nod din frontiera 
            return nod #returnez nodul ca rezultat

class mimo_IA(turtle.Turtle):
    def __init__(self,nivel):
        turtle.Turtle.__init__(self)
        self.hideturtle()

        wn.bgcolor("black")
        wn.bgpic("./imagini/fundal_labirint.gif")
            
        start = 0
        iesire = 0

        self.inaltime = len(nivel)
        self.lungime = max(len(linie) for linie in nivel)

        # Lista pentru stocarea coordonatelor de la ziduri
        self.ziduri = []

        for i in range(self.inaltime):
            zid = []
            for j in range(self.lungime):

                start += (nivel[i][j].count('S'))
                iesire += (nivel[i][j].count('C'))

                try:
                    if nivel[i][j] == "S":
                        self.start = (i, j)
                        zid.append(False)
                    elif nivel[i][j] == "C":
                        self.iesire = (i, j)
                        zid.append(False)
                    elif nivel[i][j] == "E":
                        zid.append(False)
                    elif nivel[i][j] == " ":
                        zid.append(False)
                    elif nivel[i][j] == "X":
                        zid.append(True)
                    else:
                        zid.append(False)
                except IndexError:
                    zid.append(False)
            self.ziduri.append(zid)

        self.solutie = None

        #Verificare daca este o singura iesire(un singur scop) si un singur start
        if start != 1:
            raise Exception("The maze should have one start point!!")
        if iesire != 1:
            raise Exception("The maze should have one Goal!!")
    
    def anima_soricel(self):
        
        soricel = turtle.Turtle()
        soricel.hideturtle()
        soricel.penup()
        soricel.shape("./imagini/soricel.gif")

        solutie = self.solutie[1] if self.solutie is not None else None
        
        for i, linie in enumerate(self.ziduri):
            for j,zid in enumerate(linie):
                if zid:
                    pass
                elif solutie is not None and (i, j) in solutie:
                    soricel.goto(-425+j*50,285-i*50)
                    soricel.showturtle()
                    time.sleep(0.1)
                    if (i, j) == self.iesire:
                        global nivel_actual
                        nivel_actual += 1
                        print(f"The shortest path:{len(self.solutie[1])} mutari")
                        wn.clearscreen()
                        nivele.pop(1)
                        try:
                            ruleaza_IA()
                        except:
                            IndexError
                            print("IA won the game!")
                            wn.clearscreen()
                            nivele.append(nivel1)
                            nivele.append(nivel2)
                            nivele.append(nivel3)
                            return False

    def afiseaza(self):
        creion = turtle.Turtle()
        creion.hideturtle()
        creion.penup()
        creion.speed(0)

        solutie = self.solutie[1] if self.solutie is not None else None

        for i, linie in enumerate(self.ziduri):
            for j, zid in enumerate(linie):
                if zid:
                    print("█", end="")
                    creion.shape("./imagini/zid1.gif")
                    if nivel_actual == 2:
                        creion.shape("./imagini/zid2.gif")
                    if nivel_actual == 3:
                        creion.shape("./imagini/zid3.gif")
                    creion.goto(-425+j*50,285-i*50)
                    creion.stamp()
                elif (i, j) == self.start:
                    print("S", end="")
                    creion.goto(-425+j*50,285-i*50)
                    creion.shape("square")
                    creion.color("green")
                    creion.shapesize(2.2)
                    creion.stamp()
                elif (i, j) == self.iesire:
                    print("C", end="")
                    creion.shape("./imagini/cascaval.gif")
                    creion.goto(-425+j*50,285-i*50)
                    creion.stamp()
                    
                elif solutie is not None and (i, j) in solutie:
                    print("*", end="") 
                    creion.goto(-425+j*50,285-i*50)
                    creion.shape("square")
                    creion.color("yellow")
                    creion.shapesize(2.2)
                    creion.stamp()
                elif solutie is not None and (i, j) in self.explorate:
                    print(" ", end="")   
                    creion.goto(-425+j*50,285-i*50)
                    creion.shape("square")
                    creion.color("blue")
                    creion.shapesize(2.2)
                    creion.stamp()
                else:
                    print(" ", end="")

            print()

    def vecini(self, stare):
        linie, coloana = stare
        optiuni = [
            ("sus", (linie - 1, coloana)),
            ("jos", (linie + 1, coloana)),
            ("stanga", (linie, coloana - 1)),
            ("dreapta", (linie, coloana + 1))
        ]

        rezultat = []
        for actiune, (r, c) in optiuni:
            if 0 <= r < self.inaltime and 0 <= c < self.lungime and not self.ziduri[r][c]:
                rezultat.append((actiune, (r, c)))
        return rezultat

    def rezolvare(self):

        self.stari_explorate = 0

        #Initializez frontiera cu pozitia de start
        start = Nod(stare=self.start, stare_anterioara=None, actiune=None)
        frontiera = Frontiera_lifo()
        frontiera.adauga(start)

        # Initializez un set de stari explorate gol
        self.explorate = set()

        # Cauta pana ce gasete o solutie.
        while True:

            #Daca frontiera este 'goala' atunci nu avem solutie
            if frontiera.frontiera_goala():
                raise Exception("The maze has no solutions!")

            # Sterge un nod din frontiera
            nod = frontiera.sterge()
            self.stari_explorate += 1

            #Daca nodul este iesirea atunci avem o solutie
            if nod.stare == self.iesire:
                actiuni = []
                celule = []
                while nod.stare_anterioara is not None:
                    actiuni.append(nod.actiune)
                    celule.append(nod.stare)
                    nod = nod.stare_anterioara
                actiuni.reverse()
                celule.reverse()
                self.solutie = (actiuni, celule)
                return

            # adauga nodul in cele explorate
            self.explorate.add(nod.stare)

            # adauga vecinii in frontiera
            for actiune, stare in self.vecini(nod.stare):
                if not frontiera.verifica_stare(stare) and stare not in self.explorate:
                    nod_nou = Nod(stare=stare, stare_anterioara=nod, actiune=actiune)
                    frontiera.adauga(nod_nou)

def ruleaza_IA():
    m=mimo_IA(nivele[1])
    print("Maze:")
    m.afiseaza()
    print("Solving...")
    m.rezolvare()
    print("Steps explored:", m.stari_explorate)
    print("Solution:")
    m.afiseaza()
    m.anima_soricel()