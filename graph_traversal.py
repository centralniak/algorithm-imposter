from typing import Optional, Any, Callable


class BinaryNode:

    left: Optional['BinaryNode'] = ...
    right: Optional['BinaryNode'] = ...
    attributes: Any = ...

    def __init__(self, left: Optional['BinaryNode'] = None, right: Optional['BinaryNode'] = None, attributes: Any = None):
        self.left = left
        self.right = right
        self.attributes = attributes

    @property
    def is_leaf(self):
        return self.left is None and self.right is None


def recursive_traverse(root: BinaryNode, callable: Callable[[BinaryNode], Any]):
    if callable is not None:
        callable(root)
    if root.is_leaf:
        return
    recursive_traverse(root.left, callable)
    recursive_traverse(root.right, callable)
