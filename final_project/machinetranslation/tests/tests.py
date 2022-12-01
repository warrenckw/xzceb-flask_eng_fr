"""Testing module"""

import unittest
from translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase):
    """En to Fr test"""
    def test1(self):
        """test none input for en to fr"""
        self.assertNotEqual(english_to_french('None'),'')
        """test null input for en to fr"""
        self.assertNotEqual(english_to_french(0),0)
        """test en to fr function"""
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        """test en not to en function"""
        self.assertNotEqual(english_to_french('Hello'),'Hello')

class TestF2E(unittest.TestCase):
    """Fr to En test"""
    def test1(self):
        """test none input for fr to en"""
        self.assertNotEqual(french_to_english('None'),'')
        """test null input for fr to en"""
        self.assertNotEqual(french_to_english(0),0)
        """test fr to en function"""
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        """test en not to en function"""
        self.assertNotEqual(french_to_english('Bonjour'),'Bonjour')

unittest.main()
