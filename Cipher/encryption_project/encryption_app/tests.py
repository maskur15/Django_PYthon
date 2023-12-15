from django.test import TestCase

# Create your tests here.
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_plaintext = pad(plaintext.encode(), AES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = cipher.decrypt(ciphertext)
    plaintext = unpad(decrypted_data, AES.block_size)
    return plaintext.decode()

# Example usage:
if __name__ == "__main__":
    # Generate a random 128-bit key (16 bytes)
    key = get_random_bytes(16)

    # Text to be encrypted
    original_text = "Hello, AES!"

    # Encrypt
    encrypted_text = encrypt(original_text, key)
    print(f"Encrypted Text: {encrypted_text.hex()}")

    # Decrypt
    decrypted_text = decrypt(encrypted_text, key)
    print(f"Decrypted Text: {decrypted_text}")
