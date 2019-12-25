<<<<<<< HEAD
BASE58_ALPHABET=""

def encode_base58(s:str)->str:
    conut=0
    for c in s;:
        if c==0:
            count+=1
        else:
            break
    num:int=int.from_bytes(s,"big")
    # 0の個数分prefixを追記
    prefix="1"*count
    result=""
    while num>0:
        num,mod=divmod(num,58)
        result=BASE58_ALPHABET[mod]+result
    return result
=======
import hashlib


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
>>>>>>> 1cc4a55ae39d32347cef3f092271eeda5474b3a1
