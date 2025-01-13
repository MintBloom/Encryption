
# Opening function giving option to encrypt or decrypt a message
def EncryptOrDecrypt():
    print ("Decrypt or encrypt?")
    choice = str(input()) 
    if choice == "decrypt":
        deCypher()
    elif choice == "encrypt":
        Cypher()

#Function which encrypts messages
def Cypher():
    print ("what message would you like to encrypt?")

    # user can type message that is to be encrypted
    msg = str(input())
    print ("shift value:")
    
    # user can type the number of shifts they want to a message
    shift = int(input())
    index = "abcdefghijklmnopqrstuvwxyz" # the set of characters that will be used to replace the original message
    encrypt_msg = ""

    # loop will be repeated for every character in msg
    for i in msg:
        if i == " ":
            encrypt_msg += i # whenever there is a space in the msg it will be replaced with another space
        else:
            encrypt_msg += index[(index.find(i) + shift) % len(index)]    
    print (f"encryption: {encrypt_msg}")

# Function which decrypts messages
def deCypher():
    print ("what message would you like to decrypt?")
    
    # user can type message that is to be decrypted
    msg = str(input())
    print ("shift value:")

    # user can type an (integer) amount of shifts that was used to encode the message
    shift = int(input())
    index = "abcdefghijklmnopqrstuvwxyz" # the set of characters that the msg will be compared to and shifted against, allowing for decryption
    decrypt_msg = ""

    # loop will be repeated for every character in msg
    for i in msg:
        if i == " ":
            decrypt_msg += i # whenver there there is a space in the msg it will be replaced with a space 
        else:
            ''' decrypt_msg is created by concatenating each new character that is found with each loop, with the character(s) from the previous
            loop(s). 
            To find the new characters: 1. the position of the first character from msg is found in the index string. this position
            (which is an integer) has a number taken away from it (the amount of shifts specified by the user in shift variable) to create a new 
            position (another integer that will be called x). the character at this new position is stored in decrypt_msg. these steps are repeated
            until there are no further characters in msg. 
            The modulus is taken of x (refer to above) with the length of index, to find a suitable new position of a character IF it exceeds the
            length of the index.
            '''
            decrypt_msg += index[(index.find(i) - shift) % len(index)]    
    print (f"decryption: {decrypt_msg}") # output of the function

EncryptOrDecrypt()