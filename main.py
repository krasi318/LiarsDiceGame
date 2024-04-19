def play_game():
    print("Hello welcome to the game")
    print("its turn based and each player types in...")
    words_p1 = []
    words_p2 = []
    turn_count = 0

    while True:
        turn_count += 1
        if turn_count % 2 == 0:
            word = input("player 1 says: ")
            words_p1.append(word)
        else:
            word = input("player 2 says: ")
            words_p2.append(word)

        if word.lower() == 'exit':
            print("game over")
            print("player 1 said - ")
            print(words_p1)
            print("player 2 said - ")
            print(words_p2)
            break


play_game()
