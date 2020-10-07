class Convert:
    def __init__(self,convertStr):
        self.convertStr = convertStr
    def strToHex(self):  #将字符串转为hex
        s = self.convertStr
        HexStr = ''
        for i in s:
            c = ord(i)
            h = hex(c)
            HexStr += h[2:]
        return HexStr
