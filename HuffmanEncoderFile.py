from PriorityQueueFile import PriorityQueue
from TreeNodesFile import *
from typing import Dict, List


class HuffmanEncoder:
    def __init__(self, string_to_encode=""):
        self.encode_string = string_to_encode
        self.encode_dictionary: Dict[str, List[int]] = {}
        self.freq_dict: Dict[str, int] = {}
        self.frequency_queue: PriorityQueue[TreeNode[str]] = PriorityQueue[TreeNode[T]]()
        self.encoding_tree: TreeNode[str] = TreeNode[None]

    def do_setup(self):
        self.build_frequency_dictionary()
        self.build_priority_queue()
        self.build_tree()
        self.build_encode_dictionary_with_tree(self.encoding_tree)

    def build_frequency_dictionary(self):
        """
        construct a dictionary, self.freq_dict, where the various single-character strings found in the encode_string
        are the keys, and the number of times they appear are the values.
        For instance, "red beret" would lead to a dictionary {"r": 2, "e": 3, "d": 1, " ": 1, "b": 1, "t": 1}
        """
        self.freq_dict: Dict[str, int] = {}
        for character in self.encode_string:
            # ----------------------------------------
            # TODO: This is where you will write your code to either add a new item to the dictionary or to
            #  increment the item that is already there. The key should be the character
            #  and the value is the frequency.
            pass

            # ----------------------------------------

    def build_priority_queue(self):
        """
        create a min-heap priority queue of TreeNodes (called self.frequencyQueue) out of the data in self.freqDict.
        Your priorityQueue will have priority of the count of the letters, and the values will be brand-new LeafNodes,
        with the character as the value in the node.
        (That is, you'll need to make a new LeafNode[str] for each item in self.freq_dict and add it to the PQ.)

        """
        self.frequency_queue: PriorityQueue[TreeNode[str]] = PriorityQueue[TreeNode[T]](isMinHeap=True)
        # ----------------------
        # TODO: You'll be writing this part! Insert your code here.

        # ----------------------

    def build_tree(self):
        """
        Use the priority queue (self.frequencyQueue) to generate a Huffman Encoding tree for this string.
        (We are using the queue to make the most efficient tree for this string, so that frequently used characters
        appear higher in the tree.) This will radically change the PQ in the process. Here is the algorithm for doing
        this:
            • Pop *two* PQ nodes (priority, TreeNode[str]) off the priority queue. These are the two lowest-frequency
              nodes on the tree.
            • Create a new JointNode with these two tree nodes. (1st -> left; 2nd -> right)
            • Add the new JointNode back into the priority queue, with a new priority that is the sum of the previous
              two.
            • Repeat until you cannot pop two nodes - that is, until there are no more pairs to combine!
            • The one PQ node left in the queue will hold your new tree, which you should store in the variable
              self.encodingTree.
        Note: I've written the last step for you... so don't reinvent it.
        """
        # ----------------------
        # TODO: You'll be writing this part! Insert your code here.

        # suggestion: each time through your loop, log the
        # priority queue to help you debug.
        # OR
        # Each time you pop a node, log its priority and the node itself (via the node's printTree method)
        # and each time you are about to push a node, print its priority and the node itself.
        #  e.g.:
        #  popped:
        #   13
        #   X
        #  popped:
        #   18
        #       J
        #     <
        #       Z
        #   <
        #     Q
        #  pushed:
        #   31
        #     X
        #   <
        #         J
        #       <
        #         Z
        #     <
        #       Q
        # ----------------------

        last_PQ_Node = self.frequency_queue.pop()
        self.encoding_tree: TreeNode[str] = last_PQ_Node[1]

    def build_encode_dictionary_with_tree(self, root: TreeNode[str] = None, path_so_far: List[int] = []):
        """
        Generates a lookup table based on the given tree, producing a dictionary of characters --> 0/1 code sequences.
        (A recursive method)
        :param root: the root of the tree or subtree to add to dictionary.
        :param path_so_far: the path (a list of 0s and 1s) that got us to this root.
        :return: None
        Note: this is building self.encode_dictionary, a dictionary {str -> list of 0s and 1s} that was initialized
        in __init__().
        """
        # I've written this one for you.
        if root is None:
            root = self.encoding_tree  # ok to do, because we would only go left or right recursively if there is a left
            # and right, so this must be the real root node.

        if isinstance(root, JointNode):  # is this node a joint node?
            # The assertion on the next line should never trigger... (i.e., the statement should always be true),
            # but if it does trigger on a false, you should know about it!
            assert root.left is not None and root.right is not None, "Found a joint node with None for a child. "\
                   "That shouldn't happen... there's something wrong with your encoding tree."

            # as you might imagine, the JointNodes are handled recursively.
            left_list = path_so_far[:]  # makes a copy
            left_list.append(0)
            self.build_encode_dictionary_with_tree(root.left, left_list)
            right_list = path_so_far[:]  # makes a copy
            right_list.append(1)
            self.build_encode_dictionary_with_tree(root.right, right_list)

        else:  # then this must be a leaf node.... Note that this is the only time we actually add anything to the
            # dictionary. And it's the base case.
            self.encode_dictionary[root.value] = path_so_far

    def encode_message(self, message_to_encode: str) -> List[int]:
        """
        Use the self.encodingDictionary to convert each letter into a sequence of 1's and 0's (bits),
        and generate a (very) long array of bits, which you should return.
        :param message_to_encode: a string, all of whose characters should be contained in the encoding tree.
        :return: a (very long) list of ones and zeros.
        """
        encoded_result: List[int] = []
        # ----------------------
        # TODO: You'll be writing this part! Insert your code here.
        for char in message_to_encode:
            pass

            # if there is a problem, you should throw the following.
            # raise new KeyError(f"The letter \'{char}\' was not contained in the key string.")

        # ----------------------

        return encoded_result

    def decode_message(self, message_to_decode: List[int]) -> str:
        """

        :param message_to_decode:
        :return:
        """
        decoded_result = ""
        p = self.encoding_tree
        # ----------------------
        # TODO: You'll be writing this part! Insert your code here.
        # I suggest you make use of "if isinstance(p, JointNode):" and/or "if isinstance(p, LeafNode):"

        # ----------------------

        return decoded_result
