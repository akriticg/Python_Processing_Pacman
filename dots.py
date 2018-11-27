from dot import Dot


class Dots:

    """A collection of dots."""
    def __init__(self, WIDTH, HEIGHT,
                 LEFT_VERT, RIGHT_VERT,
                 TOP_HORIZ, BOTTOM_HORIZ):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.TH = TOP_HORIZ
        self.BH = BOTTOM_HORIZ
        self.LV = LEFT_VERT
        self.RV = RIGHT_VERT
        self.SPACING = 75
        self.EAT_DIST = 50

        # Initialize four rows of dots, based on spacing and width of the maze
        self.top_row = [Dot(self.SPACING * i, self.TH)
                        for i in range(self.WIDTH//self.SPACING + 1)]
        self.bottom_row = [Dot(self.SPACING * i, self.BH)
                           for i in range(self.WIDTH//self.SPACING + 1)]
        self.left_col = [Dot(self.LV, self.SPACING * i)
                         for i in range(self.HEIGHT//self.SPACING + 1)]
        self.right_col = [Dot(self.RV, self.SPACING * i)
                          for i in range(self.HEIGHT//self.SPACING + 1)]

        # I combine all the dots into a single list to make removal easier

        self.all_dots = (self.top_row + self.bottom_row +
                         self.left_col + self.right_col)

    def display(self):
        """Calls each dot's display method"""
        for i in range(0, len(self.all_dots)):
            self.all_dots[i].display()
        for k in self.all_dots:
            print(k.x)
            print(k.y)

    def eat(self, x, y):
        '''eats the dot near the pacman'''
        for dot in self.all_dots:

            if (abs(dot.x - x) <= self.EAT_DIST or
               abs(dot.x - x) >= self.WIDTH) and dot.y == y:
                self.all_dots.remove(dot)

            elif (abs(dot.x - x) <= self.EAT_DIST or
                  abs(dot.x - x) >= self.WIDTH) and dot.y == y:
                self.all_dots.remove(dot)

            elif (abs(dot.y - y) <= self.EAT_DIST or
                  abs(dot.y - y) >= self.HEIGHT) and dot.x == x:
                self.all_dots.remove(dot)

            elif (abs(dot.y - y) <= self.EAT_DIST or
                  abs(dot.y - y) >= self.HEIGHT) and dot.x == x:
                self.all_dots.remove(dot)

    def dots_left(self):
        """Returns the number of remaing dots in the collection"""
        return len(self.all_dots)
