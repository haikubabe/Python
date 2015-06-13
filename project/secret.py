import os

def rename_files():
	# get all the filenames from a directory
	file_names=os.listdir(r"/home/sreemoyee/alphabet/alphabet")
	directory=os.getcwd()
	print("Current working directory is " +directory)
	print file_names
	os.chdir("/home/sreemoyee/alphabet/alphabet")
	#rename those filenames
	for file in file_names:
		os.rename(file,file.translate(None,"0123456789"))
		print("Old File "+file)
		print("New File "+file.translate(None,"0123456789"))
	os.chdir(directory)

rename_files()
