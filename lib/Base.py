import re
class ScanBaseType:
    def __init__(self,BaseString):
        self.BaseString  =BaseString
        # print(self.BaseEncodeString)
    # def detail(self):
    #     print(self.BaseString)
    def check(self):
        BaseType = []
        BaseTypeList = ['base16','base32','base36','base58','base62','base64','base91','base92']
        """
        base64:
        Base16编码使用16个ASCII可打印字符（数字0-9
        Base16先获取输入字符串每个字节的二进制值（不足8比特在高位补0），然后将其串联进来再按照4比特一组进行切分，将每组二进制数分别转换成十进制
        8比特数据按照4比特切分刚好是两组， ** 所以Base16不可能用到填充符号“=”
        """

        test1 = re.findall(r'[a-z]|[G-Z]',self.BaseString)   #排除base16
        test2 = re.findall(r'[0-1]|[G-Za-z]|\=|\/|\+',self.BaseString) #排除base32
        test3 = re.findall(r'[a-z]', self.BaseString) # 匹配小写
        test4 = re.findall(r'[A-Z]', self.BaseString)  # 匹配大写
        test5 = re.findall(r'0|o|l|\/|\+', self.BaseString)  # 匹配0 o l  base58
        test6 = re.findall(r'\=|\/|\+', self.BaseString)  # base62
        test7 = re.findall(r'[A-Z]|[a-z]|[0-9]|\#|\$|\%|\&\(|\)|\*|\+|\,|\.|\/|\:|\;|\<|\=|\>|\?|\@|\[|\]|\^|\_|\'|\{|\}|\||\~|\"', self.BaseString)  # base91
        # print(test1)
        if test1 == []:
            BaseType.append('base16')
        if test2 == []:
            BaseType.append('base32')
        if (test3 == [] and test4 != []) or (test3 != [] and test4 == []):
            BaseType.append('base36')
        if test5 == []:
            BaseType.append('base58')
        if test6 == []:
            BaseType.append('base62')
        BaseType.append('base64')
        BaseType.append('base91')
        BaseType.append('base92')
        return BaseType
# string = "A"
# print(string)
# obj1  = ScanBaseType(string)
# a = obj1.check()
# print(a)
# https://blog.csdn.net/MikeCoke/article/details/105512385

class BaseDecode:
    def __init__(self,):
        pass
