class Song:

    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        type(self).add_song_to_count()
        type(self).add_to_genres(genre)
        type(self).add_to_artists(artist)
        type(self).add_to_genre_count(genre)
        type(self).add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1


## EXTRA EXTRA
    @classmethod
    def find_artist_with_most_songs(cls):
        try:
            return max(cls.artist_count, key = lambda k: cls.artist_count.get(k, 0))
        except Exception as e:
            print(e)
            return False
        
    


# s1 = Song("99 Problems", "Jay Z", "Rap")
# s2 = Song("Halo", "Beyonce", "Pop")
# s3 = Song("Smells Like Teen Spirit", "Nirvana", "Rock")
# s4 = Song("Girls", "Beyonce", "Pop")
print('done')