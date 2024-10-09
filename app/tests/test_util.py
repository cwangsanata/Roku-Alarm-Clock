import unittest
from app.util import select_random, load_yaml

class TestUtils(unittest.TestCase):
    '''
    Test select_random function
    '''
    def test_select_random(self):
        arr = [1, 2, 3, 4, 5]
        self.assertIn(select_random(arr), arr)
    
    def test_select_random_empty(self):
        arr = []
        with self.assertRaises(IndexError):
            select_random(arr)

    '''
    Test load_yaml function
    '''
    data = load_yaml('tests/test_data.yaml')
    def test_load_yaml_multiple(self):
        videos = self.data['content']['video_ids_multiple']
        self.assertIsInstance(videos, list)
        for video in videos:
            self.assertIsInstance(video, str)
    
    def test_load_yaml_single(self):
        videos = self.data['content']['video_ids_single']
        self.assertIsInstance(videos, list)
        for video in videos:
            self.assertIsInstance(video, str)

    def test_load_yaml_empty(self):
        videos = self.data['content']['video_ids_empty']
        self.assertIsInstance(videos, list)
        self.assertEqual(len(videos), 0)

if __name__ == '__main__':
    unittest.main()

