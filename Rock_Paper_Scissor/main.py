import random
import pprint


MOVE_LIST = ["Rock", "Paper", "Scissor",]
pc_score, human_score, rounds = 0, 0, 0

while True:
    user_move = input("Enter your move (rock, paper, scissor, exit): ").capitalize()
    if user_move == "Exit":
        quit()

    while user_move not in MOVE_LIST:
        user_move = input("Enter existence move (rock, paper, scissor, exit): ").capitalize()

    pc_move = random.choice(MOVE_LIST)
    if user_move == pc_move:
        pass
    elif user_move == "Rock":
        if pc_move == "Paper":
            pc_score += 1
        else:
            human_score += 1
    elif user_move == "Paper":
        if pc_move == "Scissor":
            pc_score += 1
        else:
            human_score += 1
    elif user_move == "Scissor":
        if pc_move == "Rock":
            pc_score += 1
        else:
            human_score += 1
    rounds += 1
    border = "=" * 50
    print(f"""
    {border}
    | Player:        {user_move.ljust(20).rjust(30)} |
    | Computer:      {pc_move.ljust(20).rjust(30)} |
    | Player Score:  {str(human_score).ljust(20).rjust(30)} |
    | Computer Score:{str(pc_score).ljust(20).rjust(30)} |
    | Rounds Played: {str(rounds).ljust(20).rjust(30)} |
    {border}
    """)
