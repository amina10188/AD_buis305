import random
number1 = int(input('Enter number 1:'))
if number1 % 3 == 0 and number1 % 5 == 0:
    print(number1, 'Tic Tac')
elif number1 % 5 == 0:
    print(number1, 'Tac')
elif number1 % 3 == 0:
    print(number1, 'Tic')
count = 1
while count <= 20:
    print(count)
    count += 1
count = 1
while count <= 20:
    if count % 3 == 0 and count % 5 == 0:
        print(count, 'Tic Tac')
    elif count % 5 == 0:
        print(count, 'Tac')
    elif count % 3 == 0:
        print(count, 'Tic')
    count += 1
random_number = random.randint(1, 100)
print('Random Number:', random_number)
tmp_count = 1
user_value = int(input('Enter a value:'))
while user_value <= 0 and tmp_count < 5:
    user_value = int(input('Enter a value greater than 0:'))
    tmp_count += 1
if user_value > 0:
    random_value = random.randint(1, 100)
    print('Random Value:', random_value)
    if user_value == random_value:
        print('Perfect Match!')
    else:
        print('Numbers don\'t match:', user_value, random_value)
