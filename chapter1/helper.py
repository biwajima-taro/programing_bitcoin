import hashlib
BASE58_ALPHABET = ""


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
