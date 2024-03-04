def xor(bytes1, bytes2):
    if len(bytes1) != len(bytes2):
        raise ValueError("both bytes must be equal length")
    
    return bytes(x^y for x,y in zip(bytes1, bytes2))

if __name__=='__main__':
    test1 = "1c0111001f010100061a024b53535009181c"
    test2 = "686974207468652062756c6c277320657965"
    res = "746865206b696420646f6e277420706c6179" # the kid don't play
    assert xor(bytes.fromhex(test1), bytes.fromhex(test2)).hex() == res, bytes.fromhex(res).decode('utf-8')
