from flask import Flask, flash, Blueprint, render_template, request, redirect, url_for, session
from game_logic import evaluate_player_input, generate_number, generate_hand_for_players_and_stack, card_value
import os

app = Flask(__name__)

bp = Blueprint('bp', __name__)  # Create a Blueprint named 'bp'


@bp.route('/')  # Using 'bp' instead of 'app' for the Blueprint routes
def index():
    session['number'] = generate_number()
    player_hand, card_stack = generate_hand_for_players_and_stack()
    return render_template('index.html', number=session['number'], player_hand=player_hand, card_stack=card_stack, card_value=card_value)


@bp.route('/submit_answer', methods=['POST'])
def submit_answer():
    user_input = request.form['player_input']
    result = evaluate_player_input(user_input)
    
    # Fetch the number from the session.
    number_generated = session.get('number')
    
    if (result == number_generated):
        flash("Correct result ! Well done", "success")
    else:
        flash("Error, " + str(result) + " is not equal to " + str(number_generated) , "error")
    return redirect(url_for('bp.index'))  


    