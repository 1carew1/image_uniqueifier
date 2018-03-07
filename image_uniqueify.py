from os import walk
import sys
import hashlib
import os
import sys

BUF_SIZE = 65536

def populateFileList(dirpath):
	file_list = []
	for(directory, dirnames, filenames) in walk(dirpath):
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


if(__name__ == "__main__"):
	dirpath = sys.argv[1]
	if(os.path.exists(dirpath)):
		print("Obtaining Files")
		file_list = populateFileList(dirpath)
		print("There are ", len(file_list), " files in total")
		redundant_files = obtainDuplicates(file_list)
		number_of_duplicates = len(redundant_files)
		print("There are ", number_of_duplicates, " duplicated files")
		if(number_of_duplicates > 0):
			user_input = str(input("Do you want to delete these duplicate files? (y/n): ")).lower()
			if(user_input == "y"):
				print("Deleting Files")
				deleteFiles(redundant_files)
	else:
		print("Please enter a valid directory")