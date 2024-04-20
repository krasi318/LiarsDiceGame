import random

def generate_dices():
    num_players = int(input("How many players will be playing? "))
    players_dices = []

    for _ in range(num_players):
        # Generate 5 random numbers for each player, e.g., between 1 and 6 for dice values
        dice_rolls = [random.randint(1, 6) for _ in range(5)]
        players_dices.append(dice_rolls)

    return players_dices

players_dices = generate_dices()
# for index, dices in enumerate(players_dices):
#     print(f"Player {index + 1} rolled: {dices}")
print(players_dices)

def check_dice_rolls(players_dices, number, count):
    combined_dices = [dice for player_dices in players_dices for dice in player_dices] # makes the lists (for each player) into 1 combined
    actual_count = combined_dices.count(number)

    if actual_count >= count:
        print(f"There are at least {count} {number}'s on the table.")
        return 1
    else:
        print(f"There are not enough {number}'s on the table. Only {actual_count} found.")
    return 0

# Check for three '4's
results = check_dice_rolls(players_dices, 2, 7)

print("heyo")

if results == 1:
    print("yes")
else:
    print("no")