from flask import Flask, flash, Blueprint, render_template, request, redirect, url_for, session
from game_logic import evaluate_player_input
from game_logic import generate_number
import os

app = Flask(__name__)

bp = Blueprint('bp', __name__)  # Create a Blueprint named 'bp'

card_values = {
    'J': 11, 'Q': 12, 'K': 13, 'A': 14
}



@bp.route('/')  # Use 'bp' instead of 'app' for the Blueprint routes
def index():
    session['number'] = generate_number()
    return render_template('index.html', number=session['number'])

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
    return redirect(url_for('bp.index'))  # Update the endpoint to 'bp.index'
