import urllib

def read_text():
	file_name=open("/home/sreemoyee/text_doc.txt")
	content=file_name.read()
	print("The content of the file is "+content)
	file_name.close()
	check_profanity(content)


def check_profanity(text):
	window=urllib.urlopen("http://isithackday.com/arrpi.php?text="+text)
	location=window.read()
	print("The file now is "+location)
	window.close()

read_text()
