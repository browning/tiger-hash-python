
def tiger_compress(str, r1, r2, r3):
    #setup
    a = r1
    b = r2
    c = r3
    
    x0 = str[0]
    x1 = str[1]
    x2 = str[2]
    x3 = str[3]
    x4 = str[4]
    x5 = str[5]
    x6 = str[6]
    x7 = str[7]

    # compress
    save_abc
    for i in range(0, 2):
        if i != 0:
            key_schedule
        if i == 0:
            tiger_pass(a,b,c,0)
        if i == 1:
            tiger_pass(a,b,c,1)
        if i == 2:
            tiger_pass(a,b,c,2)
        tmpa = a
        a = c
        c = b
        b = tmpa
    feed_forward

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
