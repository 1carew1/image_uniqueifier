from os import walk

dirpath = "/Users/colmcarew/IdeaProjects/cachingrest/images"
file_list = []

def populateFileList():
	for(directory, dirnames, filenames) in walk(dirpath):
		for filename in filenames:
			file_list.append(directory + "/" + filename)


populateFileList()
for s in file_list :
	print(s)
