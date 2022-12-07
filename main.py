from suffixtree import *
import string
import random

# initializing size of string
N = 100000

# using random.choices()
# generating random strings
#input = ''.join(random.choices(string.ascii_uppercase +string.digits, k=N))

# print result#
#print("The generated random string : " + str(res))


input="abaababaabaababaababa$"

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
suffix_set=set()
for i in range(len(input)):
    suffix_set.add(input[i:len(input)])
print(suffix_set)
print(len(suffix_set))



suffixtree=Suffixtree(input)
suffixtree.build_suffixtree()
suffixlist=suffixtree.print_dfs()
print(len(suffixlist))
if (set(suffixlist)==suffix_set):
    print("test ok!")



