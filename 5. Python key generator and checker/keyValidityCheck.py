key_to_check= input("Please enter your key: ")

key = key_to_check.split("-")

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m'
           ,'n','o','p','q','r','s','t','u','v','w','x','y','z']


def invalid_key():
    print("That is not a valid key!")


def reverse_step(index):
    if index + 3 > 25:
        return (index + 3) % 26
    else:
        return index + 3
    

def check_section_1(key):
    section1 = key[0]
    key_letters = []
    start_index = 0

    for letter in section1:
        key_letters.append(letter)

    for i in range(len(letters)):
        if key_letters[0] == letters[i]:
            start_index = i

    new_index = reverse_step(start_index)
    check1 = letters[new_index]

    if check1 == key_letters[1]:
        pass
    else:
        invalid_key()

    new_index = reverse_step(new_index)
    check2 = letters[new_index]

    if check2 == key_letters[2]:
        check_section_2(key)
    else:
        invalid_key()

def check_section_2(key):
    total = key[2]
    number = total[:2]
    number = int(number)
    number_total = 0

    numbers = key[1]
    numbers_array = []

    for value in numbers:
        numbers_array.append(value)

    for i in range(len(numbers_array)):
        number_total += int(numbers_array[i])

    if number_total == number:
        print("That is a valid key!")
    else:
        invalid_key()


check_section_1(key)