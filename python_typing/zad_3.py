def is_even(number: int) -> bool:
    return number % 2 == 0


result_bool = is_even(7)
if result_bool:
    print("Even number")
else:
    print("Odd number")
