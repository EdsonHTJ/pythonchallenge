f=open("file2.txt",'r').read()
alfa="abcdefghijklmnopqrstuvwxyz"
f=str(f)
#f="sadadhdlXXXxXXXsajdsadlfdfjajdkfl"
for x in range (len(f)-7):
	if f[x].isupper():
		if (f[x-1].islower() and f[x+1].isupper() and f[x+2].isupper() and f[x+3].islower() and f[x+4].isupper() and f[x+5].isupper() and f[x+6].isupper() and f[x+7].islower()):
			print(f[x-1:x+8])

#for x in range (len(f)-7):
#	if f[x].isupper():
#		letter=f[x]
#		if(f[x+1]==letter and f[x+2]==letter and f[x+3]==letter.lower() and f[x+4]==letter and f[x+5]==letter and f[x+6]==letter):
#			print(f[x:x+7])