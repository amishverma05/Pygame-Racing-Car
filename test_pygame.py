import unittest
import pygame
from cargame import Game

class TestApp(unittest.TestCase):
    """
    Unit tests for Pygame Racing Car app functionalities including event loop and game over functions are behaving as expected.
    """
    def setUp(self):
        """
        Initialize pygame
        """
        pygame.init()
        self.game = Game()

    def tearDown(self):
        """
        Clean up the test environment by quit the pygame
        """
        pygame.quit()

    def test_score_increase_when_enemy_car_speed_increase(self):

        """
        If score is over 1500, score should be increase by 1 + int(0.5 * (score//1500))
        """

        # score should be 1500 + 1 + int(0.5 * (1500//1500) = 1501
        self.game.score = 1500
        self.game.update_score()
        self.assertEqual(self.game.score, 1501)

        # score should be 3000 + 1 + int(0.5 * (3000//1500) = 3002
        self.game.score = 3000
        self.game.update_score()
        self.assertEqual(self.game.score, 3002)

if __name__ == '__main__':
    unittest.main()