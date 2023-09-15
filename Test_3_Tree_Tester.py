import unittest
from HuffmanEncoderFile import HuffmanEncoder


class MyTestCase(unittest.TestCase):

    def test_build_tree(self):
        encoder = HuffmanEncoder("May the force be with you, always.")
        encoder.build_frequency_dictionary()
        encoder.build_priority_queue()
        encoder.build_tree()
        print("This is your tree:")
        encoder.encoding_tree.print_tree()
        print("----------------------------------------")
        print("This is what Mr. Howe's looked like.")
        print("""
                       [i]
            <
                    [u]
                <
                    [b]
        <
            [y]
    <
                [o]
            <
                    [M]
                <
                    [.]
        <
                    [f]
                <
                    [,]
            <
                [h]
<
                    [l]
                <
                    [s]
            <
                [t]
        <
                [w]
            <
                    [r]
                <
                    [c]
    <
            [ ]
        <
                [e]
            <
                [a]
-----------------------------------------
""")

        encoder.build_encode_dictionary_with_tree()

        expected = {"a": [1, 1, 1, 1], "b": [0, 0, 0, 1, 1], "c": [1, 0, 1, 1, 1], "e": [1, 1, 1, 0],
                    "f": [0, 1, 1, 0, 0], "h": [0, 1, 1, 1], "i": [0, 0, 0, 0], "l": [1, 0, 0, 0, 0],
                    "M": [0, 1, 0, 1, 0], "o": [0, 1, 0, 0], "r": [1, 0, 1, 1, 0],  "s": [1, 0, 0, 0, 1],
                    "t": [1, 0, 0, 1], "u": [0, 0, 0, 1, 0], "w": [1, 0, 1, 0], "y": [0, 0, 1], " ": [1, 1, 0],
                    ".": [0, 1, 0, 1, 1], ",": [0, 1, 1, 0, 1]}

        self.assertEqual(len(expected), len(encoder.encode_dictionary),
                         "expected and encoder have different number of keys.")

        for item in sorted(encoder.encode_dictionary.keys()):
            print(f"\"{item}\" : {encoder.encode_dictionary[item]}")
            self.assertTrue(item in expected, "unexpected key in the encode_dictionary")
            self.assertEqual(expected[item], encoder.encode_dictionary[item], f"Value for {item} did not match.")

    def test_build_long(self):
        """
        Tests whether we can build a encoder dictionary for a long piece of text.
        Sample text is the opening chapter of "Foundation" by Isaac Asimov, copyright 1951
        :return:
        """
        source_text = """
        HARI SELDON—. . . born in the 11,988th year of the Galactic Era; died 12,069. The dates are more commonly given in terms of the current Foundational Era as -79 to the year 1 F.E. Born to middle-class parents on Helicon, Arcturus sector (where his father, in a legend of doubtful authenticity, was a tobacco grower in the hydroponic plants of the planet), he early showed amazing ability in mathematics. Anecdotes concerning his ability are innumerable, and some are contradictory. At the age of two, he is said to have . . .

. . . Undoubtedly his greatest contributions were in the field of psychohistory. Seldon found the field little more than a set of vague axioms; he left it a profound statistical science. . . .

. . . The best existing authority we have for the details of his life is the biography written by Gaal Dornick who, as a young man, met Seldon two years before the great mathematician's death. The story of the meeting . . .

ENCYCLOPEDIA GALACTICA*


Chapter One


His name was Gaal Dornick and he was just a country boy who had never seen Trantor before. That is, not in real life. He had seen it many times on the hyper-video, and occasionally in tremendous three-dimensional newscasts covering an Imperial Coronation or the opening of a Galactic Council. Even though he had lived all his life on the world of Synnax, which circled a star at the edges of the Blue Drift, he was not cut off from civilization, you see. At that time, no place in the Galaxy was.

There were nearly twenty-five million inhabited planets in the Galaxy then, and not one but owed allegiance to the Empire whose seat was on Trantor. It was the last half-century in which that could be said.

To Gaal, this trip was the undoubted climax of his young, scholarly life. He had been in space before so that the trip, as a voyage and nothing more, meant little to him. To be sure, he had traveled previously only as far as Synnax's only satellite in order to get the data on the mechanics of meteor driftage which he needed for his dissertation, but space-travel was all one whether one travelled half a million miles, or as many light years.

He had steeled himself just a little for the Jump through hyper-space, a phenomenon one did not experience in simple interplanetary trips. The Jump remained, and would probably remain forever, the only practical method of travelling between the stars. Travel through ordinary space could proceed at no rate more rapid than that of ordinary light (a bit of scientific knowledge that belonged among the items known since the forgotten dawn of human history), and that would have meant years of travel between even the nearest of inhabited systems. Through hyper-space, that unimaginable region that was neither space nor time, matter nor energy, something nor nothing, one could traverse the length of the Galaxy in the interval between two neighboring instants of time.

Gaal had waited for the first of those jumps with a little dread curled gently in his stomach, and it ended in nothing more than a trifling jar, a little internal kick which ceased an instant before he could be sure he had felt it. That was all.

And after that, there was only the ship, large and glistening; the cool production of 12,000 years of Imperial progress; and himself, with his doctorate in mathematics freshly obtained and an invitation from the great Hari Seldon to come to Trantor and join the vast and somewhat mysterious Seldon Project.

What Gaal was waiting for after the disappointment of the Jump was that first sight of Trantor. He haunted the View-room. The steel shutter-lids were rolled back at announced times and he was always there, watching the hard brilliance of the stars, enjoying the incredible hazy swarm of a star cluster, like a giant conglomeration of fireflies caught in mid-motion and stilled forever. At one time there was the cold, blue-white smoke of a gaseous nebula within five light years of the ship, spreading over the window like distant milk, filling the room with an icy tinge, and disappearing out of sight two hours later, after another Jump.

The first sight of Trantor's sun was that of a hard, white speck all but lost in a myriad such, and recognizable only because it was pointed out by the ship's guide. The stars were thick here near the Galactic center. But with each Jump, it shone more brightly, drowning out the rest, paling them and thinning them out.

An officer came through and said, "View-room will be closed for the remainder of the trip. Prepare for landing."

Gaal had followed after, clutching at the sleeve of the white uniform with the Spaceship-and-Sun of the Empire on it.

He said, "Would it be possible to let me stay? I would like to see Trantor."

The officer smiled and Gaal flushed a bit. It occurred to him that he spoke with a provincial accent.

The officer said, "We'll be landing on Trantor by morning."

"I mean I want to see it from Space."

"Oh. Sorry, my boy. If this were a space-yacht we might manage it. But we're spinning down, sun-side. You wouldn't want to be blinded, burnt, and radiation-scarred all at the same time, would you?"

Gaal started to walk away.

The officer called after him, "Trantor would only be a gray blur anyway, Kid. Why don't you take a space-tour once you hit Trantor. They're cheap."

Gaal looked back, "Thank you very much."

It was childish to feel disappointed, but childishness comes almost as naturally to a man as to a child, and there was a lump in Gaal's throat. He had never seen Trantor spread out in all its incredibility, as large as life, and he hadn't expected to have to wait longer."""

        encoder = HuffmanEncoder(source_text)
        encoder.build_frequency_dictionary()
        encoder.build_priority_queue()
        encoder.build_tree()

        encoder.build_encode_dictionary_with_tree()

        expected = {"\n": [1, 0, 0, 1, 0, 1, 1], " ": [1, 1, 1], "\"": [1, 1, 0, 0, 1, 1, 0, 1, 1],
                    "\'": [1, 0, 0, 1, 0, 1, 0, 1, 0], "(": [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    ")": [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1], "*": [1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0],
                    ",": [1, 1, 0, 1, 1, 1, 1], "-": [0, 1, 0, 0, 1, 1, 1, 1], ".": [0, 1, 0, 0, 0, 1],
                    "0": [1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1], "1": [0, 1, 0, 0, 1, 1, 1, 0, 0, 0],
                    "2": [1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0], "6": [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
                    "7": [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1], "8": [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
                    "9": [1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0], ";": [1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1],
                    "?": [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0], "A": [1, 1, 0, 0, 1, 1, 0, 0, 0],
                    "B": [1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1], "C": [1, 1, 0, 1, 1, 1, 0, 0, 0, 0],
                    "D": [0, 1, 0, 0, 1, 1, 0, 1, 1, 1], "E": [0, 1, 0, 0, 0, 0, 0, 1, 1],
                    "F": [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1], "G": [0, 1, 0, 0, 1, 1, 0, 0],
                    "H": [0, 1, 0, 0, 1, 1, 0, 1, 0], "I": [1, 1, 0, 0, 1, 1, 0, 0, 1],
                    "J": [0, 1, 0, 0, 1, 1, 0, 1, 1, 0], "K": [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                    "L": [0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1], "N": [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                    "O": [1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0], "P": [1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1],
                    "R": [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0], "S": [1, 0, 0, 1, 0, 1, 0, 1, 1],
                    "T": [1, 1, 0, 1, 1, 1, 0, 1], "U": [1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1],
                    "V": [1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1], "W": [0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
                    "Y": [0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0], "a": [1, 0, 1, 0], "b": [1, 1, 0, 0, 1, 1, 1],
                    "c": [1, 1, 0, 1, 1, 0], "d": [1, 0, 0, 0, 0], "e": [0, 0, 0], "f": [1, 0, 0, 1, 1, 1],
                    "g": [1, 0, 0, 0, 1, 0], "h": [0, 0, 1, 0], "i": [0, 1, 1, 0],
                    "j": [1, 1, 0, 0, 1, 1, 0, 1, 0, 1], "k": [1, 0, 0, 1, 0, 1, 0, 0], "l": [1, 1, 0, 0, 0],
                    "m": [1, 1, 0, 0, 1, 0], "n": [0, 1, 0, 1], "o": [0, 1, 1, 1], "p": [0, 1, 0, 0, 1, 0],
                    "r": [0, 0, 1, 1], "s": [1, 1, 0, 1, 0], "t": [1, 0, 1, 1], "u": [1, 0, 0, 1, 1, 0],
                    "v": [0, 1, 0, 0, 0, 0, 1], "w": [1, 0, 0, 1, 0, 0], "x": [0, 1, 0, 0, 1, 1, 1, 0, 1],
                    "y": [1, 0, 0, 0, 1, 1], "z": [0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
                    "—": [1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0]}

        self.assertEqual(len(expected), len(encoder.encode_dictionary),
                         "expected and encoder have different number of keys.")


        for item in encoder.encode_dictionary.keys():
            self.assertTrue(item in expected, "unexpected key in the encode_dictionary")
            self.assertEqual(expected[item], encoder.encode_dictionary[item], f"Value for {item} did not match.")


if __name__ == '__main__':
    unittest.main()
