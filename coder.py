from tree import Node
import binascii


def create_probability_list(f):
    letters = {}
    counter = 0
    for line in f:
        if len(line) > 0:
            for l in line:
                counter += 1
                if l in letters:
                    letters[l] += 1
                else:
                    letters[l] = 1
    for k in letters:
        letters[k] = letters[k]/counter
    nodes = []
    for y in letters:
        n = Node(value=y, probability=letters[y])
        nodes.append(n)
    return nodes


def create_tree(nodes):
    while len(nodes) > 1:
        indexes = find_smallest_two(nodes)
        values = []
        if nodes[indexes[0]].values is not None:
            values.extend(nodes[indexes[0]].values)
        else:
            values.append(nodes[indexes[0]].value)

        if nodes[indexes[1]].values is not None:
            values.extend(nodes[indexes[1]].values)
        else:
            values.append(nodes[indexes[1]].value)

        n = Node(left_child=nodes[indexes[0]], right_child=nodes[indexes[1]], values=values)
        nodes.append(n)
        if indexes[0] > indexes[1]:
            nodes.pop(indexes[0])
            nodes.pop(indexes[1])
        else:
            nodes.pop(indexes[1])
            nodes.pop(indexes[0])
    return nodes[0]


def find_smallest_two(nodes):
    probability = [1, 1]
    index = [0, 1]
    for i in range(len(nodes)):
        if nodes[i].probability < probability[1]:
            if nodes[i].probability < probability[0]:
                probability[1] = probability[0] #przesun pierwszy element
                index[1] = index[0]

                index[0] = i
                probability[0] = nodes[i].probability
            else:
                index[1] = i
                probability[1] = nodes[i].probability
    return index


def get_code(letter, tree):
    node = tree
    code = ""
    while True:
        if node.value is None:
            if letter in node.right_child.values:
                code += '1'
                node = node.right_child
            else:
                code += '0'
                node = node.left_child
        else:
            if node.value == letter:
                return code


def encode(f, tree):
    code = ""
    for line in f:
        if len(line) > 0:
            for l in line:
                code += get_code(l, tree)
    n = int(code, 2)
    x = n.to_bytes((n.bit_length() + 7) // 8, 'big')
    return x


def decode(f, tree):

    x = bin(int(binascii.hexlify(f.read()), 16))
    x = x[0] + x[2:]
    t = get_decoded_string(x, tree)
    return t


def get_decoded_string(bits, tree):
    node = tree
    text = ""
    i=0
    end = len(bits)
    while i < end:
        if node.value is None:
            if bits[i] == "1":
                node = node.right_child
            else:
                node = node.left_child
            i+=1
        else:
            text += node.value
            node = tree
            continue
    return text

