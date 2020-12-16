from turtle import *

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):
      def __init__(self):
          super(Player, self).__init__()
          self.shape("turtle")
          self.penup()
          self.goto(STARTING_POSITION)
          self.setheading(90)


      def turtle_up(self):
          self.forward(MOVE_DISTANCE)

      def turtle_back(self):
          self.backward(MOVE_DISTANCE)

      def turtle_reset(self):
          self.goto(STARTING_POSITION)

      def is_in_goal(self):
       if self.ycor() > 280:
          return True
       elif self.ycor() < 280:
           return False
