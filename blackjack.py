Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def blackjack():
...     def deal_card():
...         """Returns a random card from the deck"""
...         cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
...         return random.choice(cards)
... 
...     def calculate_score(hand):
...         """Calculates the score of the current hand"""
...         if sum(hand) == 21 and len(hand) == 2:
...             return 0  # Blackjack
...         if 11 in hand and sum(hand) > 21:
...             hand.remove(11)
...             hand.append(1)
...         return sum(hand)
... 
...     print("Welcome to Blackjack!")
...     player_hand = [deal_card(), deal_card()]
...     computer_hand = [deal_card(), deal_card()]
... 
...     game_over = False
...     while not game_over:
...         player_score = calculate_score(player_hand)
...         computer_score = calculate_score(computer_hand)
... 
...         print(f"Your hand: {player_hand}, current score: {player_score}")
...         print(f"Computer's first card: {computer_hand[0]}")
... 
...         if player_score == 0:
...             print("You got a Blackjack! You win!")
...             break
...         elif player_score > 21:
...             print("You went over. You lose!")
...             break
... 
...         should_continue = input("Type 'y' to get another card, 'n' to pass: ")
...         if should_continue == 'y':
...             player_hand.append(deal_card())
        else:
            game_over = True

    while computer_score < 17 and not game_over:
        computer_hand.append(deal_card())
        computer_score = calculate_score(computer_hand)

    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")

    if computer_score > 21:
        print("Computer went over. You win!")
    elif player_score > computer_score:
        print("You win!")
    elif player_score < computer_score:
        print("You lose!")
    else:
