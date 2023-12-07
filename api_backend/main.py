# Generate a random number between 1 and 151 to use as the Pokemon ID number 
# 2.Using the Pokemon API get a Pokemon based on its ID number 
# 3.Create a dictionary that contains the returned Pokemon's name, id, height and weight (★ 
# https://pokeapi.co/​) 
# 4.Get a random Pokemon for the player and another for their opponent 
# 5.Ask the user which stat they want to use (id, height or weight)  
# 6.Compare the player's and opponen\t's Pokemon on the chosen stat to decide who wins 
#  

import random, requests

def get_pokemon():
    id = random.randint(1,151)
    url = f"https://pokeapi.co/api/v2/pokemon/{id}"
    response = requests.get(url)
    data = response.json()
    pokemon_data = {
        'id': data['id'],
        'name':data['name'],
        'height': data['height'],
        'weight': data['weight']
    }
    return pokemon_data
def get_winner():
    print("First, I'll randomly assign you a pokemon!")
    my_pokemon = get_pokemon()
    opponent = get_pokemon()
    print(f"Your pokemon stats: \n Name: {my_pokemon['name']},\n Height: {my_pokemon['height']},\n Weight: {my_pokemon['weight']}")
    
    chosen_stat = ''
    while chosen_stat != "height" and chosen_stat != "weight":
        chosen_stat = input("Which stat would you like to compare? Height or weight? ").lower()
    if chosen_stat == "height": 
        if my_pokemon["height"] > opponent["height"]:
            print(f"Your pokemon's height, {my_pokemon['height']} is larger than its opponent, {opponent['height']}\n***\nYOU WIN\n***")
        elif my_pokemon["height"] < opponent['height']:
            print(f"Your pokemon's height, {my_pokemon['height']} is less than its opponent, {opponent['height']}\n***\nYOU LOSE\n***")
        else:
            print(f"There has been a tie! Your pokemon's height, {my_pokemon['height']} and your opponents, {opponent['height']} is the same\n***\nTIE\n***")
    else: 
        if my_pokemon["weight"] > opponent["weight"]:
            print(f"Your pokemon's weight, {my_pokemon['weight']} is larger than its opponent, {opponent['weight']}\n***\nYOU WIN!\n***")
        elif my_pokemon["height"] < opponent['height']:
            print(f"Your pokemon's weight, {my_pokemon['weight']} is less than its opponent, {opponent['weight']}\n***\nYOU LOSE\n***")
        else:
            print(f"There has been a tie! Your pokemon's weight, {my_pokemon['weight']} and your opponents, {opponent['weight']} is the same\n***\nTIE\n***")
    print(f"Your opponents stats: \n Name: {opponent['name']},\n Height: {opponent['height']},\n Weight: {opponent['weight']}")

get_winner()