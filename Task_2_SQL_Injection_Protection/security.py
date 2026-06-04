from cryptography.fernet import Fernet
SECRET_KEY = b"xnSBII6NOEO_VV2oiKXaJjd6J38T6VqELVF12Ae7F5U="
cipher = Fernet(SECRET_KEY)

def encrypt_data(data):

    encrypted = cipher.encrypt(
        data.encode()
    )

    return encrypted.decode()

def decrypt_data(data):

    decrypted = cipher.decrypt(
        data.encode()
    )

    return decrypted.decode()