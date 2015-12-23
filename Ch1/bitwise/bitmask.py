
class BitMask(int):
    """Derived from int so already has its parent __new__ and __init__.
    """

    def NOT(self):
        return BitMask(~self)

    def AND(self, bm):
        return BitMask(self & bm)

    def OR(self, bm):
        return BitMask(self | bm)

    def XOR(self, bm):
        return BitMask(self ^ bm)

    def shiftleft(self, places):
        return BitMask(self << places)

    def shiftright(self, places):
        return BitMask(self >> places)

    def bit(self, idx):
        mask = 1 << idx
        return BitMask(bool(self & mask))

    def setbit(self, idx):
        mask = 1 << idx
        return BitMask(self | mask)

    def zerobit(self, idx):
        mask = 1 << idx
        return BitMask(self ^ mask)

    def listbits(self, start=0, end=None):
        if end: end = end if end < 0 else end + 2
        return [int(bit) for bit in bin(self)[start+2:end]]
        # Discussed with Alan Gauld and the above is his solution.
        # It relies on array[:None] === array[:] which I fear 
        # may be implementation dependent and perhaps we shouldn't
        # depend on it.
        # A somewhat more verbose but perhaps more reliable solution:
        if end is None:
            return [int(bit) for bit in bin(self)[start+2:]]
        else:
            end = end if end < 0 else end + 2
            return [int(bit) for bit in bin(self)[start+2:end]]


def test():
    bm1 = BitMask()
    assert bm1 == 0
    assert (bm1.NOT() & 0xf) == 0b1111
    bm2 = BitMask(0b10101100)
    assert (bm2 & 0xf) == 0b1100
    assert bm2.AND(0xf) == 0b1100
    assert (bm2 & 0xff) == 0b10101100
    assert bm2.AND(0xff) == 0b10101100
    assert bm1.AND(bm2) == 0
    assert bm1.OR(bm2) == bm2

    bm4 = BitMask.listbits(0b11110000)
    assert bm4 == [1,1,1,1,0,0,0,0]

    bm_test = BitMask(0b11110000)
    assert bm_test.listbits(0) == bm4
    assert bm_test.listbits(0, -1) == bm4[:-1]
    assert bm_test.listbits(2, -2) == bm4[2:-2]
    assert bm_test.listbits(2, 6) == [1,1,0,0]
    assert bm_test.listbits(end=6) == [1,1,1,1,0,0]

if __name__ ==  "__main__":
    test()
