# Explanation
 - B = g ^ b % p
 - g = B ^ b % p  
 - since b < q < p, then b % p == b 
 - Therefore, g = B ^ b == b = B ^ g
 - key = A ^ b


# Flag
crypto{b3_c4r3ful_w1th_y0ur_n0tati0n}