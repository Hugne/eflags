#!/usr/bin/env python

# "THE BEER-WARE LICENSE" (Revision 42):
# <erik.hugne@gmail.com> wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return Erik Hugne

import sys

#X86 EFLAGS register
EFLAGS = {
'CF (Carry flag)':              lambda x: x&0x1,
'1 (Reserved)':                 lambda x: x&0x2,
'PF (Parity flag)':             lambda x: x&0x4,
'3 (Reserved)':                 lambda x: x&0x8,
'AF (Adjust flag)':             lambda x: x&0x10,
'5 (Reserved)':                 lambda x: x&0x20,
'ZF (Zero flag)':               lambda x: x&0x40,
'SF (Sign flag)':               lambda x: x&0x80,
'TF (Trap flag)':               lambda x: x&0x100,
'IF (Interrupt enable flag)':   lambda x: x&0x200,
'SF (Direction flag)':          lambda x: x&0x400,
'OF (Overflow flag)':           lambda x: x&0x800,
'IOPL (I/O privilege level)':   lambda x: x&0x3000,
'NT (Nested task flag)':        lambda x: x&0x4000,
'15 (Reserved)':                lambda x: x&0x8000,
'RF (Resume flag)':             lambda x: x&0x10000,
'VM (Virtual 8086 mode flag)':  lambda x: x&0x20000,
'AC (Alignment check)':         lambda x: x&0x40000,
'VIF (Virtual interrupt flag)': lambda x: x&0x80000,
'VIP (Virtual interrupt pending)': lambda x: x&0x100000,
'ID (Able to use CPUID instruction)': lambda x: x&0x200000,
'22-63 (Reserved)':             lambda x: x&0xFFFFFFFFFFC00000,
}

if (len(sys.argv) != 2):
    print 'Usage:', str(sys.argv[0]), 'EFLAGS (in hex)'
    sys.exit(-1)
code = int(sys.argv[1], 16)
print 'The following flags are set:'
for flag in EFLAGS:
    bits = EFLAGS[flag](code)
    if (bits):
        print flag, '[',bits,']'

