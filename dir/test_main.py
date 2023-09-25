from base.dir import lotto_file

arr = lotto_file.fn_lotto(5)
print(arr)

#from lotto_file import fn_lotto
from base.dir.lotto_file import *
arr = fn_lotto(3)
print(arr)
from base.dir.lotto_file import fn_lotto as l
arr2 = l(10)

