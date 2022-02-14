class Shapes(object):
    def __init__(self):
        print("I created a shape!")

    def color(self):
        print('Shape Color:')

    def filled(self):
        print("Is this shape filled? ")

# Child Class Circle

class CircleShape(Shapes):
    def __init__(self):
        Shapes.__init__(self)
        print('This shape is a Circle')
        print("")

    def color(self):
        super(CircleShape, self).color()
        print("The color of this Cirle is Red")
        print("")

    def filled(self):
        super(CircleShape, self).filled()
        filledok = "N"
        if filledok == 'Y':
            print("Shape Circle is filled")
        else:
            print("Shape Circle is NOT filled")
            print("")

    def getDiameter(self):
        radius = 12
        print("The circle's Diameter is: " + str(2*radius))
        print("")

    def getCirc(self):
        radius = 12
        PI = 2.14
        print("The circle's Circumference is: " + str((2*PI) * radius))
        print("")

    def getArea(self):
        radius = 12
        PI = 2.14
        print("The circle's Area is: " + str((PI * (radius * radius))))        #((PI*radius) * radius))
        print("")

# Child Class Rectangle

class RectangleShape(Shapes):
    def __init__(self):
        Shapes.__init__(self)
        print('This shape is a Rectangle')
        print("")

    def color(self):
        super(RectangleShape, self).color()
        print("The color of this Rectangle is Blue")
        print("")

    def filled(self):
        super(RectangleShape, self).filled()
        filledok = "Y"
        if filledok == 'Y':
            print("Shape Rectangle is filled")
        else:
            print("Shape Rectangle is NOT filled")
            print("")

    def RectArea(self):
        l = 10
        w = 5
        print("The Rectangle's Area is: " + str(l * w))

    def RectPermieter(self):
        l = 10
        w = 5
        print("The Rectangle's Perimeter is: " + str(2 * (l * w)))

# Child Class Square

class SquareShape(Shapes):
    def __init__(self):
        Shapes.__init__(self)
        print('This shape is a Square')
        print("")

    def color(self):
        super(SquareShape, self).color()
        print("The color of this Square is White")
        print("")

    def filled(self):
        super(SquareShape, self).filled()
        filledok = "Y"
        if filledok == 'Y':
            print("Shape Square is filled")
        else:
            print("Shape Square is NOT filled")
            print("")

    def SquareArea(self):
        l = 5
        print("The Square's Area is: " + str(l * 2))

    def SquarePermieter(self):
        l = 5
        print("The Square's Perimeter is: " + str(4 * l))


c = CircleShape()
c.color()
c.filled()
c.getDiameter()
c.getCirc()
c.getArea()

# r = RectangleShape()
# r.color()
# r.filled()
# r.RectArea()
# r.RectPermieter()

# s = SquareShape()
# s.color()
# s.filled()
# s.SquareArea()
# s.SquarePermieter()