import random


def roll_dice(dice_count: int = 1, side_count: int = 6):
    return " ".join([str(random.randint(1, side_count+1)) for _ in range(dice_count)])


def main():
    while True:
        dice, side = input("Enter the number of dice and sides: ").split()
        if dice == 0 or side == 0:
            break
        print(roll_dice(int(dice), int(side)))


if __name__ == "__main__":
    main()
