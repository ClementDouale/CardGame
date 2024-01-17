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
    """ equation = []

    for _ in range(num_terms):
        num = random.choice(ranks)
        op = random.choice(list(ops.keys()))
        equation.extend([num, op])

    equation.pop()  # Remove the last operator
    return ' '.join(equation)"""
    
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
    