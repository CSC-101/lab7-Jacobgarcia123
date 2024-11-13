
def str_to_float(user_input1:str) -> float:
    try:
        return float(user_input1)
    except ValueError:
        return None

def gather_numbers() -> list[float]:
    new_list_of_numbers = []
    while True:
        user_input = input('Enter a number or done: ')
        if user_input.lower() == 'done':
            break
        number = str_to_float(user_input)
        if number is not None:
            new_list_of_numbers.append(number)
    return new_list_of_numbers


if __name__ == '__main__':
    numbers = gather_numbers()
    total = sum(numbers)
    print("total sum of numbers: ", total)
