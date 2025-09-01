import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    """
    A test suite for the emotion_detector function.
    """
    def test_statement_joy(self):
        """
        Test that the dominant emotion for 'I am glad this happened' is 'joy'.
        """
        response = emotion_detector("I am glad this happened")
        self.assertEqual(response['dominant_emotion'], 'joy')

    def test_statement_anger(self):
        """
        Test that the dominant emotion for 'I am really mad about this' is 'anger'.
        """
        response = emotion_detector("I am really mad about this")
        self.assertEqual(response['dominant_emotion'], 'anger')

    def test_statement_disgust(self):
        """
        Test that the dominant emotion for 'I feel disgusted just hearing about this' is 'disgust'.
        """
        response = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(response['dominant_emotion'], 'disgust')

    def test_statement_sadness(self):
        """
        Test that the dominant emotion for 'I am so sad about this' is 'sadness'.
        """
        response = emotion_detector("I am so sad about this")
        self.assertEqual(response['dominant_emotion'], 'sadness')

    def test_statement_fear(self):
        """
        Test that the dominant emotion for 'I am really afraid that this will happen' is 'fear'.
        """
        response = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(response['dominant_emotion'], 'fear')

# This makes the script runnable from the command line
if __name__ == '__main__':
    unittest.main()