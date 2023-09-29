from typing import Generic, TypeVar


T = TypeVar("T")


class TreeNode(Generic[T]):
    def __init__(self, value: T = None, left: "TreeNode[T]" = None, right: "TreeNode[T]" = None):
        self.value = value
        self.left = left
        self.right = right

    def has_left(self) -> bool:
        return self.left is not None

    def has_right(self) -> bool:
        return self.right is not None

    def string_of_tree(self, indentation_level: int = 0):
        """
            builds a string to visualize this tree. -- not implemented in abstract TreeNode.
        :param indentation_level: number of tabs before this line and its children
        :return: string describing this node and its children.
        """


# ---------------------------------------------------------------------------
class LeafNode(TreeNode[T]):
    def __init__(self, value: T = None):
        super().__init__(value=value, left=None, right=None)

    def has_left(self) -> bool:
        return False

    def has_right(self) -> bool:
        return False

    def __str__(self):
        """ this is like toString() in java, when the user wants to print this node."""
        if self.value == '\n':
            return f"[\\n]"
        return f"[{self.value}]"

    def __repr__(self):
        """ this is like toString() in java, when the user is printing a bunch of these
        objects inside another data structure. We'll need both versions."""
        if self.value == '\n':
            return f"[\\n]"
        return f"[{self.value}]"

    def string_of_tree(self, indentation_level: int = 0):
        """
        Builds a string to visualize this tree.
        :param indentation_level: number of tabs before this line and its children
        :return: string describing this node
        """
        return f"{' ' * (4 * indentation_level)}{self}\n"
# ---------------------------------------------------------------------------


class JointNode(TreeNode[T]):
    def __init__(self, left: "TreeNode[T]", right: "TreeNode[T]"):
        super().__init__(None, left, right)
        if left is None or right is None:
            raise RuntimeError(
                f"Tried to create a JointNode that didn't have both children. {left =}, {right = }")

    def __str__(self):
        result = ""
        if self.has_left():
            result += self.left.__str__()
        if self.has_right():
            result += self.right.__str__()
        return result

    def __repr__(self):
        result = ""
        if self.has_left():
            result += self.left.__repr__()
        if self.has_right():
            result += self.right.__repr__()
        return result

    def string_of_tree(self, indentation_level: int = 0) -> str:
        """
        Builds a string to visualize this subtree.
        :param indentation_level: number of tabs before this line and its children
        :return: string describing this node and its children.
        """
        output = ""
        if self.has_left():
            output += self.left.string_of_tree(indentation_level + 1)
        output += f"{' ' * (4 * indentation_level)}<\n"
        if self.has_right():
            output += self.right.string_of_tree(indentation_level + 1)
        return output
