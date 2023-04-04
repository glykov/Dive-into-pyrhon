from random import randint

while True:
    secret_number = randint(1, 1000)
    guesses = 10
    print('Я загадал число от 1 до 1000, сможешь угадать?')
    guess = int(input('Введи число: '))
    
    while guesses > 0:
        if guess > secret_number:
            print('Слишком много')
        elif guess < secret_number:
            print('Слишком мало')
        else:
            print('Ты победил')
            break
        guesses -= 1
        print(f'Осталось {guesses} попыток')
        guess = int(input('Попробуй еще: '))
        
    
    if (guesses == 0):
        print('В этот раз ты проиграл')
    print('Хочешь попробовать еще раз? [д/н]: ')
    choice = input()
    if (choice.lower() == 'н'):
        break

