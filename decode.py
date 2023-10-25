def decode(coded_password):
    decoded_password = ""
    for char in coded_password:
        if int(char) < 3:
            decoded_password += str(int(char) + 7)
        else:
            decoded_password += str(int(char) - 3)
    return decoded_password