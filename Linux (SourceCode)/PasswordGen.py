import random
import hashlib
import time

Chars = []

with open("./keychain.dll", 'w') as keychain:
	for i in range(10):
		keychain.write(f"{str(i)}\n")
	SpecialChars = ["\\", "|", "€", "đ", "[", "]", "ł", "Ł", "#", "&", "@", "{", "}", ",", ".", "-", "?", ":", "_", "$", "ß", ")", "(", "'", "\""]
	Alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	for i in range(len(Alphabet)):
		keychain.write(f"{Alphabet[i]}\n")
	for i in range(len(Alphabet)):
		keychain.write(f"{Alphabet[i].lower()}\n")
	for i in range(len(SpecialChars)):
		keychain.write(f"{SpecialChars[i]}\n")
	keychain.close()

with open("./keychain.dll", 'r') as keychain:
	for char in keychain.readlines():
		Chars.append(char.strip())

lenght = input("Enter required length of the password.\n> ")
build = ""
for i in range(int(lenght)):
	build = build + str(random.choice(Chars))
hsh = input("Would you like to hash? (Y/N - default is N)\n> ")
if hsh.lower() == "y":
	build = hashlib.md5(bytes(build, "utf-8")).digest()
	build = hashlib.sha512(build).digest()
	build = hashlib.sha256(build).digest()
print(f"--- Generated Password ---\n{build}")
time.sleep(5)