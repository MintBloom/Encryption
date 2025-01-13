
def MessageToEncode():
    print ("What message would you like to encode?")
    Cypher()
    

def Cypher():
    msg = str(input())
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypt_msg = ""
    offset = 3
    for i in msg:
        if i == " ":
            encrypt_msg += i
        else:
            encrypt_msg += alphabet[(alphabet.find(i) + offset) % len(alphabet)]    
    print (f"encryption: {encrypt_msg}")

MessageToEncode()