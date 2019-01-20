#!/usr/bin/env python3.6

import argparse
import os

count = int(os.environ["TESTING"])
parser = argparse.ArgumentParser(description="Just tellin you like it iees")
parser.add_argument('filename', help='put in the file name here')
parser.add_argument('after')

print(f"this is rotation {count}")
thisparse = parser.parse_args()
print(f"{thisparse.filename} is what I said before {thisparse.after}")