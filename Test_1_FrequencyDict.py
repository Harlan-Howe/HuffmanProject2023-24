import unittest
from HuffmanEncoderFile import HuffmanEncoder
import logging

class MyTestCase(unittest.TestCase):

    def test_frequency_dict(self):
        encoder = HuffmanEncoder("The quick brown fox")
        encoder.build_frequency_dictionary()
        self.assertEqual(encoder.freq_dict["q"], 1, "\"q\" should be found once.")
        self.assertEqual(encoder.freq_dict["o"], 2, "\"o\" should be found twice.")
        self.assertEqual(encoder.freq_dict[" "], 3, "\" \" should be found three times.")
        self.assertFalse("j" in encoder.freq_dict, "\"j\" should not be found in the string.")
        self.assertTrue("x" in encoder.freq_dict, "\"x\" should be found in the string.")

        expected = {"T": 1, "h": 1, "e": 1, " ": 3, "q": 1, "u": 1, "i": 1, "c": 1, "k": 1, "b": 1, "r": 1,
                    "o": 2, "w": 1, "n": 1, "f": 1, "x": 1}
        self.assertEqual(encoder.freq_dict, expected, "Did not get expected dictionary.")
        logging.info(encoder.freq_dict)


if __name__ == '__main__':
    unittest.main()
