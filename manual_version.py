user_input=input("Enter a string :")
print("Here we are using Caesar Cipher. Manual version.")
print("Encrypt")
arr=[]
for i in range(len(user_input)):
    if ('a' <= user_input[i] <= 'z'):
        nu1=ord(user_input[i])
        arr.append(((nu1-97+3)%26)+97)
    elif('A' <= user_input[i] <= 'Z'):
        nu2=ord(user_input[i])
        arr.append(((nu2-65+3)%26)+65)
    elif('0' <= user_input[i] <= '9'):  
        nu3=(ord(user_input[i])-ord('0'))
        arr.append(((nu3+3)%10)+ord('0'))
    else:
        arr.append(ord(user_input[i]))
print("encrypted data:", arr)  
en_user=[]          
for i in range(len(arr)):
    en_user.append(chr(arr[i]))
en_user=''.join(en_user)
print(en_user)    
print("Decrypt")
arr1=[]
for i in range(len(en_user)):
    if ('a' <= en_user[i] <= 'z'):
        nu1=ord(en_user[i])
        arr1.append(((nu1-97-3)%26)+97)
    elif('A' <= en_user[i] <= 'Z'):
        nu2=ord(en_user[i])
        arr1.append(((nu2-65-3)%26)+65)
    elif('0' <= en_user[i] <= '9'):  
        nu3=(ord(en_user[i])-ord('0'))
        arr1.append(((nu3-3)%10)+ord('0'))    
    else:
        arr1.append(ord(en_user[i]))    
print("decrypted data:", arr1)  
de_user=[]          
for i in range(len(arr1)):
    de_user.append(chr(arr1[i]))
de_user=''.join(de_user)
print(de_user) 