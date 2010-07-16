from sboxes import t1, t2, t3, t4

def tiger_round(a,b,c,x,mul):
    c ^= x
    a -= t1[((c) >> (0*8))&0xFF] ^ t2[((c) >> ( 2*8)) & 0xFF] ^ t3[((c) >> (4*8))&0xFF] ^ t4[((c) >> ( 6*8)) & 0xFF]
    b += t4[((c) >> (1*8))&0xFF] ^ t3[((c) >> ( 3*8)) & 0xFF] ^ t2[((c) >> (5*8))&0xFF] ^ t1[((c) >> ( 7*8)) & 0xFF] 
    b *= mul
    b &= 0xffffffffffffffff
    return {"a": a, "b":b, "c": c}

def tiger_pass(a,b,c,mul, str):
    values = tiger_round(a,b,c, str[0], mul)
    values = tiger_round(values["b"], values["c"], values["a"],str[1],mul)
    values = tiger_round(values["c"], values["a"], values["b"], str[2], mul)
    values = tiger_round(values["a"], values["b"], values["c"],str[3],mul)
    values = tiger_round(values["b"], values["c"], values["a"],str[4],mul)
    values = tiger_round(values["c"], values["a"], values["b"],str[5],mul)
    values = tiger_round(values["a"], values["b"], values["c"],str[6],mul)
    values = tiger_round(values["b"], values["c"], values["a"],str[7],mul)
    return values

def tiger_compress(str, r1, r2, r3):
    #setup
    a = r1
    b = r2
    c = r3
    
    x = []

    for i in range(0,8):
        x.append( ord(str[i]) )

    # compress
    aa = a
    bb = b
    cc = c
    for i in range(0, 2):
        if i != 0:
            x[0] -= x[7] ^  0xA5A5A5A5A5A5A5A5
            x[1] ^= x[0]
            x[2] += x[1]
            x[3] -= x[2] ^ ((~x[1]) << 19)
            x[4] ^= x[3]
            x[5] += x[4]
            x[6] -= x[5] ^ ((~x[4]) >> 23)
            x[7] ^= x[6]
            x[0] += x[7]
            x[1] -= x[0] ^ ((~x[7])<<19)
            x[2] ^= x[1]
            x[3] += x[2] 
            x[4] -= x[3] ^ ((~x[2])>>23)
            x[5] ^= x[4] 
            x[6] += x[5] 
            x[7] -= x[6] ^ 0x0123456789ABCDEF

        if i == 0:
            tiger_pass(a,b,c,5, x)
        if i == 1:
            tiger_pass(a,b,c,7, x)
        if i == 2:
            tiger_pass(a,b,c,9, x)
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

def hash(str):
    result0 = 0x0123456789ABCDEF
    result1 = 0xFEDCBA9876543210
    result2 = 0xF096A5B4C3B2E187

    for i in range(0, len(str) / 8 ):
        tiger_compress( str[i*8:i*8+8], result0, result1, result2 ) 
