import unittest
from HuffmanEncoderFile import HuffmanEncoder
from PriorityQueueFile import PriorityQueue


class MyTestCase(unittest.TestCase):
    def test_PQ(self):
        """
        tests whether a frequency dictionary is created correctly with a short piece of text.
        :return:
        """
        encoder = HuffmanEncoder("How much wood would a woodchuck chuck if a woodchuck could chuck wood?")
        encoder.build_frequency_dictionary()
        encoder.build_priority_queue()
        PQ: PriorityQueue[str] = encoder.frequency_queue

        expected = [[1, "H"], [1, "m"], [1, "i"], [5, "h"], [2, "l"], [4, "k"], [1, "f"], [12, " "], [6, "d"],
                    [11, "o"], [2, "a"], [7, "u"], [6, "w"], [10, "c"], [1, "?"]]
        # expected_pq:PriorityQueue[str] = PriorityQueue[str](tree=expected, isMinHeap=True)

        self.assertFalse(PQ.is_empty(), "The priority queue should not be empty.")
        for i in range(len(PQ.my_tree)):
            self.assertEqual(expected[i][0], PQ.my_tree[i][0])
            self.assertEqual(expected[i][1], PQ.my_tree[i][1].value)

    def test_PQ_long(self):
        """
        tests whether a frequency dictionary is created correctly with a longer piece of text.
        :param self:
        :return:
        """
        # text from "Snow Crash" by Neal Stephenson, copyright 1992, [four-letter words slightly altered.]
        sample_text = """Chapter One
        
        The Deliverator belongs to an elite order, a hallowed subcategory. He's got esprit up to here. Right now, he is preparing to carry out his third mission of the night. His uniform is black as activated charcoal, filtering the very light out of the air. A bullet will bounce off its arachnofiber weave like a wren hitting a patio door, but excess perspiration wafts through it like a breeze through a freshly napalmed forest. Where his body has bony extremities, the suit has sintered armorgel: feels like gritty jello, protects like a stack of telephone books.
        
        When they gave him the job, they gave him a gun. The Deliverator never deals in cash, but someone might come after him anyway-might want his car, or his cargo. The gun is tiny, aero-styled, lightweight, the kind of a gun a fashion designer would carry; it fires teensy darts that fly at five times the velocity of an SR-71 spy plane, and when you get done using it, you have to plug it into the cigarette lighter, because it runs on electricity.
        
        The Deliverator never pulled that gun in anger, or in fear. He pulled it once in Gila Highlands. Some punks in Gila Highlands, a fancy Burbclave, wanted themselves a delivery, and they didn't want to pay for it. Thought they would impress the Deliverator with a baseball bat. The Deliverator took out his gun, centered its laser doohickey on that poised Louisville Slugger, fired it. The recoil was immense, as though the weapon had blown up in his hand. The middle third of the baseball bat turned into a column of burning sawdust accelerating in all directions like a bursting star. Punk ended up holding this bat handle with milky smoke pouring out the end. Stupid look on his face. Didn't get nothing but trouble from the Deliverator.
        
        Since then the Deliverator has kept the gun in the glove compartment and relied, instead, on a matched set of samurai swords, which have always been his weapon of choice anyhow. The punks in Gila Highlands weren't afraid of the gun, so the Deliverator was forced to use it. But swords need no demonstrations.
        
        The Deliverator's car has enough potential energy packed into its batteries to fire a pound of bacon into the asteroid Belt. Unlike a bimbo box or a Burb beater, the Deliverator's car unloads that power through gaping, gleaming, polished sphincters. When the Deiverator puts the hammer down, s**t happens. You want to talk contact patches? Your car's tires have tiny contact patches, talk to the thee asphalt in four places the size of your tongue. The Deliverator's car has big sticky tires with contact patches the size of a fat lady's thighs. The Deliverator is in touch with the road, starts like a bad day, stops on a peseta.
        
        Why is the Deliverator so equipped? Because people rely on him. He is a role model. This is America. People do whatever the f**k they feel like doing, you got a problem with that? Because they have a right to. And because they have guns and no one can f**king stop them. As a result, this country has one of the worst economies in the world. When it gets down to it—talking trade balances here—once we've brain-drained all our technology into other countries, once things have evened out, they're making cars in Bolivia and microwave ovens in Tadzhikistan and selling them here—once our edge in natural resources has been made irrelevant by giant Hong Kong ships and dirigibles that can ship North Dakota all the way to New Zealand for a nickel—once the Invisible Hand has taken all those historical inequities and smeared them out into a broad global layer of what a Pakistani brickmaker would consider to be prosperity—you know what? There's only four things we do better than anyone else:
        
        music
        movies
        microcode (software),
        high-speed pizza delvery
        
        The Deliverator used to make software. Still does, sometimes. But if life were a mellow elementary school run by well-meaning education Ph.D.s, the Deliverator's report card would say: "Hiro is so bright and creative but needs to work harder on his cooperation skills."
        
        So now he has this other job. No brightness or creativity involved—but no cooperation either. Just a single principle: the Deliverator stands tall, your pie in thirty minutes or you can have it free, shoot the driver, take his car, file a class-action suit. The Deliverator has been working this job for six months, a rich and lengthy tenure by his standards, and has never delivered a pizza in more than twenty-one minutes."
        """

        encoder = HuffmanEncoder(sample_text)
        encoder.build_frequency_dictionary()
        encoder.build_priority_queue()
        PQ: PriorityQueue[str] = encoder.frequency_queue

        print(PQ)

        expected = [[1, "C"], [1, "O"], [1, "U"], [4, "A"], [1, ";"], [1, "K"], [1, "Z"], [4, "x"], [4, ":"], [1, "7"],
                    [1, "1"], [2, "Y"], [2, "R"], [1, "I"], [1, ")"], [56, "v"], [42, "k"], [8, "z"], [4, "j"],
                    [22, "\n"], [7, "S"], [1, "L"], [21, "D"], [4, "P"], [4, "?"], [2, "q"], [10, "H"], [1, "("],
                    [3, "\""], [1, "J"], [930, " "], [66, "p"], [263, "o"], [52, "f"], [208, "h"], [59, "b"],
                    [84, "g"], [5, "W"], [320, "t"], [113, "d"], [207, "s"], [224, "n"], [46, ","], [57, "w"],
                    [8, "B"], [433, "e"], [96, "c"], [99, "u"], [6, "*"], [220, "r"], [43, "."], [63, "y"], [6, "—"],
                    [279, "a"], [17, "T"], [157, "l"], [3, "N"], [272, "i"], [13, "\'"], [58, "m"]]

        self.assertFalse(PQ.is_empty(), "The priority queue should not be empty.")
        for i in range(len(PQ.my_tree)):
            self.assertEqual(expected[i][0], PQ.my_tree[i][0])
            self.assertEqual(expected[i][1], PQ.my_tree[i][1].value)


if __name__ == '__main__':
    unittest.main()
