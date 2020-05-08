from typing import List, Any
from hashlib import hash256
from helper import hash160
OP_CODE_FUNCTIOINS = {118: op_dup,
                      170: op_hash256}
OP_CODE_NAMES = {118: "op_dup"}


def op_dup(stack: List[Any]) -> bool:
    """
    duplicate the top element of  the stack
    Parameters
    ----------
    stack : List[Any]
        [description]

    Returns
    -------
    bool
        [description]
    """
    if len(stack) < 1:
        return False
    stack.append(stack[-1])
    return True


def op_hash256(stack: List[Any]) -> bool:
    """
    consume the top of the stack  and appned its hash256 to the stack

    Parameters
    ----------
    stack : List
        [description]

    Returns
    -------
    bool
        [description]
    """
    if len(stack) < 1:
        return False
    element = stack.pop()
    stack.append(hash256(element))
    return True


def op_hash160(stack: List[Any]) -> bool:
    if len(stack) < 1:
        return False
    element = stack.pop()
    stack.append(hash160(element))
    return True


def encode_num(num: int) -> bytes:
    if num == 0:
        return b""
    abs_num = abs(num)
    negative = num < 0
    #bytearray is immutable
    result = bytearray()
    while abs_num:
        result.append(abs_num & 0xff)
        abs_num >>= 8
    # check whetherthe last element's first byte is 1
    if result[-1] & 0x80:
        if negative:
            result.append(0x80)
        else:
            result.append(0)

    elif negative:
        result[-1] |= 0x80
    return bytes(result)


def decode_num(element: bytes) -> int:
    if element == b"":
        return 0
    # sorted to make the biggest digit come first
    big_endian = element[::-1]
    if big_endian[0] & 0x80:
        negative = True
        #if first byte is 1 then extract the rest 7bits
        result = big_endian[0] & 0x7f
    else:
        negative = False
        result = big_endian[0]
    for c in big_endian[1:]:
        result <<= 8
        result += c
    if negative:
        return -result
    else:
        return result


def op_checksig(stack:List[Any]):
        # take off the last byte of the signature as that's the hash_type
    
    
    return 
