# BlackJack Program with Random Card Picking and Card Removal

import random


def check_total(a, b):
    return a + b


def randomize(new):
    return random.randint(0, new)


def true_value(val):
    if val == "Queen" or val == "King" or val == "Jack":
        return 10
    elif val == "Ace":
        return 11
    else:
        return int(val)


def choose_random_card(total_card, cards_temp):
    value = cards_temp[randomize(total_card)]
    return value


def youWon(u1, c1):
    print(f"\nYou won the game with a score of {u1}, while the computer had a score of {c1}")


def compBusted(u1, c1):
    print(f"\nThe computer busted at {c1}! You have won with a score of {u1}!")


def youBusted(u1, c1):
    print(f"\nYou busted at {u1}, while the computer has a score of {c1}")


def didWin(u1, c1, w):
    if w is True:
        compBusted(u1, c1)
    elif u1 > 21:
        youBusted(u1, c1)
    elif u1 > c1:
        youWon(u1, c1)
    elif u1 == c1:
        print(f"It's a draw! You: {u1} , Computer: {c1}")
    else:
        print(f"The computer has won with a score of {c1}")

def getCards():
    return card


# CONSTANT : To go back to fresh card set
card = ["Ace", "Ace", "Ace", "Ace", "2", "2", "2", "2", "3", "3", "3", "3",
        "4", "4", "4", "4", "5", "5", "5", "5", "6", "6", "6", "6", "7", "7", "7", "7",
        "8", "8", "8", "8", "9", "9", "9", "9", "10", "10", "10", "10", "King", "King", "King", "King",
        "Queen", "Queen", "Queen", "Queen", "Jack", "Jack", "Jack", "Jack"]


def blackjack():
    end = False
    total_cards = 51

    # Temporary card deck with removal

    cards_temp = ["Ace", "Ace", "Ace", "Ace", "2", "2", "2", "2", "3", "3", "3", "3",
                  "4", "4", "4", "4", "5", "5", "5", "5", "6", "6", "6", "6", "7", "7", "7", "7",
                  "8", "8", "8", "8", "9", "9", "9", "9", "10", "10", "10", "10", "King", "King", "King", "King",
                  "Queen", "Queen", "Queen", "Queen", "Jack", "Jack", "Jack", "Jack"]
    while not end:
        # Declare starting variables
        hit = ""

        your_third = "0"
        comp_third = "0"
        true_third_value_comp = 0
        true_third_value_user = 0
        won = False
        users_choices = []
        comp_choices = []
        # Random First Drawn Cards and Removing Drawn Cards From Deck
        your_first = choose_random_card(total_cards, cards_temp)
        cards_temp.remove(your_first)
        users_choices.append(your_first)
        total_cards -= 1
        your_second = choose_random_card(total_cards, cards_temp)
        cards_temp.remove(your_second)
        users_choices.append(your_second)
        total_cards -= 1
        comp_first = choose_random_card(total_cards, cards_temp)
        cards_temp.remove(comp_first)
        comp_choices.append(comp_first)
        total_cards -= 1
        comp_second = choose_random_card(total_cards, cards_temp)
        cards_temp.remove(comp_second)
        comp_choices.append(comp_second)
        total_cards -= 1

        # print(cards_temp)

        # Setting True Values for Picks of "King", "Queen", "Jack", "Ace" in order to ensure addition properly

        # First User Pick
        true_first_value_user = true_value(your_first)

        # Second User Pick
        true_second_value_user = true_value(your_second)

        # First Computer Pick
        true_first_value_comp = true_value(comp_first)

        # Second Computer Pick
        true_second_value_comp = true_value(comp_second)

        # Get total for 2 cards dealt each
        user_total = check_total(true_first_value_user, true_second_value_user)
        comp_total = check_total(true_first_value_comp, true_second_value_comp)

        # Print User's First 2 Cards, and Dealer's First Card
        print("--- Welcome To BlackJack --- \n")
        print(f"Your first card dealt: {your_first}\n")
        print(f"Your second card dealt: {your_second}\n")
        print(f"Your total so far is: {user_total}\n")
        print("------------------------------------\n")
        print(f"Computer's first card dealt: {comp_first}\n")

        no_more = 0

        # check if user total < 21 and if so offer a hits until stop
        while user_total < 21 and no_more == 0:
            hit = input(f"Hit? Y or N: ").lower()
            if hit == "n":
                no_more = 1
            elif hit == "y":
                new_card = choose_random_card(total_cards, cards_temp)
                cards_temp.remove(new_card)
                total_cards -= 1
                users_choices.append(new_card)
                if new_card == "Ace":
                    if user_total + 11 > 21:
                        user_total += 1
                    else:
                        user_total += true_value(new_card)
                else:
                    user_total += true_value(new_card)
                print(f"\nYou pick up a {new_card}")
                print(f"\nYour cards are now: {users_choices}\n")
                print(f"Total: {user_total}\n")
                print("------------------------------------")
            else:
                print("Enter a better value!\n")

        # check if comp_total is less than 17 allowed, after user does hit, and pick up cards until 17 or higher
        while comp_total < 17 and user_total < 21:
            new_card = choose_random_card(total_cards, cards_temp)
            cards_temp.remove(new_card)
            total_cards -= 1
            comp_choices.append(new_card)
            if new_card == "Ace":
                if comp_total + 11 > 21:
                    comp_total += 1
                else:
                    comp_total += true_value(new_card)
            else:
                comp_total += true_value(new_card)
            if comp_total > 21:
                won = True
            else:
                comp_total = comp_total

        # check on win conditions in end
        print(f"Your final cards: {users_choices} \n Computers final cards: {comp_choices}")
        didWin(user_total, comp_total, won)

        check_end = input("\nWould you like to play again with the same deck? (Y/N) (E to End): ").lower()
        print("\n")
        if check_end == "e":
            print("\nThanks for playing!")
            end = True
            break
        elif check_end == "y":
            if total_cards < 10:
                total_cards = 51
                print("\nLess than 10 cards remain, reshuffling deck....\n")
            else:
                total_cards = total_cards
            your_first = ""
            your_second = ""
            comp_first = ""
            comp_second = ""
            user_total = 0
            comp_total = 0
        elif check_end == "n":
            check_end_again = input("\nWould you like to reshuffle the deck? (Y/N) (E to End): ").lower()
            print("\n")
            if check_end_again == "y":
                blackjack()
            elif check_end_again == "n":
                print("\nYou could've just ended!  Good bye!")
                end = True
                break
            else:
                end = True
                break
        else:
            end = True
            break


blackjack()