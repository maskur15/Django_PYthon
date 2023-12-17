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


# Example usage
encryption_password = "my_secure_password"
plaintext_message = "Hello, AES encryption!"

combined_value = encrypt_text(encryption_password, plaintext_message)
print(f"Combined Value: {combined_value}")

decrypted_text = decrypt_text('boy', combined_value='1euBQ0r+mWcVarzn99vtXolW8Vm/xlc8yUknzIkvQjn+f/TeF43JCgjCaHy03A==')
print(f"Decrypted Text: {decrypted_text}")
