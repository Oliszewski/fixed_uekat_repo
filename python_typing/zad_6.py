def process_lists(list1: list, list2: list) -> list:

    combined = list1 + list2

    unique_items = set(combined)

    cubed_items = [x**3 for x in unique_items]
    return cubed_items


print(f"{process_lists([1, 2], [2, 3])}")
