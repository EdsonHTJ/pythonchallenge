import requests
r =requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345')
print(r.text)
word = (r.text).split(' ')
while word[len(word)-1].isnumeric():
	r =requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+word[len(word)-1])
	print(r.text)
	word = (r.text).split(' ')

