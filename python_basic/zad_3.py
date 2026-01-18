def print_even(numbers_list):
    for number in numbers_list:
        if number % 2 == 0:
            print(number)


list = list(range(10))

print_even(list)
