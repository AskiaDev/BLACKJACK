import random

# return 1 random card
def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# calculating the score
def calculate(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # checking if ace is in the hands and the score is greater than 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        # removing 11 in the hands
        cards.append(1)
        # removing 11 in the hands
    # return the total sum of the cards in the hands
    return sum(cards)

# comparing the cards of each user
def compare(user, computer):
    if user == computer:
        return 'Draw'
    elif computer == 0:
        return 'You Lose!'
    elif user == 0:
        return 'You Win!'
    elif computer > 21:
        return 'You win Your opponent went over 21!'
    elif user > 21:
        return 'You lose you went over 21!'
    elif computer > user:
        return 'You Win!'
    else:
        return 'You Lose!'


def play():
    user_cards = []
    computer_cards = []

    for i in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())
    game_over = False
    while not game_over:
        user = calculate(user_cards)
        computer = calculate(computer_cards)
        print(f"Your Cards: {user_cards}, Score: {user}")
        print(f"Computers first card: {computer_cards[0]}")

        if user == 0 or computer == 0 or user > 21:
            game_over = True
        else:
            another_card = input("Type 'y' to get another card type p to pass: ")
            if another_card == 'y'.lower():
                user_cards.append(deal_cards())
            else:
                game_over = True

    while computer != 0 and computer < 17:
        computer_cards.append(deal_cards())
        computer = calculate(computer_cards)


    print("         -----------------------------------------       ")
    print(f"            Your Cards: {user_cards}\n            Score: {user}")
    print("         -----------------------------------------       ")
    print(f"            Computer Cards: {computer_cards}\n            Score: {computer}")
    print(compare(user, computer))

while True:
    play()
    play_again = input("Do you want to play again? Type 'y' for yes, or 'n' for no: ")
    if play_again.lower() != 'y':
        break