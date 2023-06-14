from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()        
        self.shape('circle')
        self.penup()
        self.shapesize(0.5,0.5)
        self.color('blue')
        self.refresh()
    def refresh(self):
        position_x = random.randint(-280,280)
        position_y = random.randint(-280,280)
        self.goto(position_x,position_y)
