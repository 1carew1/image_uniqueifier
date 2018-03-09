from os import walk
import sys
import hashlib
import os
import sys

BUF_SIZE = 65536

class UniqueFile():
	def __init__(self, hash, location):
		self.hash = hash
		self.location = location
		self.duplicates = []


def populate_file_list(dirpath):
	file_list = []
	for(directory, dirnames, filenames) in walk(dirpath):
		for filename in filenames:
			file_list.append(directory + "/" + filename)
	return file_list


def calculate_file_hash(file_loc):
	md5 = hashlib.md5()
	with open(file_loc, 'rb') as file :
		while(True):
			data = file.read(BUF_SIZE)
			if not data:
				break
			md5.update(data)
	return "{0}".format(md5.hexdigest())

def obtain_unique_files(file_list) :
	unique_files = {}
	for s in file_list :
		theMd5 = calculate_file_hash(s)
		present_unique_file = unique_files.get(theMd5, None)
		if(present_unique_file == None):
			unique_file = UniqueFile(theMd5, s)
			unique_files[theMd5] = unique_file
		else :
			present_unique_file.duplicates.append(s)
	return list(unique_files.values())

def delete_files(unique_files):
	for unique_file in unique_files :
		for filepath in unique_file.duplicates :
			os.remove(filepath)
		unique_file.duplicates = []

if(__name__ == "__main__"):
	dirpath = sys.argv[1]
	if(os.path.exists(dirpath)):
		print("Obtaining Files")
		file_list = populate_file_list(dirpath)
		print("There are ", len(file_list), " files in total")
		unique_files = obtain_unique_files(file_list)
		number_of_duplicates = 0
		number_of_files_with_duplicates = 0
		for unique_file in unique_files :
			duplicates_for_this_file = len(unique_file.duplicates)
			if(duplicates_for_this_file > 0) :
				number_of_duplicates = number_of_duplicates + duplicates_for_this_file
				print(unique_file.location, " has ", duplicates_for_this_file, " duplicates. ", unique_file.duplicates)
				number_of_files_with_duplicates = number_of_files_with_duplicates + 1
		print("There are ", number_of_files_with_duplicates, " files that have duplicates")
		print("There are ", number_of_duplicates, " duplicates that can be deleted")
		if(number_of_duplicates > 0):
			user_input = str(input("Do you want to delete all of these duplicate files? (y/n): ")).lower()
			if(user_input == "y"):
				print("Deleting Files")
				delete_files(unique_files)
	else:
		print("Please enter a valid directory")