import base64

# convert hex bytes such as b"\x13\x37\xbe\xef" into base64 bytes
def hex_to_b64(hex_str):
    hex_bytes = bytes.fromhex(hex_str)
    return base64.b64encode(hex_bytes)

if __name__=='__main__':
    test = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d" # I'm killing your brain like a poisonous mushroom
    res = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    assert hex_to_b64(test).decode('utf-8') == res, bytes.fromhex(test).decode('utf-8')