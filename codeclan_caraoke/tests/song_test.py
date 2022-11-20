import unittest
from classes.song import *
from tests.room_test import *

class TestSong(unittest.TestCase):
    def setUp(self):
        self.request_1 = Song("Verka Serduchka","Lasha Tumbai")
        self.request_2 = Song("Dana International","Diva")

    def test_song_name(self):
        self.assertEqual("Lasha Tumbai", self.request_1.song_name)

    def test_artist_name(self):
        self.assertEqual("Dana International", self.request_2.artist)