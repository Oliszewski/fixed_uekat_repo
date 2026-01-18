def multiply_loop(numbers):
    result = []
    for number in numbers:
        result.append(number * 2)
    return result


numbers_list = [1, 2, 3, 4, 5]

print(multiply_loop(numbers_list))


# Second method:


def multiply_numbers(numbers):
    return [x * 2 for x in numbers]


numbers_list = [1, 2, 3, 4, 5]
print(multiply_numbers(numbers_list))
