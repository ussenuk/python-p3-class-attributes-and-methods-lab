class Song:

    count = 0   
    genres = []
    duplucate_genres =[]
    genre_count = {}
    artists = []
    duplucate_artists =[]
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls, increment = 1):
        cls.count += increment

    @classmethod
    def add_to_genres(cls, genre):
        # control duplicate before the next step 
        if genre not in cls.genres:
            cls.genres.append(genre)
        # cls.duplucate_genres.append(genre)
        
    @classmethod
    def add_to_artists(cls, artist):
        # control duplicate before the next step
        if artist not in cls.artists:
            cls.artists.append(artist)
        # cls.duplucate_artists.append(artist)
        
    @classmethod
    def add_to_genre_count(cls, genre):
         #iterate over duplicate genres list and populate a dictionary with key/value pairs
        cls.duplucate_genres.append(genre)
        cls.genre_count = {i:cls.duplucate_genres.count(i) for i in cls.duplucate_genres}
        # print(genre_count)
        # add_to_genres

    @classmethod
    def add_to_artist_count(cls, artist):
         #iterate over duplicate artists list and populate a dictionary with key/value pairs
       
        cls.duplucate_artists.append(artist)
        cls.artist_count = {i:cls.duplucate_artists.count(i) for i in cls.duplucate_artists}
        
# without the genre and artist cout
# ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
# droit_chemin = Song("Droit Chemin", "Fally Ipupa", "Rhumba")
# Maboko_pamba = Song("Maboko Pamba", "Ferre", "Rhumba")
# Associer = Song("Associer", "Fally Ipupa", "Rhumba")
# Litaka = Song("Litaka", "Ferre", "Rhumba")
# print(ninety_nine_problems.name)
# print(ninety_nine_problems.artist)
# print(ninety_nine_problems.genre)

# added to genre/artist list without repetition
print(Song.genres)
# print(Song.duplucate_genres)
print(Song.artists)
# print(Song.duplucate_artists)

# counting songs
print(Song.count)


# Add to genre/artist count using a dictionary
print(Song.genre_count)
print(Song.artist_count)
# print(Song.add_to_artist_count)



