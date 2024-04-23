import random
from colorama import Fore, Back, Style


def generate_dices(num_players, num_dices):
    players_dices = []
    for player_dices in num_dices:
        dice_rolls = [random.randint(1, 6) for _ in range(player_dices)]
        players_dices.append(dice_rolls)
    return players_dices


def check_dice_rolls(combined_dices, number, count, use_wildcards):
    number = int(number)
    count = int(count)
    actual_count = combined_dices.count(number)
    ones_count = combined_dices.count(1) if use_wildcards and number != 1 else 0
    actual_count += ones_count

    if actual_count >= count:
        print(Fore.BLUE + f"He's not a LIAR - There are at least {count} {number}'s on the table (including wildcards)." + Style.RESET_ALL)
        return True
    else:
        print(Fore.RED + f"LIAR - There are not enough {number}'s on the table. Only {actual_count} found (including wildcards)." + Style.RESET_ALL)
        return False

def check_dice_rolls_wild(combined_dices, number, count):
    number = int(number)
    count = int(count)
    actual_count = combined_dices.count(number)
    ones_count = combined_dices.count(1)

    if number != 1:
        actual_count += ones_count

    if actual_count >= count:
        print(Fore.BLUE + f"He's not a LIAR - There are at least {count} {number}'s on the table (including wildcards)." + Style.RESET_ALL)
        return True
    else:
        print(Fore.RED + f"LIAR - There are not enough {number}'s on the table. Only {actual_count} found (including wildcards)." + Style.RESET_ALL)
        return False


def play_game(use_wildCards):
    print("Hello, welcome to the game!")
    print("It's turn-based, and each player types in a bid!")
    num_players = int(input("How many players will be playing? "))
    num_dices = [5] * num_players
    print("Bids start! Bid example: 4 2 - four 2s")

    players_bids = [[] for _ in range(num_players)]

    turn_count = 0
    while sum(d > 0 for d in num_dices) > 1:
        if turn_count % num_players == 0:
            players_dices = generate_dices(num_players, num_dices)
            combined_dices = [dice for player_dices in players_dices for dice in player_dices if player_dices]

        current_player_index = turn_count % num_players
        if num_dices[current_player_index] == 0:
            turn_count += 1
            continue

        current_player = f"Player {current_player_index + 1}"
        print("\nCurrent player is:", current_player)

        print("\nDice rolls are:")
        print(players_dices[current_player_index])
        if turn_count != 0:
            print("You can bid more or call them liar.")

        word = input(f"{current_player} says: ")

        if word.lower() == 'liar':
            if turn_count == 0 or not any(players_bids):
                print("No previous bids to call liar on. Please make a bid.")
                continue

            for last_bid in reversed(players_bids):
                if last_bid:
                    last_bid = last_bid[-1]
                    break

            last_count, last_number = map(int, last_bid.split())
            result = check_dice_rolls(combined_dices, last_number, last_count, use_wildCards)
            if result:
                print(current_player + " is right!")
            else:
                loser_index = (current_player_index - 1) % num_players
                num_dices[loser_index] -= 1
                print(f"Player {loser_index + 1} lost a dice and now has {num_dices[loser_index]} dice left.")
                if num_dices[loser_index] == 0:
                    print(f"Player {loser_index + 1} is out of the game!")

            players_bids = [[] for _ in range(num_players)]
        else:
            players_bids[current_player_index].append(word)

        turn_count += 1

    print("Game over!")
    for i, dice_count in enumerate(num_dices):
        if dice_count > 0:
            print(f"Player {i + 1} wins with {dice_count} dice left!")


use_wildCards = int(input("Do you wanna play the wild version of Liars Dice? 1=yes,0=no "))
play_game(use_wildCards)
