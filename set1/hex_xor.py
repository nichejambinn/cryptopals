def xor(hexbytes1, hexbytes2):
    if len(hexbytes1) != len(hexbytes2):
        raise ValueError("hex bytes must be equal length")
    
    return bytes(x^y for x,y in zip(hexbytes1, hexbytes2))

def bytes_to_hex_str(byte_str):
    return ''.join(format(byte, '02x') for byte in byte_str)

if __name__=='__main__':
    test1 = "1c0111001f010100061a024b53535009181c"
    test2 = "686974207468652062756c6c277320657965"
    res = "746865206b696420646f6e277420706c6179" # the kid don't play
    assert bytes_to_hex_str(xor(bytes.fromhex(test1), bytes.fromhex(test2))) == res, bytes.fromhex(res).decode('utf-8')
