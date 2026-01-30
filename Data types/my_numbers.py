import math

# math.floor() # below
 
# math.ceil() # above 

# math.trunc() # closest number towards zero 

# a = 2 + 1j
# print(a*3)

print(0o20) # octal 
print(oct(16)) # oct() bin() hex()

int('64' , 8 ) # 64 to octal 
int('64' , 16 ) # 64 to hexa
int('01111' , 2 ) # to bin

import random 

random.random()
random.randint(1,10)
l1 = ["hello" , "bye"]

random.choice(l1)
random.shuffle(l1)

# this gives weird value 
# print(0.1 + 0.1 + 0.1 - 0.3)

from decimal import Decimal
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))


set1 = {1,2,3,4}
set & {1,3} # intersection