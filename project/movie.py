import webbrowser

class Movie():

	"""This file provides a list of movies & show its title,its storyline,its poster image & its trailer"""
	
	VALID_RATING=["G","PG","PG-13","R"]	#class variables
	
	def __init__(self,title,storyline,poster_image,youtube_trailer):
		self.title=title
		self.storyline=storyline
		self.poster_image_url=poster_image
		self.trailer_youtube_url=youtube_trailer

	def show_trailer(self):
		webbrowser.open(self.trailer)
