def base64Encode (message1_bytes):
    base64_message1_bytes = base64.b64encode(message1_bytes)
    base64_message1 = base64_message1_bytes.decode("utf-8")

    return base64_message1

def base85Encode (message1_bytes):
    base85_message1_bytes = base64.b85encode(message1_bytes)
    base85_message1 = base85_message1_bytes.decode("utf-8")

    return base85_message1

def base32Encode (message1_bytes):
    base32_message1_bytes = base64.b32encode(message1_bytes)
    base32_message1 = base32_message1_bytes.decode("utf-8")

    return base32_message1

def base16Encode (message1_bytes):
    base16_message1_bytes = base64.b16encode(message1_bytes)
    base16_message1 = base16_message1_bytes.decode("utf-8")

    return base16_message1


import base64

flag = True
while flag:
    print("\nEncryption System")

    print("\n1. Base 85 Encryption")
    print("2. Base 64 Encryption")
    print("3. Base 32 Encryption")
    print("4. Base 16 Encryption")

    try:
        type = int(input("\nWhat's your choice? (1/2/3/4): "))
    except ValueError:
        print("Invalid input. Please enter a number (1, 2, 3, or 4).")
        continue

    message1 = input("Encryption message: ")
    message1_bytes = message1.encode("utf-8")

    if type == 1:
        message = base85Encode(message1_bytes)
    elif type == 2:
        message = base64Encode(message1_bytes)
    elif type == 3:
        message = base32Encode(message1_bytes)
    elif type == 4:
        message = base16Encode(message1_bytes)
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")
        continue

    print("Encrypted message: " + message)

    next1 = input("\nDo you wanna continue? (Y/N): ")
    next1_upper = next1.upper()
    if next1_upper != "Y":
        flag = False