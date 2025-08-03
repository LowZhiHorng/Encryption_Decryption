def base64Decode (message1_bytes):
    base64_message1_bytes = base64.b64decode(message1_bytes)
    return base64_message1_bytes.decode("utf-8")

def base85Decode (message1_bytes):
    base85_message1_bytes = base64.b85decode(message1_bytes)
    return base85_message1_bytes.decode("utf-8")


def base32Decode (message1_bytes):
    base32_message1_bytes = base64.b32decode(message1_bytes)
    return base32_message1_bytes.decode("utf-8")

def base16Decode (message1_bytes):
    base16_message1_bytes = base64.b16decode(message1_bytes)
    return base16_message1_bytes.decode("utf-8")


import base64

flag = True
while flag:
    print("\nDecryption System")

    print("\n1. Base 85 Decryption")
    print("2. Base 64 Decryption")
    print("3. Base 32 Decryption")
    print("4. Base 16 Decryption")

    try:
        type = int(input("\nWhat's your choice? (1/2/3/4): "))
    except ValueError:
        print("Invalid input. Please enter a number (1, 2, 3, or 4).")
        continue

    message1 = input("Decryption message: ")
    try:
        message1_bytes = message1.encode("ascii")
    except UnicodeEncodeError:
        print("Error: The decryption message should only contain ASCII characters (valid BaseX encoding).")
        continue

    try:
        if type == 1:
            message = base85Decode(message1_bytes)
        elif type == 2:
            message = base64Decode(message1_bytes)
        elif type == 3:
            message = base32Decode(message1_bytes)
        elif type == 4:
            message = base16Decode(message1_bytes)
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")
            continue
    except Exception as e:
        print(f"Error during decryption: {e}")
        print("Please ensure the input message is correctly encoded for the chosen BaseX type.")
        continue

    print("Decrypted message: " + message)

    next1 = input("\nDo you wanna continue? (Y/N): ")
    next1_upper = next1.upper()
    if next1_upper != "Y":
        flag = False