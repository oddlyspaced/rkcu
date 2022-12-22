import argparse
# Python based Command Line wrapper for managing color modes on Royal Kludge RK 61 Keyboard
# author: Hardik Srivastava [oddlyspaced]

# sample usage
# rkcu --speed 4 --brightness 5 --rainbow --sleep never --animation neon_stream --red 128 --green 128 --blue 128

parser = argparse.ArgumentParser(
    prog = 'RK61 Color Utility - Linux',
    description = 'Linux Utility to manage LED\'s on the Royal Kludge RK61 Keyboard.'
)

parser.add_argument('--speed', '-sp')
parser.add_argument('--brightness', '-br')
parser.add_argument('--sleep', '-sl')
parser.add_argument('--animation', '-an')

parser.add_argument('--rainbow', '-rb', action='store_true')

parser.add_argument('--red', '-r')
parser.add_argument('--green', '-g')
parser.add_argument('--blue', '-b')

args = parser.parse_args()

print(args)