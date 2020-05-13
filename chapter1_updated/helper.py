import hashlib
from script import Script
BASE58_ALPHABET = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'


def encode_base58(s: bytes) -> str:
    # count how many 0 are at start
    count = 0
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


def hash256(s):
    '''two rounds of sha256'''
    return hashlib.sha256(hashlib.sha256(s).digest()).digest()


def encode_base58_checksum(adress: bytes):
    return encode_base58(adress+hash256(adress)[:4])


def hash160(s):
    '''sha256 followed by ripemd160'''
    return hashlib.new('ripemd160', hashlib.sha256(s).digest()).digest()


def little_endian_to_int(b: bytes) -> int:
    """[summary]

    Parameters
    ----------
    b : bytes
        [description]

    Returns
    -------
    int
        [description]
    """
    return int.from_bytes(b, "little")


def int_to_little_endian(n: int, length: int):
    return n.to_bytes(length, "little")


def read_variant(s):
    i = s.read(1)[0]
    if i == 0xfd:
        return little_endian_to_int(s.read(2))


def encode_variant(length_: int):
    if length_ < 0xfd:
        return bytes([length_])
    elif length_ < 0x10000:
        return b"\xfd"+int_to_little_endian(length_, 2)
    elif length_ < 0x100000000:
        return b"\xfe"+int_to_little_endian(length_, 4)
    elif length_ < 0x10000000000000000:
        return b"\xff"+int_to_little_endian(length_, 8)
    else:
        raise ValueError(f"integer too large {length_}")


def decode_base58(s):
    num = 0
    for c in s:
        num *= 58
        # index returns index  of c
        num += BASE58_ALPHABET.index(c)
    combined = num.to_bytes(25, byteorder="big")
    checksum = combined[-4:]
    actual = hash256(combined[:-4])[:4]
    if actual != checksum:
        raise ValueError("bad address!  {actual}!={checksum}")
    return combined


def p2pkh_script(h160: bytes):
    """[summary]
    return p2pkh script pubkey
    Parameters
    ----------
    h160 : bytes
        [description]

    Returns
    -------
    [type]
        [description]
    """
    return Script([0x76, 0xa9, h160, 0x88, 0xac])


def h160_to_p2pkh_address(h160, testnet=False):
    if testnet:
        prefix = b"\x6f"
    else:
        prefix = b"\x00"
    return encode_base58_checksum(prefix+h160)


def h160_to_p2sh_address(h160, testnet=False):
    if testnet:
        prefix = "\xc4"
    else:
        prefix = "\x05"
    return encode_base58_checksum(prefix+h160)


def bits_to_target(bits: bytes) -> int:
    exponent = bits[-1]
    coef = little_endian_to_int(bits[:-1])
    return coef*256**(exponent-3)


def target_to_bits(target):
    raw_bytes = target.to_bytes(32, "big")
    raw_bytes = raw_bytes.lstrip(b"\x00")
    if raw_bytes[0] > 0x7f:
        exponent = len(raw_bytes)+1
        coef = b"\x00" + raw_bytes[:2]
    else:
        exponent = len(raw_bytes)
        coef = raw_bytes[:3]
    new_bits = coef[::-1]+bytes([exponent])
    return new_bitws
