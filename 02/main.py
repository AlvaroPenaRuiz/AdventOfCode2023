
from functools import reduce

rawdata = ""

with open("data.txt", "r") as file:
    rawdata = file.read()

def decode_data(line: str):
    game = {"green":[], "red": [], "blue": []}
    game['id'] = int(line.split(':')[0].split(' ')[1])
    sets = line.split(':')[1].split(";")

    for set in sets:
        green = 0 
        red = 0 
        blue = 0
        picks = [pick.strip().split(" ") for pick in set.split(",")]
        for pick in picks:
            if "green" == pick[1]: green = int(pick[0])
            if "red" == pick[1]: red = int(pick[0])
            if "blue" == pick[1]: blue = int(pick[0])
        game["green"].append(green)
        game["red"].append(red)
        game["blue"].append(blue)
    
    return game

def is_posible(game, green, red, blue):
    sum_bool = lambda a,b : a and b
    is_green_posible = reduce(sum_bool, [pick <= green for pick in game["green"]])
    is_red_posible = reduce(sum_bool, [pick <= red for pick in game["red"]])
    is_blue_posible = reduce(sum_bool, [pick <= blue for pick in game["blue"]])
    return is_green_posible and is_red_posible and is_blue_posible


def get_minimum_balls_and_power(game):
    game['min_green'] = 0
    game['min_red'] = 0
    game['min_blue'] = 0
    for pick in game['green']: 
        if pick > game['min_green']: game['min_green'] = pick
    for pick in game['red']: 
        if pick > game['min_red']: game['min_red'] = pick
    for pick in game['blue']: 
        if pick > game['min_blue']: game['min_blue'] = pick
    game['power'] = game['min_green'] * game['min_red'] * game['min_blue']
    return game

decoded_data = [decode_data(line) for line in rawdata.split('\n')]

# Exercise 1
posibilities = {"green": 13, "red": 12, "blue":14}
total_exercise1 = reduce(lambda a,b : a + b, [game["id"] for game in filter(lambda game : is_posible(game, posibilities["green"], posibilities["red"], posibilities["blue"]) , decoded_data)])

print(total_exercise1)

# Exercise 2
improved_data = [get_minimum_balls_and_power(game) for game in decoded_data]
total_exercise2 = reduce(lambda a,b : a+b, [game['power'] for game in improved_data])

print(total_exercise2)