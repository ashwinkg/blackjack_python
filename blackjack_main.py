from art import logo
import random

print(logo)

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_cards(cards):
    ## Handling BlacJack Condition (Ace +10)
    if sum(cards)==21 and len(cards)==2:
        return 0
    ## If the score is already over 21 and cards contains 11 then replace it as 1
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
    

def compare(computer_score,user_score):
    if computer_score==user_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, the opponent has a blackjack"
    elif user_score == 0:
        return "Win with a blackjack"
    elif computer_score >21:
        return "Computer went over. You win"
    elif user_score> 21:
        return "You went over. Computer win"
    elif computer_score>user_score:
        return "You Lose"
    else:
        return "You win"


user_cards=[]
computer_cards=[]
is_game_over=False

for _ in range(2):
    user_cards.append(deal_cards())
    computer_cards.append(deal_cards())
    

while not is_game_over:
    user_score=calculate_cards(user_cards)
    computer_score=calculate_cards(computer_cards)
    
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    ## If user or computer has a blackjack or user score above 21 then GAME OVER!!!
    if user_score == 0 or computer_score==0 or user_score>21:
        is_game_over=True
    else:
        user_should_deal=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if user_should_deal =='y':
            user_cards.append(deal_cards())
            user_score=calculate_cards(user_cards)
        else:
            is_game_over=True
    
while computer_score!=0 and computer_score < 17:
    computer_cards.append(deal_cards())
    computer_score = calculate_cards(computer_cards)


print(f"Your final cards: {user_cards}, final score: {user_score}")
print(f"Computer's final cards: {computer_cards}, final score {computer_score}")
print(f"{compare(computer_score,user_score)}")