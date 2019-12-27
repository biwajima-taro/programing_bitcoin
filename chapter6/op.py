from typing import List
from chapter1.helper import hash256,hash160

def op_dup(stack: List) -> bool:
    """""1qｑ２"
    if len(stack) < 1:
        return False
    stack.append(stack[-1])
    return True

def op_hash256(stack:List)->bool:
    """apply hash256 to the top element of the stack"""
    if len(stack)<1:
        return False
    element=stack.pop()
    stack.append(hash256(element))
    return True

def op_hash160(stack:List)->bool:
    if len(stack)<1:
        return False
    element=stack.pop()
    stack.append(hash160(element))
    return True

OP_CODE_FUNCTIONS = {
    118:
    op_dup
}
