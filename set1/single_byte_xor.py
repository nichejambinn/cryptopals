COMMON_CHARS = 'etaoinshrdlu'

def single_byte_xor(bytes, key):
    if len(key) > 1:
        raise ValueError("key must be single byte")
    
    return xor(bytes, key * len(bytes))

def xor(bytes1, bytes2):
    if len(bytes1) != len(bytes2):
        raise ValueError("both bytes must be equal length")
    
    return bytes(x^y for x,y in zip(bytes1, bytes2))

def character_frequency(text):
    return { char: text.count(char) for char in text }

if __name__=='__main__':
    ciphertext = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    cipher_bytes = bytes.fromhex(ciphertext)

    max_common_char_freqs = 0
    plaintext = ""
    for byte_value in range(256):
        key = bytes([byte_value])
        try:
            possible_plaintext = single_byte_xor(cipher_bytes, key).decode('utf-8')
            char_freq = character_frequency(possible_plaintext)
            common_char_freqs = sum([char_freq.get(char,0) for char in COMMON_CHARS])

            # theory: the secret is the possible plaintext with the most occurrences of common english chars
            if common_char_freqs > max_common_char_freqs:
                max_common_char_freqs = common_char_freqs
                plaintext = possible_plaintext

        except UnicodeDecodeError:
            continue

    print(plaintext) # Cooking MC's like a pound of bacon
        