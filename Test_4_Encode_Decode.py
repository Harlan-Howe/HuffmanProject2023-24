import unittest
from HuffmanEncoderFile import HuffmanEncoder
import logging

class MyTestCase(unittest.TestCase):
    # @unittest.skip("Skipping testEncode.")
    def test_1_encode(self):
        logging.info("-------------------------------------\nTesting encode.")
        encoder = HuffmanEncoder("I'm here to kick butt and chew bubblegum. And I'm all out of bubblegum.")
        encoder.build_frequency_dictionary()
        encoder.build_priority_queue()
        encoder.build_tree()
        encoder.build_encode_dictionary_with_tree()
        gibberish = encoder.encode_message(
            "I'm here to kick butt and chew bubblegum. And I'm all out of bubblegum.")
        expected = [0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1,
                    1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1,
                    1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0,
                    0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1,
                    1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0,
                    1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0,
                    1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0,
                    1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1,
                    0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1]

        self.assertEqual(gibberish, expected, "Encoded text did not match.")

    # @unittest.skip("Skipping testdecode.")
    def test_2_decode(self):
        logging.info("------------------------------------\nTesting decode.")
        encoder = HuffmanEncoder("Where in the world is Carmen Sandiego?")
        encoder.do_setup()
        sequence_to_decode = [0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0,
                              1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0]
        self.assertEqual(encoder.decode_message(sequence_to_decode),
                         "on the internet",
                         "Decoded phrase does not match.")

    def test_3_short_encode_decode(self):
        logging.info("-----------------------------------\nTesting short encode decode")
        douglas_adams = ("There is an art to flying, or rather a knack. The knack lies in learning how to throw "
                         "yourself at the ground and miss.")
        encoder = HuffmanEncoder(douglas_adams)
        encoder.do_setup()
        encoded_flying_quote = encoder.encode_message(douglas_adams)
        decoded_flying_quote = encoder.decode_message(encoded_flying_quote)
        self.assertEqual(douglas_adams, decoded_flying_quote)
        logging.info(decoded_flying_quote)
        logging.info(f"Original size in ASCII: {8 * len(douglas_adams)} bits ({len(douglas_adams)} bytes)")
        logging.info(f"encoded length: {len(encoded_flying_quote)} bits ({int(len(encoded_flying_quote) / 8+0.9)} bytes)")
        logging.info(f"compression ratio: {len(encoded_flying_quote) / len(douglas_adams) / 8 * 100:3.2f}%")

    def test_4_long_encode_decode(self):
        logging.info("-----------------------------------\nTesting long encode decode")
        gettysberg = ("Four score and seven years ago our fathers brought forth on this continent, a new nation, " 
                      "conceived in Liberty, and dedicated to the proposition that all men are created equal.\n" 
                      "Now we are engaged in a great civil war, testing whether that nation, or any nation so " 
                      "conceived and so dedicated, can long endure. We are met on a great battle-field of that " 
                      "war. We have come to dedicate a portion of that field, as a final resting place for those " 
                      "who here gave their lives that that nation might live. It is altogether fitting and proper " 
                      "that we should do this.\n" 
                      "But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow " 
                      "-- this ground. The brave men, living and dead, who struggled here, have consecrated it, " 
                      "far above our poor power to add or detract. The world will little note, nor long remember " 
                      "what we say here, but it can never forget what they did here. It is for us the living, " 
                      "rather, to be dedicated here to the unfinished work which they who fought here have thus " 
                      "far so nobly advanced. It is rather for us to be here dedicated to the great task remaining " 
                      "before us -- that from these honored dead we take increased devotion to that cause for which " 
                      "they gave the last full measure of devotion -- that we here highly resolve that these dead " 
                      "shall not have died in vain -- that this nation, under God, shall have a new birth of freedom " 
                      "-- and that government of the people, by the people, for the people, shall not perish from the " 
                      "earth.\nAbraham Lincoln\nNovember 19, 1863")
        encoder = HuffmanEncoder(gettysberg)
        encoder.do_setup()
        encoded_getty = encoder.encode_message(gettysberg)

        reset_getty = encoder.decode_message(encoded_getty)
        self.assertEqual(gettysberg, reset_getty)
        logging.info(reset_getty)

        logging.info(f"Original size in ASCII: {8 * len(gettysberg)} bits ({len(gettysberg)} bytes)")
        logging.info(f"encoded length: {len(encoded_getty)} bits ({int(len(encoded_getty)/8+0.9)} bytes)")
        logging.info(f"compression ratio: {(len(encoded_getty) / len(gettysberg) / 8 * 100):3.2f}%")

    def test_encoder_exception(self):
        encoder = HuffmanEncoder("There can be only one.")
        encoder.build_frequency_dictionary()
        encoder.build_priority_queue()
        encoder.build_tree()
        encoder.build_encode_dictionary_with_tree()

        with self.assertRaises(KeyError, msg="Encoder should raise a KeyError when encountering a letter not in the "
                                             "frequency dictionary."):
            encoder.encode_message("Two to tango.")


if __name__ == '__main__':
    unittest.main()
