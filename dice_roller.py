import random
dice_rolls = int(input('How many dices u want to roll? '))
dice_sum = 0
dice_side = int(input('How many side? '))
for i in range(0,dice_rolls):
    roll = random.randint(1,dice_side)
    if roll == 1:
        print(f'You rolled a {roll}! critical fail')
    elif roll == dice_side:
        print(f'you rolled a {roll}! critical succes')
    else:
        print(f'you rolled a {roll}')
    dice_sum += roll
def main():
    print(f'You have rolled a total of {dice_sum}')
if __name__== "__main__":
  main()
