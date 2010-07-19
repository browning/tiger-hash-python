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
        ret_values = tiger.tiger_round(a,b,c,x,mul)

        assert ret_values["a"] == 4821272432160810520, \
            "a failed: " + str(ret_values["a"]) + " != 4821272432160810520\n"
        assert ret_values["c"] == 12532788606137106391, \
            "c failed: " + str(ret_values["c"]) + " != 12532788606137106391\n" 
        assert ret_values["b"] == 17424479681440429243, \
            "b failed: " + str(ret_values["b"]) + " != 17424479681440429243\n"

    def test_tiger_round2(self):
        a =  6280199717849618378
        b =  8343645101657805456
        c =  5997044206234503415

        x = 12062177936022666431
        mul = 9
        ret_values = tiger.tiger_round(a,b,c,x,mul)

        assert ret_values["a"] == 11604645957211426640, \
            "a failed: " + str(ret_values["a"]) + " != 11604645957211426640\n"
        assert ret_values["c"] == 17608143266212181064, \
            "c failed: " + str(ret_values["c"]) + " != 17608143266212181064\n" 
        assert ret_values["b"] == 3986339792283275959, \
            "b failed: " + str(ret_values["b"]) + " != 3986339792283275959\n"

    
    """
    Results from reference:
    A: 6280199717849618378
    B: 8343645101657805456
    C: 5997044206234503415
    mul: 9
    x0: 12062177936022666431
    x1: 11490956213547313652
    x2: 16829172008830410301
    x3: 11899344311637024046
    x4: 3757253942274655973
    x5: 17835857420906997132
    x6: 10787740079658512390
    x7: 17590610739856314589
    new A: 1509595445172618351
    new B: 206383248218352883
    new C: 2725617220977123037

    """
    def test_tiger_pass(self):
        a =  6280199717849618378
        b =  8343645101657805456
        c =  5997044206234503415
        mul = 9
        data = [12062177936022666431, 11490956213547313652, 16829172008830410301, \
            11899344311637024046,  3757253942274655973, 17835857420906997132, \
            10787740079658512390,  17590610739856314589]

        ret_values = tiger.tiger_pass(a,b,c,mul, data)

        assert ret_values["a"] == 1509595445172618351, \
            "a failed, " + str(ret_values["a"]) + " != 1509595445172618351"
        assert ret_values["b"] == 206383248218352883, \
            "b failed, " + str(ret_values["b"]) + " != 206383248218352883"
        assert ret_values["c"] ==  2725617220977123037, \
            "c failed, " + str(ret_values["c"]) + " != 2725617220977123037"





      
 
