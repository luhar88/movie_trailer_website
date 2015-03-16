import webbrowser

class Movie(object):
    """Movie information"""
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """Initializes the Movie Info"""
        super(Movie, self).__init__()
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Opens the Movie Trailer i.e. trailer_youtube_url in a browser window"""
        webbrowser.open(self.trailer_youtube_url)