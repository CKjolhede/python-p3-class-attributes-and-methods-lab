class Song:
    count = 0
    artists = []
    genres = []
    genre_count= {}
    artist_count = {}

        
    @classmethod
    def add_to_genres(cls, genre):
        for genre in cls.genres:
            cls.genre_count[genre] = cls.genres.count(genre)
        return

    @classmethod
    def add_to_artists(cls, artist):
        for artist in cls.artists:
            cls.artist_count[artist] = cls.artists.count(artist)
        return
            
    @classmethod
    def artist_count(cls):
        return cls.artists_dict

    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count = Song.count + 1
        Song.genres.append(genre)
        Song.artists.append(artist)
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        
