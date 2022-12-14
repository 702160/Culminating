import time
import sys

#Delays each printed character to give off a typing effect
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

# This is a faster version of the first text delay
def delay_print_fast(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.0000000001)

#Even faster
def delay_print_faster(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0)