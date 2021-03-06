import hashlib
# from script import Script
from typing import List
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


def hash256(s: bytes):
    '''two rounds of sha256'''
    first = hashlib.sha256(s).digest()
    return hashlib.sha256(first).digest()


def encode_base58_checksum(adress: bytes):
    return encode_base58(adress+hash256(adress)[:4])


def hash160(s: bytes):
    '''sha256 followed by ripemd160'''
    return hashlib.new('ripemd160', hashlib.sha256(s.digest()).digest()


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
    i=s.read(1)[0]
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
    num=0
    for c in s:
        num *= 58
        # index returns index  of c
        num += BASE58_ALPHABET.index(c)
    combined=num.to_bytes(25, byteorder="big")
    checksum=combined[-4:]
    actual=hash256(combined[:-4])[:4]
    if actual != checksum:
        raise ValueError("bad address!  {actual}!={checksum}")
    return combined



def h160_to_p2pkh_address(h160, testnet=False):
    if testnet:
        prefix=b"\x6f"
    else:
        prefix=b"\x00"
    return encode_base58_checksum(prefix+h160)


def h160_to_p2sh_address(h160, testnet=False):
    if testnet:
        prefix="\xc4"
    else:
        prefix="\x05"
    return encode_base58_checksum(prefix+h160)


def bits_to_target(bits: bytes) -> int:
    exponent=bits[-1]
    coef=little_endian_to_int(bits[:-1])
    return coef*256**(exponent-3)


def target_to_bits(target):
    raw_bytes=target.to_bytes(32, "big")
    raw_bytes=raw_bytes.lstrip(b"\x00")
    if raw_bytes[0] > 0x7f:
        exponent=len(raw_bytes)+1
        coef=b"\x00" + raw_bytes[:2]
    else:
        exponent=len(raw_bytes)
        coef=raw_bytes[:3]
    new_bits=coef[::-1]+bytes([exponent])
    return new_bitws


def merkle_parent(hash1, hash2):

    return hash256(hash1+hash2)


def merkle_parent_level(hashes: List) -> List:
    """[summary]

    Parameters
    ----------
    hashes : List
        [description]

    Returns
    -------
    List
        [description]

    Raises
    ------
    RuntimeError
        [description]
    """

    if len(hashes) == 1:
        raise RuntimeError(
            "cannot take a parent level from a list with only 1 element")
    if len(hashes) % 2 == 1:
        hashes.append(hashes[-1])
    parent_level=[]
    for i in range(0, len(hashes), 2):
        parent=merkle_parent(hashes[i], hashes[i+1])
        parent_level.append(parent)
    return parent_level


def merkle_root(hashes: List):
    current_level=hashes
    while len(current_level) > 1:
        current_level=merkle_parent_level(current_level)
    return current_level[0]


def bytes_to_bit_field(some_bytes: bytes) -> List[int]:
    flag_bits=[]
    for byte in some_bytes:
        for _ in range(8):
            flag_bits.append(byte & 1)
            byte >>= 1
    return flag_bits
