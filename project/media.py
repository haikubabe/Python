import fresh_tomatoes
import movie

avengers=movie.Movie("Avengers:Age of Ultron","When Tony Stark (Robert Downey Jr.) jump-starts a dormant peacekeeping program, things go terribly awry, forcing him, Thor (Chris Hemsworth), the Incredible Hulk (Mark Ruffalo) and the rest of the Avengers to reassemble.","http://www.hdwallpapers.in/walls/avengers_age_of_ultron_2015_movie-wide.jpg","https://www.youtube.com/watch?v=bMP-FLmiIM0")

avatar=movie.Movie("Avatar","A marine on an alien planet","http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=-9ceBgWV8io")

#print avengers.trailer

#avengers.show_trailer()

#print avatar.trailer

school_of_rock=movie.Movie("School of Rock","storyline","http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg","https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille=movie.Movie("Ratatouille","storyline","http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg","https://www.youtube.com/watch?v=c3sBBRxDAqk")


movies=[avengers,avatar,school_of_rock,ratatouille]
print movie.Movie.__doc__
print movie.Movie.__dict__
print movie.Movie.__name__
print movie.Movie.__bases__
print movie.Movie.__module__
#print movie.Movie.VALID_RATING
#fresh_tomatoes.open_movies_page(movies)



