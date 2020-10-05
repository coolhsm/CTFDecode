import sys
import getopt
from Base.scanBaseType import ScanBaseType

def printHelp():
    print("CTFDecode Power For HSM")
    print("CTFDecode help List")
    print("------")
    print("-b    --baseCheck    base Type Check")
    print("-b64    --base64    base64 Decode")
    print("-h    --help    help")

    print("------")

def main(argv):
    opts,args = getopt.getopt(argv,'-h-b:',['help','filename='])
    # print(opts)
    # print(args)
    for opt_name,opt_type in opts:
        if opt_name in ('-h','--help'):
           printHelp()
        if opt_name in ('-b'):
            TypeResult = ScanBaseType(opt_type)

            print(TypeResult.check())
            # print(type(opt_type))
    # print(argv)

if __name__ == "__main__":
   main(sys.argv[1:])

