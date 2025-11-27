print('Welcome to my quiz game!')

playing = input('Do you want to play? (yes/no): ').lower()

if playing != 'yes':
    print('Maybe next time!')
    quit()

print('Great! Let\'s start the quiz.')

score = 0

answer = input('What is the capital of France?: ').lower()

if answer == 'paris':
    print('Correct!')
    score += 1
else:
    print('Wrong! The correct answer is Paris.')

answer = input('What does CO2 stand for?: ').lower()

if answer == 'carbon dioxide':
    print('Correct!')
    score += 1
else:
    print('Wrong! The correct answer is Carbon Dioxide.')

answer = input('What is the name of the river that runs through Egypt?: ').lower()

if answer == 'nile' or answer == 'nile river':
    print('Correct!')
    score += 1
else:
    print('Wrong! The correct answer is Nile River.')

answer = input('What is the highest mountain in the world?: ').lower()

if answer == 'everest' or answer == 'mount everest':
    print('Correct!')
    score += 1
else:
    print('Wrong! The correct answer is Mount Everest.')

print(f'You got {score} out of 4 questions correct.')
print(f'Your score percentage is: {score / 4 * 100}%')