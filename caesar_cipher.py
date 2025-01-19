def encrypt(message, key):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                key_shift = ord(char) + key
                if key_shift > ord('Z'):
                    key_shift = key_shift - ord('Z')
                    key_shift += ord('A') - 1
                encrypted_message += chr(key_shift)
            elif char.islower():
                key_shift = ord(char) + key
                if key_shift > ord('z'):
                    key_shift = key_shift - ord('z')
                    key_shift += ord('a') - 1
                encrypted_message += chr(key_shift)
        else:
            encrypted_message += char
    return encrypted_message
def decrypt(message, key):
    decrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                key_shift = ord(char) - key
                if key_shift < ord('A'):
                    key_shift = ord('A') - key_shift
                    key_shift = ord('Z') - key_shift + 1
                decrypted_message += chr(key_shift)
            elif char.islower():
                key_shift = ord(char) - key
                if key_shift < ord('a'):
                    key_shift = ord('a') - key_shift
                    key_shift = ord('z') - key_shift + 1
                decrypted_message += chr(key_shift)
        else:
            decrypted_message += char
    return decrypted_message

def main():
    input_str = input("Enter a string: ")
    code = int(input("Enter the code: "))
    print("Choose your option:")
    print("1. Encrypt")
    print("2. Decrypt")
    option = int(input("Enter your option: "))
    if option == 1:
        print("Encrypted Message:", encrypt(input_str, code))
    elif option == 2:
        print("Decrypted Message:", decrypt(input_str, code))
    else:
        print("Invalid option!")

main()