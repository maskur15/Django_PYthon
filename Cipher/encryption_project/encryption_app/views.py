from django.shortcuts import render,redirect,HttpResponse

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from base64 import b64encode, b64decode
import os

def derive_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000,  # You can adjust the number of iterations based on your security requirements
        salt=salt,
        length=32  # 32 bytes for AES-256
    )
    return kdf.derive(password.encode('utf-8'))

def encrypt_text(password, text):
    salt = os.urandom(16)
    key = derive_key(password, salt)

    iv = os.urandom(16)

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    ciphertext = encryptor.update(text.encode('utf-8')) + encryptor.finalize()

    # Concatenate salt and IV to the ciphertext
    combined_value = salt + iv + ciphertext

    return b64encode(combined_value).decode('utf-8')

def decrypt_text(password, combined_value):
    combined_value = b64decode(combined_value)

    # Extract salt, IV, and ciphertext from the combined value
    salt = combined_value[:16]
    iv = combined_value[16:32]
    ciphertext = combined_value[32:]

    key = derive_key(password, salt)

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    return plaintext.decode('utf-8')


def cipherImage(request):
    if request.method=='POST':
        try:
            uploaded_file = request.FILES['image']

            # Generate a unique file name
            file_name = default_storage.get_available_name(uploaded_file.name)

            # Save the file to the MEDIA_ROOT using default_storage
            path = default_storage.save('uploads/' + file_name, ContentFile(uploaded_file.read()))
            print(path)
            return render(request, 'encrypt_image.html', {'image_path':path})
      

        except Exception as e:
            pass
    return render(request,'encrypt_image.html')
def encrypt_stegano(request):
    return render(request,'stegano.html',{})
def decryptText(request):
    if request.method=='POST':
        cipher_text = request.POST.get('text')
        password = request.POST.get('password')
        print(type(cipher_text),type(password))
        text = decrypt_text(password,cipher_text)
        print(text)
        return render(request,'decrypt_text.html',{"text":text})
        pass
    return render(request,'decrypt_text.html')

def showHome(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        password = request.POST.get('password')
        encrypted_text = encrypt_text(password=password,text=text)
        print(encrypted_text,type(encrypted_text),password,type(password))
        decrypted_text = decrypt_text(password,encrypted_text)
        print(f"Decrypted Text: {decrypted_text}")
        
        return render(request,'home.html',{'cipher_text':encrypted_text})
    return render(request, 'home.html', {})

s="506bf2130b21f114e1caf92ed54ea94640d03b7ec7e1558342d50b80e2d0e4b1"
key= "{V\xb0\x03\xcc\xe3\x16\xe6\xcf\x87m\\\xb5\x8b\xf9\xf9"
x='068ff32ad336fef758884b4f83d7343d'
y="b'(\xdd\xfb\xe2\x9c\x98JD\xb3\x01\xc7\x84\xab\xd29\\'"