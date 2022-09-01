from Crypto.Cipher import AES

if __name__ == "__main__":
    toExecute = 'print("malitious code executed")'.encode("utf-8")
    key = b'sixteen byte key'
    cipher = AES.new(key, AES.MODE_EAX)
    
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(toExecute)

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        # print("The message is authentic:", plaintext)
        eval(plaintext)
    except ValueError:
        print("Key incorrect or message corrupted")