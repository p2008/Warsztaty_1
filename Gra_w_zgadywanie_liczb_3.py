from flask import Flask, request, render_template_string

app = Flask(__name__)


def let_the_machine(min_=0, max_=1001):
    guess = int((max_ - min_) / 2) + min_
    return min_, max_, guess


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        get_form = '''<form action="/" name="gameform" method="POST">
                            Pomyśl cyfrę, a ja ją odgadnę w mniej niż dziesięć przejść<br />
                            <input type="submit" name="ok" value ="OK"/>
                    </form>'''
        return get_form
    else:
        post_form = '''<form action="/" name="gameform" method="POST">
                            Zgaduję wartość: {{guess_}}<br />
                            <input type="hidden" name="min" value={{min_}} />
                            <input type="hidden" name="max" value={{max_}} />
                            <input type="hidden" name="guess" value={{guess_}} />
                            <input type="submit" name="more" value ="Więcej"/>
                            <input type="submit" name="less" value ="Mniej"/>
                            <input type="submit" name="won" value ="Trafiłeś"/>
                </form>'''
        if request.form.get("ok"):
            guess = let_the_machine()
            return render_template_string(post_form, guess_=guess[2], min_=guess[0], max_=guess[1])
        elif request.form.get("more"):
            guess = let_the_machine(int(request.form.get("guess")), int(request.form.get("max")))
            return render_template_string(post_form, guess_=guess[2], min_=guess[0], max_=guess[1])
        elif request.form.get("less"):
            guess = let_the_machine(int(request.form.get("min")), int(request.form.get("guess")))
            return render_template_string(post_form, guess_=guess[2], min_=guess[0], max_=guess[1])
        elif request.form.get("won"):
            return "\nWygrałem!"


if __name__ == '__main__':
    app.run(debug=True)
