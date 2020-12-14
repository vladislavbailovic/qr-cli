from argparse import ArgumentParser
import sys, re

import qrcode

parser = ArgumentParser()
parser.add_argument('input', metavar='<STRING>', help='Optional string to enter', nargs='?', type=str)
parser.add_argument('-o', '--output', help="Output QR code, use dash for stdout, dot to use simplified data as file name")

options = parser.parse_args()

data = options.input if options.input else "".join(sys.stdin.readlines())
img = qrcode.make(data)

output = sys.stdout.buffer
if options.output:
    outfile = options.output
    if options.output == ".":
        outfile = re.sub(
            r'-+',
            '-',
            re.sub(r'[^-_.a-zA-Z0-9]', '-', f"{ data[:64] }.png")
        )
    output = open(outfile, 'wb')

img.save(output, 'PNG')
