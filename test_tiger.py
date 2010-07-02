import unittest
import sys
import os
import tiger

class TigerTestCase(unittest.TestCase):
    
    def test_firstpass_compress(self):
        
        r1 = 0x0123456789ABCDEF
        r2 = 0xFEDCBA9876543210
        r3 = 0xF096A5B4C3B2E187
 
        tiger.compress("TESTING!", r1, r2, r3)
        assert r1 == 0xfff, r1 + " != " + str(0xfff) + "\n"
        assert r2 == 0xddd, r2 + " != " + str(0xddd) + "\n"
        assert r3 == 0xaaa, r3 + " != " + str(0xaaa) + "\n"

