import random

pc_num = random.randint(1, 100)
rounds, guesses = 0, 0

while True:
    user_num = input("Enter your number, between 1 and 100: ")
    while not user_num.isdigit():
        if user_num.isalpha() and user_num.capitalize() == "Exit":
            quit()
        user_num = input("Enter your number, between 1 and 100: ")

    if int(user_num) > pc_num:
        print("Lower")
    elif int(user_num) < pc_num:
        print("Higher")
    else:
        guesses += 1

        print("That's it.")
        border = "=" * 40
        print(f"""
        {border}
        | Number:         {str(pc_num).ljust(20)} |
        | Guesses:        {str(guesses).ljust(20)} |
        | Rounds Played:  {str(rounds).ljust(20)} |
        {border}
        """)
        pc_num = random.randint(1, 100)

    rounds += 1
