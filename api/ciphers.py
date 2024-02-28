def caesar_encode(plain_text, shift):
    cipher_text = ""
    for c in plain_text:
        if (ord(c) >= ord('a')):
            c_encoded = ord(c) + shift
            if (c_encoded > ord('z')): 
                c_encoded = c_encoded - 26
        else:
            c_encoded = ord(c) + shift
            if (c_encoded > ord('Z')): 
                c_encoded = c_encoded - 26
        c_encoded = chr(c_encoded)
        cipher_text += c_encoded
    return cipher_text