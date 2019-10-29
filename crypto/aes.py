import base64

from Crypto import Random
from Crypto.Cipher import AES

BS = 16
def pad(data):
    padding = BS - len(data) % BS
    return data + padding * chr(padding)

def unpad(data):
    return data[0:-ord(data[-1])]

def decrypt_node(hex_data, key='0'*32, iv='0'*16):
    data = ''.join(map(chr, bytearray.fromhex(hex_data)))
    print(len(data))
    aes = AES.new(key, AES.MODE_CBC, iv)
    return unpad(aes.decrypt(data))

def encrypt_node(data, key='0'*16, iv='0'*16):
    aes = AES.new(key, AES.MODE_CBC, iv)
    return aes.encrypt(pad(data)).hex()
    # return base64.b64encode(aes.encrypt(pad(data))).decode('utf-8')

print(encrypt_node('this-needs-to-be-encrypted'))
# print(decrypt_node('b88e5f69c7bd5cd67c9c12b9ad73e8c1ca948ab26da01e6dad0e7f95448e79f4'))