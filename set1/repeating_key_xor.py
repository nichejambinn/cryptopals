def xor(bytes1, bytes2):
    if len(bytes1) != len(bytes2):
        raise ValueError("both bytes must be equal length")
    
    return bytes(x^y for x,y in zip(bytes1, bytes2))

def repeating_key_xor(plainbytes, key):
    if len(key) > len(plainbytes):
        raise ValueError("key length exceeds plaintext")

    keybytes = key*(len(plainbytes)//len(key)) + key[:len(plainbytes) % len(key)]

    return xor(plainbytes, keybytes)

if __name__=='__main__':
    test = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = "ICE"
    res = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
    output = repeating_key_xor(bytes(test, 'utf-8'), bytes(key, 'utf-8')).hex()
    assert output == res, "fail"
    