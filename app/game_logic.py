import random
import operator
from sympy import sympify
from sympy.core.sympify import SympifyError


values = {
        'clubs_2':2, 'clubs_3':3, 'clubs_4':4, 'clubs_5':5, 'clubs_6':6, 'clubs_7':7, 'clubs_8':8, 'clubs_9':9, 'clubs_10':10, 'clubs_J':11, 'clubs_Q':12, 'clubs_K':13, 'clubs_A':1,
        'diamonds_2':2, 'diamonds_3':3, 'diamonds_4':4, 'diamonds_5':5, 'diamonds_6':6, 'diamonds_7':7, 'diamonds_8':8, 'diamonds_9':9, 'diamonds_10':10, 'diamonds_J':11, 'diamonds_Q':12, 'diamonds_K':13, 'diamonds_A':1,
        'hearts_2':2, 'hearts_3':3, 'hearts_4':4, 'hearts_5':5, 'hearts_6':6, 'hearts_7':7, 'hearts_8':8, 'hearts_9':9, 'hearts_10':10, 'hearts_J':11, 'hearts_Q':12, 'hearts_K':13, 'hearts_A':1,
        'spades_2':2, 'spades_3':3, 'spades_4':4, 'spades_5':5, 'spades_6':6, 'spades_7':7, 'spades_8':8, 'spades_9':9, 'spades_10':10, 'spades_J':11, 'spades_Q':12, 'spades_K':13, 'spades_A':1
    }
card_names = set(values.keys())

def card_value(card_name):
    """Return the numerical value of a card given its name."""
    # Example card values - modify according to your game's rules
    return values.get(card_name, 0)  # Return 0 or some default value if card_name is not found

def draw_card(player_hand, card_stack, selected_cards):
    num_cards_to_draw = len(selected_cards)
    while len(player_hand) < 10 and len(card_stack) > 0 and num_cards_to_draw > 0:
        player_hand.append(card_stack.pop(0))
        num_cards_to_draw -= 1
    return player_hand, card_stack

def generate_number():
    num = random.randint(0,99)  # 1 number between 0 and 99 to be guessed 
    return num
    
def evaluate_player_input(user_input):
    try:
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

