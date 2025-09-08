from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad,unpad
secret_key=get_random_bytes(16)
print(secret_key)
cipher_obj=AES.new(secret_key,AES.MODE_CBC)
print(cipher_obj)
iv=cipher_obj.iv
print(iv)
user_input=input("Enter the string: ")
padded_text=pad(user_input.encode(),AES.block_size)
print(padded_text)
encrypted_msg=cipher_obj.encrypt(padded_text)
print(encrypted_msg)
decipher_obj=AES.new(secret_key,AES.MODE_CBC,iv)
print(decipher_obj)
decrypted_msg=unpad(decipher_obj.decrypt(encrypted_msg),AES.block_size).decode()
print(decrypted_msg)
