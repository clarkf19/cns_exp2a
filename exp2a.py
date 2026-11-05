alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def caesar_encrypt(text,key):
    result=""
    for ch in text:
            p=alphabet.index(ch)
            c=(p+key)%26
            result=result+alphabet[c]
    return result

def caesar_decrypt(text,key):
      result=""
      for ch in text:
            c=alphabet.index(ch)
            p=(c-key)%26
            result=result+alphabet[p]
      return result

text=input("Enter message:")
key=int(input("Enter key:"))
cipher=caesar_encrypt(text,key)
print("Encrypted message:", cipher)
print("Decrypted message:", caesar_decrypt(cipher,key))