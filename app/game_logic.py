import random
import operator
from sympy import sympify
from sympy.core.sympify import SympifyError

#basic set of cards
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# Mapping for face cards
card_values = {
    'J': 11, 'Q': 12, 'K': 13, 'A': 14
}
deck = ranks * 4  # Since there are four suits

random.shuffle(deck)


operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

def generate_number():
    num = random.randint(0,99)  # 1 number between 0 and 99 to be guessed 
    
    return num
    
def evaluate_player_input(user_input):
    # Replace card symbols with numbers
    for symbol, value in card_values.items():
        user_input = user_input.replace(symbol, str(value))

    # Use sympy to safely evaluate the expression
    try:
        # Convert the string to a sympy expression and evaluate it
        #! Todo logic to add to ensure that only valid cards are passed to sympify !
        result = sympify(user_input)
        print(result)
    except SympifyError:
        result = "Error: Invalid input"

    return result
    
# Function to generate a hand and stack
def generate_hand_for_players_and_stack():
    all_cards = ['clubs_2', 'clubs_3', 'clubs_4', 'clubs_5', 'clubs_6', 'clubs_7', 'clubs_8', 'clubs_9', 'clubs_10', 'clubs_J', 'clubs_Q', 'clubs_K', 'clubs_A',
                 'diamonds_2', 'diamonds_3', 'diamonds_4', 'diamonds_5', 'diamonds_6', 'diamonds_7', 'diamonds_8', 'diamonds_9', 'diamonds_10', 'diamonds_J', 'diamonds_Q', 'diamonds_K', 'diamonds_A',
                 'hearts_2', 'hearts_3', 'hearts_4', 'hearts_5', 'hearts_6', 'hearts_7', 'hearts_8', 'hearts_9', 'hearts_10', 'hearts_J', 'hearts_Q', 'hearts_K', 'hearts_A',
                 'spades_2', 'spades_3', 'spades_4', 'spades_5', 'spades_6', 'spades_7', 'spades_8', 'spades_9', 'spades_10', 'spades_J', 'spades_Q', 'spades_K', 'spades_A']  # List all card names
    random.shuffle(all_cards)
    player_hand = all_cards[:10]
    card_stack = all_cards[10:]
    return player_hand, card_stack