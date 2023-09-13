import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "Up")
scoreboard.update_scoreboard()

game_over = False
while not game_over:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_cars()
    
    # detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            scoreboard.write_game_over()
            game_over = True
            
    # detect successfully finishing
    if player.is_at_finish_line():
        scoreboard.increase_level()
        car_manager.speed_cars()
    
screen.exitonclick()

