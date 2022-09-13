import sys
import base64
import argparse

parser = argparse.ArgumentParser(description="A simple tool to encode base64 and base32",
        usage="%(prog)s --b64/--b32 cipher",
        epilog="Example %(prog)s --b64 QWRhcnNoIEFkZGVl")

parser.add_argument("-b64", "--base64",
                    help="decode base64 encoding",
                    metavar="base64",
                    dest="b64",
                    nargs="+")

parser.add_argument("-b32", "--base32",
                    help="decode base32 encoding",
                    metavar="base32",
                    dest="b32",
                    nargs="+")

parser.add_argument("-o", "--output",
                    help="saves output in file",
                    dest="out",
                    metavar="output")

parser.add_argument("-v",
                    help="version",
                    version="%(prog)s 1.0",
                    action="version")

args = parser.parse_args()

b64 = args.b64
b32 = args.b32
out = args.out

def banner():
    bann = """    
___.                          ________   _____  
\_ |__ _____    ______ ____  /  _____/  /  |  | 
 | __ \\__  \  /  ___// __ \/   __  \  /   |  |_
 | \_\ \/ __ \_\___ \\  ___/\  |__\  \/    ^   /
 |___  (____  /____  >\___  >\_____  /\____   | 
     \/     \/     \/     \/       \/      |__| 
    """
    print(bann)
    print("[*] Made By Adarsh Addee!")

def decode():
    if b64:
        for i in b64:
            res = (base64.b64decode(i)).decode()
            print(res)
            output(res)

    if b32:
        for i in b32:
            res = (base64.b32decode(i)).decode()
            print(res)
            output(res)

def output(code):
    if out:
        with open(f"{out}", "a") as f:
            f.write(code)
            f.write("\n")

if len(sys.argv) == 1:
    banner()
    parser.print_help(sys.stderr)
    sys.exit(1)

if __name__ == "__main__":
    decode()


