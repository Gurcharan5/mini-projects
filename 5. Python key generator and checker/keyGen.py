import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m'
           ,'n','o','p','q','r','s','t','u','v','w','x','y','z']

numbers = [0,1,2,3,4,5,6,7,8,9]

letters_length = 26
numbers_length = 10

generated_key = ""

def stepped_letter1(number):
    if number + 3 > 25:
        return (number + 3) % 26
    else:
        return number + 3
    

def generate_section1():
    letter1_number = random.randint(0, letters_length-1)
    letter1 = letters[letter1_number]

    letter2_number = stepped_letter1(letter1_number)
    letter2 = letters[letter2_number]

    letter3_number = stepped_letter1(letter2_number)
    letter3 = letters[letter3_number]

    letter4_number = stepped_letter1(letter3_number)
    letter4 = letters[letter4_number]

    section1 = letter1 + letter2 + letter3 + letter4

    global generated_key
    generated_key += section1
    generated_key += "-"

    generate_section2()


def generate_section2():
    total = 0

    number1_number = random.randint(0, numbers_length-1)
    total += number1_number
    number1_value = numbers[number1_number]

    number2_number = random.randint(0, numbers_length-1)
    total += number2_number
    number2_value = numbers[number2_number]

    number3_number = random.randint(0, numbers_length-1)
    total += number3_number
    number3_value = numbers[number3_number]

    number4_number = random.randint(0, numbers_length-1)
    total += number4_number
    number4_value = numbers[number4_number]
    
    generated_section2 = str(number1_value) + str(number2_value) + str(number3_value) + str(number4_value)

    global generated_key 
    generated_key += generated_section2
    generated_key += "-"

    generate_section3(total)


def generate_section3(total):
    total_string = str(total) + str(total)
    
    global generated_key
    generated_key += total_string


generate_section1()
print("Your key is: " + generated_key)
