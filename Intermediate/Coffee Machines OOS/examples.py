from turtle import Turtle, Screen
from prettytable import PrettyTable
timmy = Turtle()
my_screen = Screen()
timmy.shape("turtle")
timmy.color("coral2")
timmy.speed(1)
timmy.forward(100)
print(my_screen.canvwidth, my_screen.canvheight)
print(timmy)
# my_screen.exitonclick()
my_table = PrettyTable()
my_table.add_column("Pokemon Name", ["Pikachu", "Charmander", "Squirtle"])
my_table.add_column("Pokemon Type", ["Electric", "Fire", "Water"])
my_table.align = "l"
print(my_table)
