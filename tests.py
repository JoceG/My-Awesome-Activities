import unittest
from api import new_results, get_activity, get_key

results = [{'activity': 'Start a family tree', 
            'type': 'social', 
            'participants': 1, 
            'price': 0, 
            'link': 'https://en.wikipedia.org/wiki/Family_tree', 
            'key': '6825484', 
            'accessibility': 1}, 

            {'activity': 'Have a picnic with some friends', 
            'type': 'social', 
            'participants': 3, 
            'price': 0.1, 
            'link': '', 
            'key': '6813070', 
            'accessibility': 0.1}, 

            {'activity': 'Improve your touch typing', 
            'type': 'busywork', 
            'participants': 1, 
            'price': 0, 
            'link': 'https://en.wikipedia.org/wiki/Touch_typing', 
            'key': '2526437', 
            'accessibility': 0.8}]


class TestGetActivity(unittest.TestCase):
    def test_new_results_size(self):
        self.assertEqual(len(new_results()), 10)


    def test_get_activity(self):
        self.assertEqual(get_activity(results[0]), 'Start a family tree')
        self.assertEqual(get_activity(results[1]), 'Have a picnic with some friends')
        self.assertEqual(get_activity(results[2]), 'Improve your touch typing')


    def test_get_key(self):
        self.assertEqual(get_key(results[0]), '6825484')
        self.assertEqual(get_key(results[1]), '6813070')
        self.assertEqual(get_key(results[2]), '2526437')


if __name__ == '__main__':
    unittest.main()
