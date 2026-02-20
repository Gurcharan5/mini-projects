user_string = input("Enter the text you want to encrypt (lowercase): ")
length = len(user_string)

## Encrypt text
def split_text(text):
    letters = list(text)
    binary = []
    new_string_list = []
    new_string = ""
    
    for char in letters:
        if char.isalpha():
            binary_val = make_binary(char)
            new_string_list.append(binary_to_int(binary_val))
        else:
            new_string_list.append(char)
    
    for i in range(len(binary)):
        if binary[i] == "":
            new_string_list.append(" ")
        else:
            new_string_list.append(binary_to_int(binary[i]))

    for i in range(len(new_string_list)):
        new_string += new_string_list[i]

    print("The encrypted text is: " + new_string)
    decrypt_text(new_string)


def ceasur_text(message):
    global length
    letters = 'abcdefghijklmnopqrstuvwxyz'

    new_message = ""

    for x in message:
        if x in letters:
            new_message += letters[(letters.index(x) + length) % 26]

    return new_message

def make_binary(given_string):
    updated_string = ceasur_text(given_string)
    ascii_value = ord(updated_string)
    binary_value = bin(ascii_value)[2:]

    if len(binary_value) < 8:
        missing_0 = 8 - len(binary_value)
        string_to_add = ""
        for i in range(missing_0):
            string_to_add += "0"
        binary_value = string_to_add + str(binary_value)

    front_half_binary = binary_value[:4]
    back_half_binary = binary_value[4:]

    return swap_binary(front_half_binary, back_half_binary)

def swap_binary(front, back):
    temp = front
    front = back
    back = temp

    return (str(front) + str(back))


def binary_to_int(binary):
    integer = int(binary, 2)
    return int_to_ascii(integer)

def int_to_ascii(integer):
    letter = chr(integer)
    return letter


## Decrypt text
def decrypt_text(encrypted_string):
    global length
    original_length = length
    decrypted_result = ""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    for char in encrypted_string:
        if char == " ":
            decrypted_result += " "
            continue
            
        ascii_val = ord(char)
        binary_val = format(ascii_val, '08b')
        
        original_binary = binary_val[4:] + binary_val[:4]
        
        shifted_char = chr(int(original_binary, 2))
        
        if shifted_char in alphabet:
            original_idx = (alphabet.index(shifted_char) - original_length) % 26
            decrypted_result += alphabet[original_idx]
        else:
            decrypted_result += shifted_char
            
    print("The decrypted text is: " + decrypted_result)

split_text(user_string)
