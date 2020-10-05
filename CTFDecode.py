#! /usr/bin/env python3
import sys
import getopt
from lib.Base import *
def printHelp():
    print(" Power For HSM")
    print("NAME: \n   CTFDecode\t A powerful decoding tool\tPower By HSM\n\n")
    print("DESCRIPTION:\t由JJUSEC团队HSM编写的用于CTF比赛的解码工具\n")
    print("\nOPTIONS:\n")
    print("\t-b\t--baseCheck    查询可能使用过的Base编码类型")
    print("\t--basedecode\tbase家族解密")
    print("\t-h\t--help\thelp")
def main(argv):
    opts,args = getopt.getopt(argv,'-h-b:',['help','filename=','basedecode='])
    for opt_name,opt_type in opts:
        if opt_name in ('-h','--help'):
           printHelp()
           exit()
        if opt_name in ('-b'):
            TypeResult = ScanBaseType(opt_type)
            print(TypeResult.check())
            # print(type(opt_type))
            exit()
        if opt_name in ('--basedecode'):
            # print(opt_type)
            Result = DecodeBase(opt_type)
            Result.Decode()
            # print(opt_type)
            exit()
        printHelp()
        exit()
    # print(argv)
if __name__ == "__main__":
   main(sys.argv[1:])

