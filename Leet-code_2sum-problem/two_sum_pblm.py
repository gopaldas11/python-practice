#learning
from array import *
vals = array('i', [45, 34, 65, 44, 24])
newarr = array(vals.typecode, (a * a for a in vals))
for i in newarr:
    print(i)