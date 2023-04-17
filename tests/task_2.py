import unittest
from unittest.case import TestCase
from ya_disk import YaUploader

class TestYaDisk(TestCase):
    def test_create_folder(self):
        with open('token_ya_test.txt', 'r') as file:
            token_ya = file.read().strip()
        self.assertEqual(YaUploader(token_ya).get_create_folder(), 201)

    def test_authorisation_error(self):
        with open('token_ya_test2.txt', 'r') as file:
            token_ya = file.read().strip()
        self.assertEqual(YaUploader(token_ya).get_create_folder(), 401)

if __name__ == '__main__':
    unittest.main()