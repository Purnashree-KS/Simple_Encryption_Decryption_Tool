import cryptography
from cryptography.fernet import Fernet
secret_key=Fernet.generate_key()
print(secret_key)
print(type(secret_key))
cipher_text=Fernet(secret_key)
print(cipher_text)
print(type(cipher_text))
user_input=input("Enter string:").encode()
encrypt_msg=cipher_text.encrypt(user_input)
print(encrypt_msg)
decrypt_msg=cipher_text.decrypt(encrypt_msg)
print(decrypt_msg.decode('utf-8'))