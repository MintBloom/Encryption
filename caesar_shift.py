
def EncryptOrDecrypt():
    print ("Decrypt or encrypt?")
    choice = str(input())
    if choice == "decrypt":
        deCypher()
    elif choice == "encrypt":
        Cypher()

def Cypher():
    print ("what message would you like to decrypt?")
    msg = str(input())
    print ("shift value:")
    shift = int(input())
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypt_msg = ""
    for i in msg:
        if i == " ":
            encrypt_msg += i
        else:
            encrypt_msg += alphabet[(alphabet.find(i) + shift) % len(alphabet)]    
    print (f"encryption: {encrypt_msg}")

def deCypher():
    print ("what message would you like to decrypt?")
    msg = str(input())
    print ("shift value:")
    shift = int(input())
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypt_msg = ""
    for i in msg:
        if i == " ":
            encrypt_msg += i
        else:
            encrypt_msg += alphabet[(alphabet.find(i) - shift) % len(alphabet)]    
    print (f"decryption: {encrypt_msg}")

EncryptOrDecrypt()