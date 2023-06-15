# The number_list is taken to print the values with fizz, buzz or fizz_buzz
number_up_to = int(input('Fizz Buzz Game from 1 to: ')) + 1
for number_to_change in range(1, number_up_to):
    if number_to_change % 3 == 0 and number_to_change % 5 == 0:
        print(f'{number_to_change} is FizzBuzz!')
    elif number_to_change % 3 == 0:
        print(f'{number_to_change} is Fizz!')
        continue
    elif number_to_change % 5 == 0:
        print(f'{number_to_change} is Buzz!')
        continue
    else: print(number_to_change)