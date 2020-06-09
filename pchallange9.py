#from PIL import Image,ImageDraw
import matplotlib.pyplot as plt


file = open('file4.txt','r').read()
file = file[file.find('first:'):]
first = file[7:file.find('second:')-2]
second = file[file.find('second:')+8:]
#print(first)
#print(second)
#print(''.isnumeric())
first=first.split('\n')
first_=[]
second=second.split('\n')
second_=[]
second=second[:len(second)-3]
#print(len(first))
for x in range(len(first)):
    first[x]=first[x].split(',')
    if not first[x][len(first[x])-1].isnumeric():
        first[x]=first[x][:len(first[x])-3]

    for y in range(len(first[x])):
        first[x][y]=int(first[x][y])

    first_ += first[x]
for x in range(len(second)):
    second[x]=second[x].split(',')
    if not second[x][len(second[x])-1].isnumeric():
        second[x]=second[x][:len(second[x])-3]

    for y in range(len(second[x])):
        second[x][y]=int(second[x][y])

    second_ += second[x]
    #second[x].remove('')
    #second[x].remove('\n')
    #second[x].remove('')

print(len(first_))
print('')
print(len(second_))

#im = Image.new('RGB',(100,100))
#draw = ImageDraw.Draw(im)
first_x=[]
first_y=[]
second_x=[]
second_y=[]
for i in range(len(first_)):
    if i%2==0:
        first_x.append(first_[i])
    else:
        first_y.append(first_[i])

for i in range(len(second_)):
    if i%2==0:
        second_x.append(second_[i])
    else:
        second_y.append(second_[i])
plt.plot(first_x,first_y)
plt.plot(second_x,second_y)
plt.show()
