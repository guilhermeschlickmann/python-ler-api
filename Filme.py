class Filme:
    def __init__(self):
        self.__adult = None
        self.__backdrop_path = None
        self.__genre_ids = None
        self.__original_language = None
        self.__original_title = None
        self.__overview = None
        self.__popularity = None
        self.__poster_path = None
        self.__release_date = None
        self.__title = None
        self.__video = None
        self.__vote_average = None
        self.__vote_count = None

    @property
    def adult(self):
        return self.__adult

    @adult.setter
    def adult(self,valor):
        self._adult = valor

    @property
    def backdrop_path(self):
        return self.__backdrop_path

    @backdrop_path.setter
    def backdrop_path(self,backdrop_path):
        self.__backdrop_path = backdrop_path

    @property
    def genre_ids(self):
        return self.__genre_ids

    @genre_ids.setter
    def genre_ids (self, genre_ids):
        self.__genre_ids = genre_ids
    
    @property
    def original_language(self):
        return self.__original_language

    @original_language.setter
    def original_language(self,original_language):
        self.__original_language = original_language
    
    @property
    def original_title (self):
        return self.__original_title

    @original_title.setter
    def original_title(self,original_title):
        self.__original_title = original_title

    @property
    def overview(self):
        return self.__overview

    @overview.setter
    def overview (self,overview):
        self.__overview = overview

    @property
    def popularity (self):
        return self.__popularity

    @popularity.setter
    def popularity (self,popularity):
        self.__popularity = popularity

    @property
    def poster_path (self):
        return self.__poster_path
    
    @poster_path.setter
    def poster_path (self,poster_path):
        self.__poster_path = poster_path

    @property 
    def release_date(self):
        return self.__release_date
    
    @release_date.setter
    def release_date (self,release_date):
        self.__release_date = release_date

    @property
    def title (self):
        return self.__title
    
    @title.setter
    def title (self,title):
        self.__title = title

    @property
    def video (self):
        return self.__video

    @video.setter
    def video (self,video):
        self.__video = video

    @property
    def vote_average (self):
        return self.__vote_average
    
    @vote_average.setter
    def vote_average (self,vote_average):
        self.__vote_average = vote_average

    @property
    def vote_count (self):
        return self.__vote_count
    
    @vote_count.setter
    def vote_count (self,vote_count):
        self.__vote_count = vote_count
