import random
from colorama import Fore, Back, Style


def generate_dices(num_players, dices):
    players_dices = []

    for _ in range(num_players):
        dice_rolls = [random.randint(1, 6) for _ in range(dices)]
        players_dices.append(dice_rolls)

    return players_dices


def check_dice_rolls(combined_dices, number, count):
    number = int(number)
    count = int(count)

    actual_count = combined_dices.count(number)

    if actual_count >= count:
        print(Fore.BLUE + f"He's not a LIAR - There are at least {count} {number}'s on the table." + Style.RESET_ALL)
        return 1
    else:
        print(Fore.RED + f"LIAR - There are not enough {number}'s on the table. Only {actual_count} found." + Style.RESET_ALL)
    return 0


def play_game():
    print("Hello, welcome to the game!")
    print("It's turn-based, and each player types in a bid 4 3, 2 2 (four 3's ...)")
    num_players = int(input("How many players will be playing? "))
    print("Bids start ! bid ex. 4 2 - four 2s")
    players_dices = generate_dices(num_players, 5)

    combined_dices = [dice for player_dices in players_dices for dice in player_dices]
    players_bids = [[] for _ in range(num_players)]  # List of lists to store bids said by each player

    turn_count = 0

    while True:
        current_player_index = turn_count % num_players  # raw data for which player it is (0,1,2)
        current_player = f"Player {current_player_index + 1}"  # human-readable data it uses the player_index !

        print("\nDice rolls are:")
        print(players_dices[current_player_index])
        if turn_count != 0:
            print("you can bid more or call them liar")
        word = input(f"{current_player} says: ")

        if word.lower() == 'liar':
            if turn_count == 0 or not any(players_bids):
                print("No previous bids to call liar on. Please make a bid.")
                continue

            for last_bid in reversed(players_bids):
                if last_bid:
                    last_bid = last_bid[-1]
                    break

            print("\n" + current_player + " bidded " + last_bid)
            result = check_dice_rolls(combined_dices,last_bid[2], last_bid[0])

            if result == 1:
                print(current_player + " is right!")
            else:
                print(current_player + " lost :( ")

            for i, words in enumerate(players_bids): # shows the bids of the players
                print(f"\nPlayer {i + 1}'s bids: {words}")

            print("\nDice rolls were:") # shows the dices of players
            for i, dices in enumerate(players_dices):
                print(Back.GREEN + f"Player {i + 1} rolled: {dices}")
            break
        else:
            players_bids[current_player_index].append(word)

        turn_count += 1


play_game()
