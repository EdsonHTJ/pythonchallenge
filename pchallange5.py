import pickle
import gzip
file=open("banner.p",'rb')
newdict=pickle.load(file)
file.close()
#print(newdict)
u=[j for i in newdict for j in i]
u=zip(*u)
ul=list(u)
#print(ul[0],ul[1])
for x in range(len(ul[0])):
	print(''.join(ul[0][x]*ul[1][x]),end='')