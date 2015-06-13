import time
import webbrowser

def break_time():

	print("The program started on "+time.ctime())
	wait=0
	while(wait<3):
		webbrowser.open('https://www.youtube.com/watch?v=_WOwRVTKJUw')
		time.sleep(2)
		wait=wait+1

break_time()
