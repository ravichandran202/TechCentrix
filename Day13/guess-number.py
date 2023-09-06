import random
print('--------------GUESS NUMBER GAME--------------')
random_num = random.randint(0,9)
attempt = 0

while True:
    user_input = int(input('Enter Number 0 to 9 : '))
    attempt+=1
    if user_input == random_num:
        break
    print('Please Try Again....\n\n')
print('\n.....SUCCESS......')
print(f'Total Attempts : {attempt}')