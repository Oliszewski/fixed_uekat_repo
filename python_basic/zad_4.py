def print_every_second_element(number_list):

    elements = number_list[::2]

    for element in elements:
        print(element)


list_of_10 = list(range(10))
print("Every second element:")
print_every_second_element(list_of_10)
