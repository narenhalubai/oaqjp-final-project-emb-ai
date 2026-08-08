import unittest
from emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):

    def test_positive(self):
        result = emotion_detector("I love this new technology.")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_negative(self):
        result = emotion_detector("I am very angry and upset.")
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_neutral(self):
        result = emotion_detector("The book is on the table.")
        self.assertIn(result["dominant_emotion"], [
            "anger", "disgust", "fear", "joy", "sadness"
        ])


if __name__ == "__main__":
    unittest.main()
