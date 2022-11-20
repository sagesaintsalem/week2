# from classes.guest import *

class Room:
    def __init__(self, name, spaces, entry_fee, till):
        self.name = name
        self.spaces = spaces
        self.entry_fee = entry_fee
        self.till = till
        self.current_guests = []
        self.waiting_list = []
        self.playlist = []
        self.song_history = []
        
    def entry_paid(self, guest):
        self.till += self.entry_fee
        guest.wallet -= self.entry_fee

    def check_in(self, guest):
        if self.spaces > 0:
            self.current_guests.append(guest.name)
            self.spaces -= 1
        else:
            self.waiting_list.append(guest.name)

    def check_out(self, guest):
        self.current_guests.remove(guest.name)
        self.spaces += 1

    def add_song(self, song):
        self.playlist.append(song.song_name)

    def song_played(self):
        del self.playlist[0]
