def let_the_machine(min_=0, max_=1001):
    guess = int((max_ - min_) / 2) + min_
    return min_, max_, guess


def main():
    guess = let_the_machine()
    i = 0
    user_answers = ("Za dużo", "Za mało", "Zgadłeś")
    while True:
        i += 1
        print(f"zgaduję po raz {i}: " + str(guess[2]))
        print("wybierz: 1 - {0[0]}, 2 - {0[1]}, 3 - {0[2]}".format(user_answers))
        user_ans = input("Podaj swoją odpowiedź")
        if user_ans == '3':
            print("Wygrałem!")
            return False
        elif user_ans == '2':
            guess = let_the_machine(min_=guess[2], max_=guess[1])
        elif user_ans == '1':
            guess = let_the_machine(min_=guess[0], max_=guess[2])
        else:
            print("Nie oszukuj!")


if __name__ == '__main__':
    main()
