import sys
import getopt
import scanBaseType
def printHelp():
    print("CTFDecode Power For HSM")
    print("CTFDecode help List")
    print("------")
    print("-b64    --base64    base64 Decode")
    print("-b64    --base64    base64 Decode")
    print("-b64    --base64    base64 Decode")

    print("------")

def main(argv):
    opts,args = getopt.getopt(argv,'-h-b:',['help','filename='])
    # print(opts)
    # print(args)
    for opt_name,opt_type in opts:
        if opt_name in ('-h','--help'):
           printHelp()

    # print(argv)

if __name__ == "__main__":
   main(sys.argv[1:])

