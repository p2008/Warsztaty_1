"""
Napisz program, który:

    zapyta o typowane liczby, przy okazji sprawdzi następujące warunki:
        czy wprowadzony ciąg znaków jest poprawną liczbą,
        czy użytkownik nie wpisał tej liczby już poprzednio,
        czy liczba należy do zakresu 1-49,
    po wprowadzeniu 6 liczb, posortuje je rosnąco i wyświetli na ekranie,
    wylosuje 6 liczb z zakresu i wyświetli je na ekranie,
    poinformuje gracza, czy trafił przynajmniej "trójkę".
"""

from flask import Flask, request, render_template_string
import random

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def lotto():
    """random.sample() - Chooses k unique random elements from a population sequence or set"""
    temp = '''
        <form action="/" name="lotto_form" method="post" title="LOTTO" >
            liczby oddzielone spacją <br />
            <input type="text" name="lotto_input" value="{{val}}" placeholder='np. 12 12 12 12 12 12' pattern="([0-9]{1,2}\s{1}){5}[0-9]{1,2}"/>
            <input type="submit" name="send" value="Wyślij" />
        </form> '''

    if request.method == 'GET':
        return render_template_string(temp, val='')

    else:
        lotto_list = list(request.form.get('lotto_input').split(" "))
        lotto_set = set(map(int, lotto_list))

        if len(lotto_set) != len(lotto_list) or max(lotto_set) > 49:
            return render_template_string(temp, val=request.form.get('lotto_input')) + "<br/ >Podano zdublowaną lub za dużą wartość"

        else:
            lotto_numbers_set = set(random.sample(range(50), 6))
            result = lotto_set & lotto_numbers_set
            result = result if len(result) != 0 else ''

            return f'Podane liczby: {str(lotto_set)[1:-1]}<br />Wylosowane liczby: {str(lotto_numbers_set)[1:-1]}<br />Trafiłeś <strong>{len(result)}</strong>: {str(result)[1:-1]}'


if __name__ == "__main__":
    app.run(debug=True)
