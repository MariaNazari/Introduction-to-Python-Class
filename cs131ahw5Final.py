"""
The purpose of this program is to print out its own command line arguments in
reverse order from last to first. 

Directions: enter file name following by inputs
    Example: filename.py Input1 Input2 ... Input n 
"""

import sys

# Get argument list:
args = list(sys.argv)

#Remove file name
args.pop(0)

# Reverse arguments
args_reversed = args[::-1]
#args_reversed = list(reversed(sys.argv))

#Print out 
print("Command Line Inputs Oringal:", ' '.join(args))
print("Command Line Inputs Reversed:", ' '.join(args_reversed))

