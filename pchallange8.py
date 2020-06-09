import ast
import bz2,re

file = open('file3.txt','r').read()
#file=file[file.find('BZh91AY&SYA'):file.find("4'")+1]
file2 = file[file.find('pw'):]
a = re.search(r"\'(.*?)\'",''.join(file)).group()
b = re.search(r"\'(.*?)\'",''.join(file2)).group()
a = eval("b%s" % a)
b = eval("b%s" % b)

#a=c_char_p('x69'.encode('ascii'))
print(bz2.decompress(a))
print(bz2.decompress(b))
