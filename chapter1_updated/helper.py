BASE58_ALPHABET = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'


def encode_base58(s: bytes) -> str:
    # count how many 0 are at start
    count = 0cv
    for c in s:
        if c == 0:
            count += 1
        else:
            break
        prefix = "1"*count
        num = int.from_bytes(s, "big")
        result = ""
        while num > 0:
            num, mod = divmod(num, 58)
            result = BASE58_ALPHABET[mod]+result
        return prefix+result
