import requests
import png,re
(w,h,i,d)=png.Reader('oxygen.png').read()
#print(list(i))
it = list(i)
#print(len(list(i)[0]),h,w)
r=[]
for x in range(0,len(it[0]),4*7):
	r.append(chr(it[int(h/2)][x]))
#print(r)
print(''.join(r))
#r2=r[r.find('is'):]
#print(''.join(r2))
