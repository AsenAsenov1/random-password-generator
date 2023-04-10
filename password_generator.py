import random


def generate_pass():
    special_characters = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '_', '-', '+', '=', '`', '|', '\\', '(', ')',
                          '{', '}', '[', ']', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']
    # ASCII chars [a-z]
    lower_letters = [chr(x) for x in range(97, 123)]
    # ASCII chars [A-Z]
    upper_letters = [chr(x) for x in range(65, 91)]
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    all_symbols = [special_characters, lower_letters, upper_letters, digits]
    password = []
    for i in range(len(all_symbols)):
        for symbol_list in all_symbols:
            current_char = random.choice(symbol_list)
            password += str(current_char)
    random.shuffle(password)
    result = "".join(password)
    print(result)
    



generate_pass()

while True:
    key = input("Press 'n' to exit or any other key to generate new password.\n")
    if key == 'n':
        break
    generate_pass()

