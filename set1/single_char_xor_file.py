import heapq

def single_byte_xor(hex_bytes, key):
    if len(key) > 1:
        raise ValueError("key must be single byte")
    
    return xor(hex_bytes, key * len(hex_bytes))

def xor(hexbytes1, hexbytes2):
    if len(hexbytes1) != len(hexbytes2):
        raise ValueError("hex bytes must be equal length")
    
    return bytes(x^y for x,y in zip(hexbytes1, hexbytes2))

def character_frequency(text):
    return { char: text.count(char) for char in text }

def single_byte_xor_frequency_analysis(cipher_bytes, test_chars='etaoinshrdlu'):
    possible_plaintexts = {}
    # xor ciphertext bytes with single byte key
    for byte_value in range(256):
        key = bytes([byte_value])
        try:
            possible_plaintext = single_byte_xor(cipher_bytes, key).decode('utf-8')
            char_freq = character_frequency(possible_plaintext)

            # sum the number of occurrences of test chars within possible plaintext
            common_char_freqs = sum(char_freq.get(char,0) for char in test_chars)

            possible_plaintexts[possible_plaintext] = common_char_freqs
        except UnicodeDecodeError:
            continue

    return possible_plaintexts


if __name__=='__main__':
    with open("chall4.txt", "r") as file:
        top_plaintexts = {}
        for ciphertext in file.readlines():
            cipher_bytes = bytes.fromhex(ciphertext)
            possible_plaintexts = single_byte_xor_frequency_analysis(cipher_bytes)
            if possible_plaintexts:
                top_plaintexts.update(heapq.nlargest(3, possible_plaintexts.items(), key=lambda x: x[1]))
                
        top_3 = heapq.nlargest(3, top_plaintexts.items(), key=lambda x: x[1])
        print(top_3) # Now that the party is jumping
    