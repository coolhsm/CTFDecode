#! usr/bin/env python3
import sys
import getopt
from Base.scanBaseType import ScanBaseType
from Base.baseDecode import BaseDecode
def printHelp():
    print(" Power For HSM")
    print("NAME \n   CTFDecode\t A powerful decoding tool\tFrom jjusec HSM\n\n")
    print("DESCRIPTION\t由JJUSEC团队HSM编写的用于CTF比赛的解码工具\n")
    print("\nOPTIONS\n")
    print("\t-b    --baseCheck    base Type Check")
    print("\t--basedecode base家族解密")
    print("\t-h    --help    help")
    # print("------")

def main(argv):
    opts,args = getopt.getopt(argv,'-h-b:',['help','filename=','basedecode='])
    # print(opts)
    # print(args)
    for opt_name,opt_type in opts:
        if opt_name in ('-h','--help'):
           printHelp()
        if opt_name in ('-b'):
            TypeResult = ScanBaseType(opt_type)

            print(TypeResult.check())
            # print(type(opt_type))
        if opt_name in ('--basedecode'):
            print(opt_type)
    # print(argv)

if __name__ == "__main__":
   main(sys.argv[1:])

