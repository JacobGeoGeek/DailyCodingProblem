import unittest
from Node import Node
from challenge3 import deserialize, serialize


class TestChallenge(unittest.TestCase):

    def test_exemple_from_challenge(self):
        node = Node('root', Node('left', Node('left.left')), Node('right'))

        self.assertEqual(deserialize(
            serialize(node)).left.left.val, "left.left")
