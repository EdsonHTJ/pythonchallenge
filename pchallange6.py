import zipfile
zp = zipfile.ZipFile("channel.zip")
path2 = '90052.txt'
r=zp.read(path2).decode("utf-8")
print(r)
i=zp.getinfo(path2).comment.decode("utf-8")
print(i)
word = (r).split(' ')
com=[]
com.append(i)
while word[len(word)-1].isnumeric():
	r=zp.read(path2).decode("utf-8")
	print(r)
	i=zp.getinfo(path2).comment.decode("utf-8")
	print(i)
	word = (r).split(' ')
	com.append(i)
	path2 = word[len(word)-1]+'.txt'
#print(com)
print(''.join(com))