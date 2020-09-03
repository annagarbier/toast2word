import os
from flask import Flask, render_template, session, redirect, url_for
from forms import GuessForm, StartForm
from nlp import normalize_for_display, normalize_for_evaluation, evaluate, get_target


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)
# app.config['SECRET_KEY'] = 'secret'


@app.route('/', methods=["GET", "POST"])
def index():
    """The start/index route, with the option to begin playing."""
    global current_word
    global target_word
    start_form = StartForm()

    # If start button is clicked, let the game begin.
    if start_form.validate_on_submit():
        current_word = 'toast'
        target_word = get_target()
        return redirect(url_for('play'))

    return render_template(
        'index.html',
        render_form=start_form)


@app.route('/play', methods=["GET", "POST"])
def play():
    """The play route, where guessing happens."""
    global current_word
    global guess_word
    global target_word
    info = ''
    guess_form = GuessForm()

    # If a guess is submitted, complete the comparison
    # logic, and conditionally advance.
    if guess_form.validate_on_submit():
        # Process the guess.
        guess_word = normalize_for_evaluation(guess_form.guess.data)
        # Move is an enum that describes how to proceed.
        move = evaluate(current_word, guess_word, target_word)[0]
        # Info is a message displayed to explain the result.
        info = evaluate(current_word, guess_word, target_word)[1]

        if move == 0:  # (win)
            return redirect(url_for('end'))
        elif move == 1:  # (advance)
            current_word = guess_word

        # Clear the form.
        guess_form.guess.data = ''

    return render_template(
        'play.html',
        current_word=current_word,
        render_form=guess_form,
        info=info)


@app.route('/end', methods=["GET", "POST"])
def end():
    """End the game, and give option to restart."""
    start_form = StartForm()
    global current_word
    global target_word

    # If start button is clicked, let the game begin (again).
    if start_form.validate_on_submit():
        current_word = 'toast'
        target_word = get_target()
        return redirect(url_for('play'))

    return render_template(
        'end.html',
        target_word=target_word,
        render_form=start_form
    )
