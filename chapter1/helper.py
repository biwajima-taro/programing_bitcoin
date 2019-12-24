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