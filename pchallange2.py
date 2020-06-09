f=open("file.txt",'r').read()
alfa="abcdefghijklmnopqrstuvwxyz"
f=str(f)
for x in f:
	if x not in alfa:
		f=f.replace(x,'')

print(f)