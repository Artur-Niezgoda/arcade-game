"""The module to keep the score and display in on the screen.

Classes:
    Scoreboard(Turtle)

Methods:
    update_scoreboard()
        Print the score on the Screen
    l_point()
        Add a point to the left player and update the scoreboard
    r_point()
        Add a point to the right player and update the scoreboard

Constants:
    ALIGN
        option for aligning score text
    FONT
        tuple containing font, fontsize and font option
"""

from turtle import Turtle

# option for aligning score text
ALIGN = "Center"
# tuple containing font, fontsize and font option
FONT = ("Courier", 80, "bold")

class Scoreboard(Turtle):
    """Class creating a score text on the top of the screen

    Args:
        Turtle (class): superclass of Scoreboard class

    Attributes:
        l_score (int): initial score of the left player, default 0 
        r_score (int): initial score of the right player, default 0 
    """

    def __init__(self):
        """Creates object that displays score
        """

        super().__init__()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update the scoreboard
        """

        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGN, font = FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGN, font = FONT)
    
    def l_point(self):
        """Add a point to the left player and update the scoreboard
        """

        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """Add a point to the right player and update the scoreboard
        """

        self.r_score += 1
        self.update_scoreboard()