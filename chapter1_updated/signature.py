

class Signature:
    def __init__(self, r: int, s: int):
        self.r = r
        self.s = s

    def der(self) -> bytes:
        """
        serialize itself for transaction

        Returns
        -------
        bytes
            [description]
        """
        rbin = self.__serialize(self.r)
        sbin = self.__serialize(self.s)
        result = rbin+sbin
        result += bytes([0x30, len(result)])+result
        return result

    def __serialize(self, num: int) -> bytes:
        """
        helper funciton for der method

        Parameters
        ----------
        num : int
            [description]

        Returns
        -------
        bytes
            [description]
        """
        bin_ = num.to_bytes(32, byteorder="big")
        bin_ = bin_.lstrip(b"\x00")
        # if rbin has a high bit ad\x00
        if bin_[0] & 0x80:
            bin_ = b"\x00"+bin_
        # 0x02+length(r)+rbin
        bin_ = bytes([2, len(bin_)])+bin_
        return bin_

    def __repr__(self):
        return "{}({:x},{:x})".format(self.__class__.__name__, self.r, self.s)


if __name__ == "__main__":
    print(9)

