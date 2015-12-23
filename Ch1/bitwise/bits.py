

def NOT(value):
    return ~value

def AND(value1, value2):
    return value1 & value2

def OR(value1, value2):
    return value1 | value2

def XOR(value1, value2):
    return value1 ^ value2

def shiftleft(value, places):
    return value << places

def shiftright(value, places):
    return value >> places

def bit(value, idx):
    mask = 1 << idx
    return bool(value & mask)

def setbit(value, idx):
    mask = 1 << idx
    return value | mask

def zerobit(value, idx):
    mask = 1 << idx
    return value ^ mask

def listbits(value):
    return [int(bit) for bit in bin(value)[2:]]
