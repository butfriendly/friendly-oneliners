#!/usr/bin/env python
"""The base64 file encoder helps you to encode binary files at the 
command-line.

As defined by RFC 2397, data URIs are designed to embed small data items 
as "immediate" data, as if they were referenced externally. Using inline 
images saves HTTP requests over externally referenced objects.

Usage:
  base64encode.py <filename>
  base64encode.py (-h | --help)
  base64encode.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.

"""
from docopt import docopt

import sys
import base64

if __name__ == "__main__":
	args = docopt(__doc__, version='1.0.0')

	filename = args['<filename>']
	with open(filename, "rb") as image_file:
		encoded_string = base64.b64encode(image_file.read())

	print encoded_string
	sys.exit(0)