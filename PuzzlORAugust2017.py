
import random
from collections import Counter

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + \
        'abcdefghijklmnopqrstuvwxyz' + \
        '0123456789' + \
        ':.;,?!@#$%&()+=-*/_<> []{}`~^"\'\\'

def main():
	message = 'DKFFQHXAQBUTKTKUGHJNMDHPAQBDUCKO' + " " + \
	'TUOEKGMDKOQGKVHMDAQBTPBSKTHQTUJU' + " " + \
	'FAMHOPPEHFFPHVUJMKGMQMDUJEAQBXQTT' + " " + \
	'KUGHJNMDKSBYYFQTXQTMDKPKSUPMMKJA' + " " + \
	'KUTPUJGFKMAQBEJQVMDUMMDHPVHFFRKM' +  " " + \
	'DKFUPMSBYYFKMDHPDUPRKKJUVQJGKTXBF' +  " " + \
	'QSSQTMBJHMAXQTIKMQOQJMTHRBMKMQMD' + " " + \
	'KHJXQTIPOQIIBJHMAUJGIKKMIUJAJKVSKQS' + " " + \
	'FKRBMHMPMHIKMQOFQPKMDHPODUSMKTUJ' + " " + \
	'GIQCKQJMQJKVQSSQTMBJHMHKPMDUJEAQB'
	
	#frequency analysis
	#print(Counter(message))
	collection_info = {"A":"u",
	"B":" ",
	"C":" ",
	"D":"h",
	"E":" ",
	"F":"l",
	"G":" ",
	"H":"i",
	"I":" ",
	"J":"n",
	"K":"e",
	"L":" ",
	"M":"t",
	"N":" ",
	"O":" ",
	"P":" ",
	"Q":"o",
	"R":" ",
	"S":"p",
	"T":"r",
	"U":"a",
	"V":" ",
	"W":" ",
	"X":" ",
	"Y":"z",
	"Z":" "

	}

	newmessage = ""
	info = ""
	for i in range(0, len(message)-1):
		info = message[i]
		if info == " ":
			newmessage+=info
		else:
			newmessage += collection_info[info]
	print(newmessage)

if __name__ == "__main__":
	main()