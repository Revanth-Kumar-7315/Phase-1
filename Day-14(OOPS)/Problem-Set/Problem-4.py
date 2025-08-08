# 4. Model a Playlist class that contains multiple Song objects (Composition).

class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration  # in minutes

    def __str__(self):
        return f"{self.title} by {self.artist} ({self.duration} mins)"


class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def total_duration(self):
        return sum(song.duration for song in self.songs)

    def list_of_songs(self):
        for song in self.songs:
            print(song)

    def remove_song(self, title):  # Optional
        self.songs = [song for song in self.songs if song.title != title]