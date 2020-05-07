from helper import read_variant, little_endian_to_int, int_to_little_endian


class Script:
    def __init__(self, cmds=None):
        """[summary]

        Parameters
        ----------
        cmds : [type], optional
            [description], by default None
            each element is opcode or element
        """
        if cmds is None:
            self.cmds = []
        else:
            self.cmds = cmds

    @classmethod
    def parse(cls, s):
        length = read_variant(s)
        cmds = []
        count = 0
        while count < length:
            # TODO:check how s.read works and type of s
            current = s.read(1)
            count += 1
            current_byte = current[0]
            if current_byte >= 1 and current_byte <= 75:
                n = current_byte
                cmds.append(s.read(n))
            elif current_byte == 76:
                data_length = little_endian_to_int(s.read(1))
                cmds.append(s.read(data_length))
                count += data_length+1
            elif current_byte == 77:
                data_length = little_endian_to_int(s.read(2))
                cmds.append(s.read(data_length))
                count += data_length+2

            else:
                op_code = current_byte
                cmds.append(op_code)
        if count != length:
            raise SyntaxError("parsing script failed")
        return cls(cmds)

    def raw_serialize(self):
        result = b""
        for cmd in self.cmds:
            if type(cmd) == int:
                result += int_to_little_endian(cmd, 1)

    def evaluate(self, z):
        """[summary]

        Parameters
        ----------
        z : [type]
            message
        """
        # hard-copy
        cmds = self.cmds[:]
        stack = []
        altstack = []
        while len(cmds) > 0:
            cmd = cmds.pop(0)

    def __add__(self, other):
        return self.__class__(self.cmds+other.cmds)
