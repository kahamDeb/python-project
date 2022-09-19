import string 
from string import *
import itertools 
from  itertools import product
value = ascii_letters+digits+punctuation
for i in range(1,64):
    for j in product(value,repeat=i):
        word = "".join(j)
        p = open("password.txt","a")
        p.write(word)
        p.write("\n")
