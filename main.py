import turtle

t = turtle.Turtle()

# 2.1
def square():
    for i in range(4):
        t.left(90)
        t.forward(50)
#square()

# 2.2
def re_square(x, y):
    if x>=100:
        return
    else:
        for i in range(4):
            t.forward(x)
            t.left(90)

        re_square(x + y, y + 1)

#re_square(10, 1)

#2.3
#t.speed("fastest")
def triangle(x):
    for i in range(3):
        t.forward(x)
        t.left(120)

def multi_triangle(x, y):
    if y ==0:
        triangle(x)
    else:
        # rysowanie 3 malych trojkatow
        multi_triangle(x / 2, y - 1)
        # przesuwanie zółwia
        t.forward(x / 2)
        multi_triangle(x / 2, y - 1)
        t.backward(x / 2)
        # przesuniecie do trzeciego trojkata
        t.left(60)
        t.forward(x / 2)
        t.right(60)
        #rysowanie trzeciego trojkata
        multi_triangle(x / 2, y - 1)
        #powrot do poczatku
        t.left(60)
        t.backward(x / 2)
        t.right(60)

#multi_triangle(200,5)

#2.4 a) Płatek śniegu Kocha
class KochPlatek:
    def __init__(self, length, level):
        self.length = length
        self.level = level
        self.t = turtle.Turtle()
        #self.t.speed("fastest")

    def koch_platek(self, length, level):
        if level == 0:
            self.t.forward(length)
        else:
            length /= 3
            self.koch_platek(length, level - 1)  # Pierwszy segment
            self.t.left(60)
            self.koch_platek(length, level - 1)  # Drugi segment
            self.t.right(120)
            self.koch_platek(length, level - 1)  # Trzeci segment
            self.t.left(60)
            self.koch_platek(length, level - 1)  # Czwarty segment

    def draw_snowflake(self):
        for _ in range(3):  # Płatki śniegu mają trzy boki
            self.koch_platek(self.length, self.level)  # Rysowanie krzywej Kocha
            self.t.right(120)  # Skręt w prawo o 120 stopn

length = 300
level = 4
snowflake = KochPlatek(length, level)
#snowflake.draw_snowflake()

#2.4 b) Fraktal drzewa

class FractalTree:
    def __init__(self, length, level):
        self.length = length
        self.level = level
        self.t = turtle.Turtle()
        self.t.speed("fastest")

    def draw_branch(self, length, level):
        if level == 0:
            return
        self.t.forward(length)
        self.t.right(20)
        self.draw_branch(length * 0.7, level - 1)
        self.t.left(40)
        self.draw_branch(length * 0.7, level - 1)
        self.t.right(20)
        self.t.backward(length)

    def draw(self):
        self.t.left(90)  # Ustaw kąt początkowy
        self.draw_branch(self.length, self.level)


length = 100
level = 5
tree_fractal = FractalTree(length, level)
tree_fractal.draw()