import unittest

from src.high_scores import High_Scores

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0

class HighScoresTest(unittest.TestCase):
    def setUp(self):
        self.player1 = [13, 16, 11, 13, 17]
        self.player2 = [10, 12, 17, 14, 20]
        self.player3 = [16, 3, 18, 19, 7, 14, 17, 12, 20]
        self.player4 = [13, 14, 15, 13, 14, 17, 15]
        self.high_scores = High_Scores()    
    # Tests

    # Test latest score (the last thing in the list)
    def test_latest(self):
        player1 = self.player1
        self.assertEqual(17, self.high_scores.latest(player1))

    # Test personal best (the highest score in the list)
    def test_personal_best(self):
        player2 = self.player2
        self.assertEqual(20, self.high_scores.personal_best(player2))

    # Test top three from list of scores
    def test_personal_top_three(self):
        player3 = self.player3
        top_scores = [18, 19, 20]
        self.assertEqual(top_scores, self.high_scores.personal_top_three(player3))

    # Test ordered from highest tp lowest
    def test_high_to_low(self):
        player3 = self.player3
        hiToLow = [20, 19, 18, 17, 16, 14, 12, 7, 3]
        self.assertEqual(hiToLow, self.high_scores.high_to_low(player3))

    # Test top three when there is a tie
    def test_no_ties(self):
        player4 = self.player4
        result = [14, 15, 17]
        self.assertEqual(result, self.high_scores.no_ties(player4))


    # Test top three when there are less than three
    def test_less_three(self):
        player5 = [14, 13]
        result = [0, 13, 14]
        self.assertEqual(result, self.high_scores.less_three(player5))


    # Test top three when there is only one
    def test_only_one(self):
        player6 = [12]
        result = [0, 0, 12]
        self.assertEqual(result, self.high_scores.only_one(player6))

