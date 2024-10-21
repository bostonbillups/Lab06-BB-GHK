# Group no 49
# Boston Billups, Gunho Kim

def encode(data):
    string = ""
    for item in data:
        item = int(item)
        item +=  3
        item = str(item)
        if item == '10':
            item = str(0)
        if item == '11':
            item = str(1)
        if item == '12':
            item = str(2)
        string += item
    return string

def decode(data):
    string = ""
    for item in data:
        item = int(item)
        item -= 3
        if item == -1:
            item = 9
        elif item == -2:
            item = 8
        elif item == -3:
            item = 7
        string += str(item)
    return string

if __name__ == '__main__':
    player_continue = True
    while player_continue:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        player_choice = float(input("Please enter an option: "))
        if player_choice == 1:
            password = str(input("Please enter your password to encode: "))
            password = encode(password)
            print("Your password has been encoded and stored!")
            print()
        elif player_choice == 2:
            print(f"The encoded password is {password}, and the original password is {decode(password)}")
        elif player_choice == 3:
            exit()
        elif player_choice != (1, 2, 3):
            print("Invalid input!\nPlease enter an integer value between 1 and 3.\n")
