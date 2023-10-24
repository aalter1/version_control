# function to encode 8 digit string
def encode(string):
    string_list = list(string)
    int_list = list(map(int, string_list))
    for i in range(len(int_list)):
        int_list[i] = int_list[i] + 3
        if int_list[i] > 9:
            int_list[i] = int_list[i] % 10
    new_str_list = list(map(str, int_list))
    return_to_string = "".join(new_str_list)
    return return_to_string


# Menu and options that repeat until quitting
def main():
    encode_program = True
    while encode_program == True:
        print("Menu")
        print("-" * 13)
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = int(input("Please enter an option: "))
        if option == 1:
            value = str(input("Please enter your password to encode: "))
            if len(str(value)) == 8:
                print("Your Password has been encoded and stored!")
            else:
                break
        if option == 2:
            encoded = encode(value)
            print(f"The encoded password is {encoded}, and the original password is {decode(encoded)}.")
            pass
        if option == 3:
            break


if __name__ == "__main__":
    main()
