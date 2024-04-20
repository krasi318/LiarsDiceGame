import random

def generate_dices():
    num_players = int(input("How many players will be playing? "))
    players_dices = []

    for _ in range(num_players):
        # Generate 5 random numbers for each player, e.g., between 1 and 6 for dice values
        dice_rolls = [random.randint(1, 6) for _ in range(5)]
        players_dices.append(dice_rolls)

    return players_dices

# Example of calling the function and printing the result
players_dices = generate_dices()
for index, dices in enumerate(players_dices):
    print(f"Player {index + 1} rolled: {dices}")