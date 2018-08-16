import random
"""Program ask user for number in range of 0-100.
If True compares given number with random number giving information less/more"""

if __name__ == '__main__':
    max_int = 100
    min_int = 0
    random_number = random.randint(min_int, max_int)

    while True:
        user_input = input("Zgadnij liczbę: ")
        if user_input.isdigit():
            user_input_int = int(user_input)
            if user_input_int == random_number:
                print("Zgadłeś!")
                break
            elif user_input_int > max_int or user_input_int < min_int:
                print(f"Zakres liczb jest od {min_int} do {max_int}, spróbuj ponownie")
            elif user_input_int > random_number:
                print("Za dużo!")
            elif user_input_int < random_number:
                print("Za mało!")
        else:
            print("Proszę wpisać liczbę")
