from flask import Flask, flash, Blueprint, render_template, request, redirect, url_for, session
from game_logic import evaluate_player_input, generate_number, generate_hand_for_players_and_stack, card_value, draw_card
import os

app = Flask(__name__)

bp = Blueprint('bp', __name__)  # Create a Blueprint named 'bp'

""""
@bp.route('/game')
def index():
    # Check if a game is already in progress
    if 'player_hand' in session and 'card_stack' in session:
        # Continue the current game
        player_hand = session['player_hand']
        card_stack = session['card_stack']
        number = session.get('number')
    else:
        # Start a new game
        player_hand, card_stack = generate_hand_for_players_and_stack()
        session['player_hand'] = player_hand
        session['card_stack'] = card_stack
        session['used_card_stack'] = []
        session['number'] = generate_number()
        number = session['number']

    return render_template('index.html', number=number, player_hand=player_hand, card_stack=card_stack, card_value=card_value)
"""

@bp.route('/')
def game():
    # Every time this route is accessed, a new game starts
    
    if 'player_hand' in session and 'card_stack' in session:
        print("not working")
        # Continue the current game
        player_hand = session['player_hand']
        card_stack = session['card_stack']
        number = session.get('number')
    else:
        player_hand, card_stack = generate_hand_for_players_and_stack()
        session['player_hand'] = player_hand
        session['card_stack'] = card_stack
        session['used_card_stack'] = []  # Initialize an empty list for used cards
        session['number'] = generate_number()  # Generate a new target number
        number = session['number']

    return render_template('index.html', number=number, player_hand=player_hand, card_stack=card_stack, card_value=card_value)

@bp.route('/new_game', methods=['POST'])
def new_game():
    # Reset the game state
    session.pop('player_hand', None)
    session.pop('card_stack', None)
    session.pop('used_card_stack', None)
    session.pop('number', None)

    # Redirect to the main game route to start a new game
    return redirect(url_for('bp.game'))

@bp.route('/submit_answer', methods=['POST'])
def submit_answer():
    user_input = request.form['player_input']
    selected_cards = request.form['selected_cards'].split(',')
    print(selected_cards)
    result = evaluate_player_input(user_input)
    number_generated = session.get('number')

    if result == number_generated:
        player_hand = session.get('player_hand', [])
        print(player_hand)
        card_stack = session.get('card_stack', [])
        print(card_stack)


        # Remove used cards from the player's hand
        for card in selected_cards:
            if card in player_hand:
                player_hand.remove(card)

        # Draw new cards based on the number of used cards
        player_hand, card_stack = draw_card(player_hand, card_stack, selected_cards)
        
        session['player_hand'] = player_hand
        session['card_stack'] = card_stack
        session['number'] = generate_number()  # Generate a new number for the next round
        session.modified = True

        print(player_hand)
        print(card_stack)
        flash("Correct result! Well done", "success")
        return redirect(url_for('bp.game'))

    else:
        flash("Error, " + str(result) + " is not equal to " + str(number_generated), "error")
        # Render the current game state instead of redirecting to a new game
        return render_template('index.html', number=session['number'], player_hand=session['player_hand'], card_stack=session['card_stack'], card_value=card_value)




    