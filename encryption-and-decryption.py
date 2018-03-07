import sys

#--------defined functions---------#
def encrypt(y):
	msg = [y]
	n = len(msg[0])
	#end="" means there is no line break after this print statement
	print("encrypted word is : ", end="")
	for i in range(0, n):
		x = ord(msg[0][i]) + i
		print(chr(x),end = "")
	print("\n")

def decrypt(y):
	msg = [y]
	n = len(msg[0])
	print("decrypted word is : ", end = "")
	for i in range(0, n):
		x = ord(msg[0][i]) - i
		print(chr(x), end = "")
	print("\n")
#-----------------------------------#

print ("---------------------------\n","Developed by %s" % ("Amaan Ahmad"), "\n encrypter and decrypter\n My profile : github.com/amaan-ahmad\n Program at : github.com/amaan-ahmad/cryptopython","\n---------------------------")
word = input(">>> ")
encrypt(word)
choice = input("wanna decrypt ? (Y / N): ")
if choice == 'Y':
	ch = input ("Enter word to be decrypted : ")
	decrypt(ch)
