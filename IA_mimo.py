import turtle
import time
import keyboard

#intialize turtle window
wn = turtle.Screen()

#define levels globally

levels = [""]

level1 = [
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

#level 2
level2 = [
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

#level 3
level3 = [
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

#Add maze in the list of mazes
levels.append(level1)
levels.append(level2)
levels.append(level3)

current_level = 1

class Node():
    def __init__(self, state, previous_state, action):
        self.state = state
        self.previous_state = previous_state
        self.action = action

class frontier_lifo():
    
    #the frontier is a empty list at the start
    def __init__(self):
        self.frontier = []
    #function to add a node to the end of the frontier list
    def add(self, node):
        self.frontier.append(node)

    #function to check a certain state
    def check_state(self, state):
        return any(node.state == state for node in self.frontier)

    #Check if frontier is empty
    def empty_frontier(self):
        return len(self.frontier) == 0

    #remove from the frontier and check if it's not empty
    def remove(self):
        if self.empty_frontier():
            raise Exception("frontier goala!")
        else:
            #LIFO-last in first out (the last element from the list is the first out from the list)
            node = self.frontier[-1] #remove the last element from the list
            self.frontier = self.frontier[:-1] #remove the node from the frontier 
            return node #return the node as result

class mimo_AI(turtle.Turtle):
    def __init__(self,level):
        turtle.Turtle.__init__(self)
        self.hideturtle()

        wn.bgcolor("black")
        wn.bgpic("./images/background_maze.gif")
            
        start = 0
        goal = 0

        self.height = len(level)
        self.length = max(len(row) for row in level)

        #List for storing walls coords
        self.walls = []

        for i in range(self.height):
            wall = []
            for j in range(self.length):

                start += (level[i][j].count('S'))
                goal += (level[i][j].count('C'))

                try:
                    if level[i][j] == "S":
                        self.start = (i, j)
                        wall.append(False)
                    elif level[i][j] == "C":
                        self.goal = (i, j)
                        wall.append(False)
                    elif level[i][j] == "E":
                        wall.append(False)
                    elif level[i][j] == " ":
                        wall.append(False)
                    elif level[i][j] == "X":
                        wall.append(True)
                    else:
                        wall.append(False)
                except IndexError:
                    wall.append(False)
            self.walls.append(wall)

        self.solution = None

        #Check if there's only one goal and one start point
        if start != 1:
            raise Exception("The maze should have one start point!!")
        if goal != 1:
            raise Exception("The maze should have one Goal!!")
    
    def animate_mouse(self):
        
        soricel = turtle.Turtle()
        soricel.hideturtle()
        soricel.penup()
        soricel.shape("./images/mouse.gif")

        solution = self.solution[1] if self.solution is not None else None
        
        for i, row in enumerate(self.walls):
            for j,wall in enumerate(row):
                if wall:
                    pass
                elif solution is not None and (i, j) in solution:
                    soricel.goto(-425+j*50,285-i*50)
                    soricel.showturtle()
                    time.sleep(0.1)
                    if (i, j) == self.goal:
                        global current_level
                        current_level += 1
                        print(f"The shortest path:{len(self.solution[1])} moves")
                        wn.clearscreen()
                        levels.pop(1)
                        try:
                            run_AI()
                        except:
                            IndexError
                            print("IA won the game!")
                            wn.clearscreen()
                            levels.append(level1)
                            levels.append(level2)
                            levels.append(level3)
                            return False
    def escape_exit_btn(self):
        if(keyboard.is_pressed('Escape')):
            return True
        else:
            False

    def display(self):
        pencil = turtle.Turtle()
        pencil.hideturtle()
        pencil.penup()
        pencil.speed(0)

        solution = self.solution[1] if self.solution is not None else None

        for i, row in enumerate(self.walls):
            for j, wall in enumerate(row):
                if wall:
                    print("█", end="")
                    pencil.shape("./images/wall1.gif")
                    if current_level == 2:
                        pencil.shape("./images/wall2.gif")
                    if current_level == 3:
                        pencil.shape("./images/wall3.gif")
                    pencil.goto(-425+j*50,285-i*50)
                    pencil.stamp()
                elif (i, j) == self.start:
                    print("S", end="")
                    pencil.goto(-425+j*50,285-i*50)
                    pencil.shape("square")
                    pencil.color("green")
                    pencil.shapesize(2.2)
                    pencil.stamp()
                elif (i, j) == self.goal:
                    print("C", end="")
                    pencil.shape("./images/cheese.gif")
                    pencil.goto(-425+j*50,285-i*50)
                    pencil.stamp()
                    
                elif solution is not None and (i, j) in solution:
                    print("*", end="") 
                    pencil.goto(-425+j*50,285-i*50)
                    pencil.shape("square")
                    pencil.color("yellow")
                    pencil.shapesize(2.2)
                    pencil.stamp()
                elif solution is not None and (i, j) in self.explored:
                    print(" ", end="")   
                    pencil.goto(-425+j*50,285-i*50)
                    pencil.shape("square")
                    pencil.color("blue")
                    pencil.shapesize(2.2)
                    pencil.stamp()
                else:
                    print(" ", end="")

            print()

    def neighbours(self, state):
        row, column = state
        options = [
            ("up", (row - 1, column)),
            ("down", (row + 1, column)),
            ("left", (row, column - 1)),
            ("right", (row, column + 1))
        ]

        result = []
        for action, (r, c) in options:
            if 0 <= r < self.height and 0 <= c < self.length and not self.walls[r][c]:
                result.append((action, (r, c)))
        return result

    def solve(self):

        self.nodes_explored = 0

        #Initialize frontier with the start position
        start = Node(state=self.start, previous_state=None, action=None)
        frontier = frontier_lifo()
        frontier.add(start)

        # Initialize a set of states explored empty
        self.explored = set()

        # Search until a solution is found
        while True:

            #If the frontier is empty then there's no solution
            if frontier.empty_frontier():
                raise Exception("The maze has no solutions!")

            # remove a node from frontier
            node = frontier.remove()
            self.nodes_explored += 1

            #If the state is the goal then we have a solution
            if node.state == self.goal:
                actions = []
                cells = []
                while node.previous_state is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.previous_state
                actions.reverse()
                cells.reverse()
                self.solution = (actions, cells)
                return

            # add the node in the explored ones
            self.explored.add(node.state)

            # add neighbours in frontier
            for action, state in self.neighbours(node.state):
                if not frontier.check_state(state) and state not in self.explored:
                    new_node = Node(state=state, previous_state=node, action=action)
                    frontier.add(new_node)

def run_AI():
    m=mimo_AI(levels[1])
    print("Maze:")
    m.display()
    print("Solving...")
    m.solve()
    print("Steps explored:", m.nodes_explored)
    print("Solution:")
    m.display()
    m.animate_mouse()