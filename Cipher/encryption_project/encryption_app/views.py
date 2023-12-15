from django.shortcuts import render,redirect,HttpResponse
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from PIL import Image 
from django.contrib import messages 
import imghdr
# Create your views here.

def encrypt_image(request):
    if request.method=='POST':
        print('work fine ')
        if request.FILES['image']:
            orginal_image = request.FILES['image']
            image_type = imghdr.what(orginal_image)
            if image_type not in ['jpeg','png','gif']:
                messages.SUCCESS("Invalid file. Upload an image <jpeg,png,gif>")
                return redirect('home')
        else:
            messages.SUCCESS("Invalid file. Upload an image <jpeg,png,gif>")
            return redirect('home')

            
    return render(request,'encrypt_image.html')
def encrypt_stegano(request):

    return render(request,'stegano.html',{})

def encrypt(plaintext):
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_ECB)
    padded_plaintext = pad(plaintext.encode(), AES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return key,ciphertext

def decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = cipher.decrypt(ciphertext)
    plaintext = unpad(decrypted_data, AES.block_size)
    return plaintext.decode()
def showHome(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        image = request.FILES.get('image')
        type_value = request.POST.get('type')
        if type_value=='text' and text:
            
            # Encrypt
            key,encrypted_text = encrypt(text)
            print(f"Encrypted Text: {encrypted_text.hex()}")
            print(f'key is : {key}')
            print(f'Decrypted text : {decrypt(encrypted_text,key)}')

            return render(request,'home.html',{'key':key,'text':encrypted_text})
    return render(request, 'home.html', {})

s="506bf2130b21f114e1caf92ed54ea94640d03b7ec7e1558342d50b80e2d0e4b1"
key= "{V\xb0\x03\xcc\xe3\x16\xe6\xcf\x87m\\\xb5\x8b\xf9\xf9"