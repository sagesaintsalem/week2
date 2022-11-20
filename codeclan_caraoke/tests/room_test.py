import unittest
from classes.room import *
from classes.song import Song
from classes.guest import *

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.request_1 = Song("Verka Serduchka","Lasha Tumbai")
        self.request_2 = Song("Dana International","Diva")
        self.request_3 = Song("Zdob si Zdub ft Fratii Advahov","Trenuletul")
        self.request_4 = Song("Koza Mostra ft Agathonas Iakovidis","Alcohol is Free")
        self.request_5 = Song("Lordi", "Hard Rock Hallelujah")
        self.request_6 = Song("Maneskin", "Zitti e Buoni")
        self.room = Room("Carrie's OK", 4, 2, 100.00)
        self.guest_1 = Guest("Annie", 50)
        self.guest_2 = Guest("Bobby", 25)
        self.guest_3 = Guest("Veronica", 60)
        self.guest_4 = Guest("Tim", 80)
        self.guest_5 = Guest("Alan", 20)


    def test_entry_paid(self):
        self.room.entry_paid(self.guest_2)
        self.assertEqual(102.00, self.room.till)
        self.assertEqual(23, self.guest_2.wallet)

    def test_check_in(self):
        self.room.check_in(self.guest_4)
        self.assertEqual(["Tim"], self.room.current_guests)
        self.assertEqual(3, self.room.spaces)
        
    def test_check_out(self):
        self.room.check_in(self.guest_4)
        self.room.check_out(self.guest_4)
        self.assertEqual([], self.room.current_guests)
        self.assertEqual(4, self.room.spaces)
    
    def test_overbooked(self):
        self.room.check_in(self.guest_1)
        self.room.check_in(self.guest_2)
        self.room.check_in(self.guest_3)
        self.room.check_in(self.guest_4)
        self.room.check_in(self.guest_5)
        self.assertEqual(["Annie", "Bobby", "Veronica", "Tim"], self.room.current_guests)
        self.assertEqual(["Alan"], self.room.waiting_list)
        self.assertEqual(0, self.room.spaces)

    
    def test_add_song(self):
        self.room.add_song(self.request_3)
        self.assertEqual(["Trenuletul"], self.room.playlist)

    def test_song_played(self): 
        self.room.add_song(self.request_1)
        self.room.add_song(self.request_2)
        self.room.add_song(self.request_4)
        self.room.song_played()
        self.assertEqual(["Diva", "Alcohol is Free"], self.room.playlist)
       #I added this because I figured that a playlist would automatically remove
       #songs already played. I wanted to add played songs to a song history list but
       #couldn't figure it out.