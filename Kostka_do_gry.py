"""Napisz funkcję, która:

    przyjmie w parametrze taki kod w postaci stringa,
    rozpozna wszystkie dane wejściowe:
        rodzaj kostki,
        liczbę rzutów,
        modyfikator,
    wykona symulację rzutów i zwróci wynik.

Typy kostek występujące w grach: D3, D4, D6, D8, D10, D12, D20, D100.
"""

import random
import re
from flask import Flask, request

app = Flask(__name__)
opt = 0  # run in: 0 - console, 1 - flask


def dice_roll(dice_throw='D6'):
    """Function simulate n-number of throws of D-wall dice and modify result by modifier.
    Function takes string and compare it to the regex expression and divides it to groups.
    Groups are converted to int and next checked with dice_possible for instance of dice.
    return int if positive.
    """
    regex = r'([1-9]{0,})([Dd]\d{1,})([+-]?\d*)'

    match = re.search(regex, dice_throw)

    dice_possible = (3, 4, 6, 8, 10, 12, 100)

    try:
        dice_dict = dict(
            throws=int(match.group(1) if match.group(1) != '' else 1),
            dice=int(match.group(2)[1:]),
            modifier=int(match.group(3) if match.group(3) != '' else 0)
        )
    except AttributeError:
        return f'Eeeee, what is: {dice_throw}?'

    if dice_dict['dice'] in dice_possible:
        return sum([random.randint(1, dice_dict['dice']) for t in range(dice_dict['throws'])]) + dice_dict['modifier']
    else:
        return f"Sorry, but i don't have D{dice_dict['dice']} dice"


@app.route('/', methods=['GET', 'POST'])
def flask_dice_roll():
    """Same as dice_roll but made in Flask"""
    if request.method == 'GET':
        return '''<form method="POST" name="dice_form">Podaj kość według formatu xDy+z<br />Default D6<br />
                <input type="text" name="user_input" value='' placeholder="2D10+5" pattern="([1-9]{0,})([Dd]\d{1,})([+-]?\d*)">
                <input type="submit" name="button" value="Send">
                </form>'''
    else:
        dice_throw = request.form.get('user_input') if request.form.get('user_input') else 'D6'
        regex = r'([1-9]{0,})([Dd]\d{1,})([+-]?\d*)'

        match = re.search(regex, dice_throw)

        dice_possible = (3, 4, 6, 8, 10, 12, 100)

        dice_dict = dict(
            throws=int(match.group(1) if match.group(1) != '' else 1),
            dice=int(match.group(2)[1:]),
            modifier=int(match.group(3) if match.group(3) != '' else 0)
        )

        if dice_dict['dice'] in dice_possible:
            return str(sum([random.randint(1, dice_dict['dice']) for t in range(dice_dict['throws'])]) + dice_dict['modifier'])
        else:
            return f"Sorry, but i don't have D{dice_dict['dice']} dice"


if __name__ == '__main__' and opt == 0:
    d = input("Podaj kość według formatu xDy+z gdzie:\nx - Liczba_rzutów\ny - liczba ścian kostki\nz - dodatni/ujemny modyfikator\n:")
    print(dice_roll(d))


if __name__ == '__main__' and opt == 1:
    app.run(debug=True)
