import random

user_guesses = []
game_chances = 0
def get_birdname():
    birds_file = open('Day16/birds.txt','r')
    birds_name = birds_file.read().splitlines()
    bird_name = random.choice(birds_name)
    return bird_name


def guess_name():
    bird_name = get_birdname().lower()
    print(bird_name)
    bird_name_in_letters = [ch for ch in bird_name]
    game_chances = int(len(bird_name)+1)
    
    print("****** WELCOME TO GUESSING GAME *****\n")
    print(f"Bird is having {len(bird_name)} letters")
    while game_chances>0:
        print(f'Remining Chances : {game_chances} ')
        user_guess_name = input('Enter Name : ').lower()
        
        if len(user_guess_name)>1 and len(user_guess_name) != len(bird_name):
            print('Invalid Input')
        if user_guess_name not in bird_name_in_letters:
            print('Invalid Input')
        if user_guess_name == bird_name:
            print('Hurray Pattern Matched!!!!')
            print('\nYou Won the Game!!!')
            break
        if user_guess_name in user_guesses:
            print('I Think U Guessed it Already!!!!')
        if user_guess_name not in user_guesses and len(user_guess_name)==1:
            user_guesses.append(user_guess_name)
        if game_chances == 0:
            print('\nGame Over!!!\nYou Lost the Game!!!')
        
        game_chances = game_chances - 1
        print("\n************************\n\n")

    print(f'Gussing Bird Name : {bird_name}')
guess_name()