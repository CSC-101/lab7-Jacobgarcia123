import sys



def str_to_float(user_input1:str) -> float:
    try:
        return float(user_input1)
    except ValueError:
        return None

if __name__ =='__main__':
    total = 0.0
    for arg in sys.argv[1:]:
        number = str_to_float(arg)
        if number is not None:
            total += number
    print('Total sum of numbers: ', total)






#user = input('Enter a number: ')
#print(str_to_float(user))

