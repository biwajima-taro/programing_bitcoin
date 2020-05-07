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



