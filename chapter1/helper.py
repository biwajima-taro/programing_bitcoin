import hashlib
BASE58_ALPHABET = ""


def int_to_little_endiant(n: int, length:int) -> bytes:
    """convert int to bytes in designated length"""
    return n.to_bytes(length, "little")


def encode_variant(i: int):
    """encode integer as a variant."""

    if i < 0xfd:
        # below 253,
        return bytes([i])
    elif i < 0x10000:
        return b'0xfd'+int_to_little_endiant(i, 2)
    elif i<0x100000000:
        return b'0xff'+int_to_little_endiant(i,8)
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
    # TODO:write rest of the function
    return result


def hash256(s: str) -> str:
    # https://www.pebblewind.com/entry/2018/05/05/230100
    # s.encode('utf-8')にする必要がある？
    return hashlib.new("rpemd160", hashlib.sha256(s).digest()).digest()


def encode_base58_checksum(b):
    return encode_base58(b+hash256(b)[:4])


if __name__=="__main__":
    print(int_to_little_endiant(123,3))