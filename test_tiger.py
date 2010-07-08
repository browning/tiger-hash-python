import unittest
import sys
import os
import tiger

class TigerTestCase(unittest.TestCase):
    
    def test_hash1(self):        
        hashval = tiger.hash("TESTING!")
        assert hashval == "lol", hashval + " != lol\n"

    def test_tiger_round(self):
        a = 13065445776871430898 
        b = 17855811585246249540
        c = 518233413090174763
        x = 12311797252403697916
        mul = 7
        tiger.tiger_round(a,b,c,x,mul)

        assert a == 4821272432160810520, "a failed: " + str(a) + " != 4821272432160810520\n"
        assert b == 17424479681440429243, "b failed: " + str(b) + " != 17424479681440429243\n"
        assert c == 12532788606137106391, "c failed: " + str(c) + " != 12532788606137106391\n" 

