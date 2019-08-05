from functools import partial
from typing import Any, Callable, Optional, Type


class BinaryNode:

    left: Optional['BinaryNode'] = ...
    right: Optional['BinaryNode'] = ...
    attributes: Any = ...

    def __init__(self, left: Optional['BinaryNode'] = None, right: Optional['BinaryNode'] = None, attributes: Any = None):
        self.left = left
        self.right = right
        self.attributes = attributes

    def __repr__(self):
        return str(self.attributes)

    @property
    def is_leaf(self):
        return self.left is None and self.right is None


class GraphCollection(list):

    def __iter__(self):  # list.__iter__ does not return self by default!
        return self

    def __next__(self):
        raise NotImplementedError


class Stack(GraphCollection):

    def __next__(self):
        if not self:
            raise StopIteration
        return self.pop()


class FIFOQueue(GraphCollection):

    def __next__(self):
        if not self:
            raise StopIteration
        return self.pop(0)


def recursive_traverse(root: BinaryNode, callable: Optional[Callable[[BinaryNode], Any]]):
    if callable is not None:
        callable(root)
    if root.is_leaf:
        return
    recursive_traverse(root.left, callable)
    recursive_traverse(root.right, callable)


def incremental_traverse(
    root: BinaryNode,
    callable: Callable[[BinaryNode], Any],
    collection_class: Type[GraphCollection],
    updater: Callable[[GraphCollection, BinaryNode, BinaryNode], GraphCollection]
):
    stack = collection_class([root])
    while stack:
        current_binary_node = next(stack)
        if callable is not None:
            callable(current_binary_node)
        if current_binary_node.is_leaf:
            continue
        stack = updater(stack, current_binary_node.left, current_binary_node.right)


def depth_first_update(stack: Stack, left: BinaryNode, right: BinaryNode) -> Stack:
    stack.append(right)
    stack.append(left)
    return stack


def breadth_first_update(fifo_queue: FIFOQueue, left: BinaryNode, right: BinaryNode) -> FIFOQueue:
    fifo_queue.append(left)
    fifo_queue.append(right)
    return fifo_queue


depth_first_traverse = partial(incremental_traverse, collection_class=Stack, updater=depth_first_update)
breadth_first_traverse = partial(incremental_traverse, collection_class=FIFOQueue, updater=breadth_first_update)
