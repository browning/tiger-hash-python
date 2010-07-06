t1 = []
t2 = []
t3 = []
t4 = []

def tiger_round(a,b,c,x,mul):
    c ^= ord(x)
    a -= t1[((c) >> (0*8))&0xFF] ^ t2[((c) >> ( 2*8)) & 0xFF] ^ t3[((c) >> (4*8))&0xFF] ^ t4[((c) >> ( 6*8)) & 0xFF]
    b += t4[((c) >> (1*8))&0xFF] ^ t3[((c) >> ( 3*8)) & 0xFF] ^ t2[((c) >> (5*8))&0xFF] ^ t1[((c) >> ( 7*8)) & 0xFF] 
    b *= mul

def tiger_pass(a,b,c,mul, str):
    tiger_round(a,b,c, str[0], mul)
    tiger_round(b,c,a,str[1],mul)
    tiger_round(c,a,b, str[2], mul)
    tiger_round(a,b,c,str[3],mul)
    tiger_round(b,c,a,str[4],mul)
    tiger_round(c,a,b,str[5],mul)
    tiger_round(a,b,c,str[6],mul)
    tiger_round(b,c,a,str[7],mul)

def tiger_compress(str, r1, r2, r3):
    #setup
    a = r1
    b = r2
    c = r3
    
    # compress
    aa = a
    bb = b
    cc = c
    for i in range(0, 2):
        if i != 0:
            key_schedule
        if i == 0:
            tiger_pass(a,b,c,5, str)
        if i == 1:
            tiger_pass(a,b,c,7, str)
        if i == 2:
            tiger_pass(a,b,c,9, str)
        tmpa = a
        a = c
        c = b
        b = tmpa
    a ^= aa
    b -= bb
    c += cc

    # map values out
    r1 = a
    r2 = b
    r3 = c

str = "HACK THE PLANET. HACK THE WORLD"

result0 = 0x0123456789ABCDEF
result1 = 0xFEDCBA9876543210
result2 = 0xF096A5B4C3B2E187

for i in range(0, len(str) / 8 ):
    tiger_compress( str[i*8:i*8+8], result0, result1, result2 ) 
