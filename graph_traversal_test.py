from pytest import fixture

from graph_traversal import BinaryNode, recursive_traverse, depth_first_traverse, Stack, FIFOQueue


@fixture
def graph():
    yield BinaryNode(
        BinaryNode(
            BinaryNode(attributes=3),
            BinaryNode(attributes=4),
            1
        ),
        BinaryNode(
            BinaryNode(attributes=5),
            BinaryNode(attributes=6),
            2
        ),
        0
    )


def test_stack():
    stack = Stack()
    stack.append(1)
    stack.append(2)
    assert list(stack) == [2, 1]


def test_fifo_queue():
    queue = FIFOQueue()
    queue.append(1)
    queue.append(2)
    assert list(queue) == [1, 2]


def test_binary_node_is_leaf():
    root = BinaryNode(
        BinaryNode(),
        BinaryNode()
    )
    assert not root.is_leaf
    assert root.left.is_leaf
    assert root.right.is_leaf


def test_recursive_traverse(graph):
    order = []
    recursive_traverse(graph, lambda bn: order.append(bn.attributes))
    assert order == [0, 1, 3, 4, 2, 5, 6]


def test_depth_first_traverse(graph):
    order = []
    depth_first_traverse(graph, lambda bn: order.append(bn.attributes))
    assert order == [0, 1, 3, 4, 2, 5, 6]
