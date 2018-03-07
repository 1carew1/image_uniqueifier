from os import walk
import sys
import hashlib

BUF_SIZE = 65536
DIRPATH = "/Users/colmcarew/IdeaProjects/cachingrest/images"
file_list = []

def populateFileList():
	for(directory, dirnames, filenames) in walk(DIRPATH):
		for filename in filenames:
			file_list.append(directory + "/" + filename)


populateFileList()
for s in file_list :
	md5 = hashlib.md5()
	with open(s, 'rb') as file :
		while(True):
			data = file.read(BUF_SIZE)
			if not data:
				break
			md5.update(data)
	print(s, " ", "MD5: {0}".format(md5.hexdigest()))
