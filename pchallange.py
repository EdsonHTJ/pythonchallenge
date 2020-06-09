

def change(St):
	alfa="abcdefghijklmnopqrstuvwxyz"
	if St in alfa:
		return alfa[(alfa.find(St)+2)%(len(alfa))]
	else:
		return St
	#if St=='m':
	#	return 'k'
	#elif St=='q':
	#	return 'o'
	#elif St=='g':
	#	return 'e'
	#else:
	#	return St

a="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
b="map"

result = map(change,a)
print(''.join(result))



