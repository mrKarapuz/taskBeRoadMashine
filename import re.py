truestr = 'o..ooo.o'
falsestr = 'lsdfjs.o'

import re

def special_match(strg, search=re.compile(r'[^o.]').search):
    return not bool(search(strg))

print(not bool(re.compile(r'[^o.]').search(falsestr)))
