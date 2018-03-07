from os import walk
import sys
import hashlib
import os

BUF_SIZE = 65536
DIRPATH = "/Users/colmcarew/IdeaProjects/cachingrest/images"

def populateFileList():
	file_list = []
	for(directory, dirnames, filenames) in walk(DIRPATH):
		for filename in filenames:
			file_list.append(directory + "/" + filename)
	return file_list


def obtainDuplicates(file_list) :
	unique_files = {}
	duplicate_files = []
	for s in file_list :
		md5 = hashlib.md5()
		with open(s, 'rb') as file :
			while(True):
				data = file.read(BUF_SIZE)
				if not data:
					break
				md5.update(data)
		theMd5 = "{0}".format(md5.hexdigest())
		if(unique_files.get(theMd5, "NONE") == "NONE"):
			unique_files[theMd5] = s
		else :
			duplicate_files.append(s)
	#for md5value, fileLocation in unique_files.items():
		#print(md5value, " ", fileLocation)
	return duplicate_files

def deleteFiles(duplicate_files):
	for filepath in duplicate_files :
		os.remove(filepath)


file_list = populateFileList()
redundant_files = obtainDuplicates(file_list)
deleteFiles(redundant_files)