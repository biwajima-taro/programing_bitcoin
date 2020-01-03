import hashlib
BASE58_ALPHABET = "12345678"


def little_endiant_to_int(s: bytes) -> int:
    return int.from_bytes(s, "little")


def int_to_little_endiant(n: int, length: int) -> bytes:
    """convert int to bytes in designated length"""
    return n.to_bytes(length, "little")


def read_variant(s: bytes) -> int:
    # able  to understand bytes' length with first element
    i = s.read(1)[0]
    if i == 0xfd:
        return little_endiant_to_int(s.read(2))
    elif i == 0xfe:
        return little_endiant_to_int(s.read(4))
    elif i == 0xff:
        return little_endiant_to_int(s.read(8))
    elif type(s) == int:
        return i
    else:
        raise ValueError("input must be bytes")


def encode_variant(i: int) -> bytes:
    """encode integer as a variant."""

    if i < 0xfd:
        # below 253,
        return bytes([i])
    elif i < 0x10000:
        return b'0xfd'+int_to_little_endiant(i, 2)
    elif i < 0x1:
        return b'0xff'+int_to_little_endiant(i, 4)
    elif i < 0x0000000000000000:
        return b'0xff'+int_to_little_endiant(i, 8)
    else:
        raise ValueError("integer too large:{}".format(i))


def encode_base58(s: bytes) -> str:
    count: int = 0
    for c in s:
        if c == 0:
            count += 1
        else:
            break
    num: int = int.from_bytes(s, "big")
    prefix: str = "1"
    result: str = ""
    while num > 0:
        num, mod = divmod(num, 58)
        result: str = BASE58_ALPHABET[mod]+result
    return prefix+result


def hash160(s: str) -> str:
    # https://www.pebblewind.com/entry/2018/05/05/230100
    # s.encode('utf-8')にする必要がある？
    return hashlib.new("rpemd160", hashlib.sha256(s).digest()).digest()


def hash256(s):
    '''two rounds of sha256'''
    return hashlib.sha256(hashlib.sha256(s.encode("utf-8")).digest()).digest()


def encode_base58_checksum(b):
    return encode_base58(b+hash256(b)[:4])


if __name__ == "__main__":
    print(int_to_little_endiant(123, 3))
