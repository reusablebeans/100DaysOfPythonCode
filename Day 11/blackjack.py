import random as random
import blackjack_art as art


def draw_card(receiving_deck):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card_value = random.choice(cards)
    receiving_deck.append(card_value)


def blackjack():
    print(art.logo)

    game_over = False
    computer_cards = []
    computer_sum = 0
    player_cards = []
    player_sum = 0

    for i in range(0, 2):
        draw_card(computer_cards)
        draw_card(player_cards)

    while not game_over:
        for number in player_cards:
            player_sum += number
        for number in computer_cards:
            computer_sum += number
        print(f"    Your cards: {player_cards}, CURRENT SCORE ---> {sum(player_cards)}")
        print(f"    The Computer's cards: [{computer_cards[0]}, ?]")
        if player_sum > 21:
            game_over = True
            print("bop")
        else:
            game_over = False
            hit_or_stand = input("Would you like to HIT or STAND? Type 'H' to HIT or 'S' to STAND: ")
            if hit_or_stand.lower() == "h":
                draw_card(player_cards)


play_game = input("Do you want to play a game of Blackjack? Type 'Y' for YES & 'N' for NO: ")
if play_game.lower() == "y":
    blackjack()
