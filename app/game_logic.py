import random
import operator

#basic set of cards
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = ranks * 4  # Since there are four suits

random.shuffle(deck)


ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

def generate_equation():
    num_terms = random.randint(2, 3)  # 2 or 3 terms in the equation
    equation = []

    for _ in range(num_terms):
        num = random.choice(ranks)
        op = random.choice(list(ops.keys()))
        equation.extend([num, op])

    equation.pop()  # Remove the last operator
    return ' '.join(equation)

# Example
print(generate_equation())