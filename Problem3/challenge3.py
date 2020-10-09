from Node import Node


def serialize(root):
    if root == None:
        return "null"

    leftSerialize = serialize(root.left)
    rightSerialize = serialize(root.right)

    return str(root.val) + "," + leftSerialize + "," + rightSerialize


def deserialize(s):
    listValues = s.split(",")
    return deserializeList(listValues)


def deserializeList(listValues):
    value = listValues.pop(0)
    if value == "null":
        return None
    node = Node(value, deserializeList(listValues),
                deserializeList(listValues))
    return node


if __name__ == "__main__":
    node = Node('root', Node('left', Node('left.left')), Node('right'))

    print(deserialize(serialize(node)).left.left.val == "left.left")
