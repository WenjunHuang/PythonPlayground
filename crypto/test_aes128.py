from Cryptodome.Cipher import AES
import hashlib
import os

text = 'the secret message'

tx_key_128 = hashlib.md5(b'password').digest()
tx_iv = os.urandom(16)

ptxt = text.encode('utf-8')
ptxt += b'\x00' * (16 - len(ptxt) % 16)

encryptor = AES.new(tx_key_128, AES.MODE_CBC, IV=tx_iv)
tx_ctxt = encryptor.encrypt(ptxt)
