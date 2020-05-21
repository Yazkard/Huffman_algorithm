class Node:
    def __init__(self, left_child=None, right_child=None, value=None, probability=0, values=None): ##dla liscia podajemy value i porbability, dla node right i lfet child i values
        self.left_child = left_child
        self.right_child = right_child
        if left_child is not None and right_child is not None:
            self.probability = left_child.probability + right_child.probability
        else:
            self.probability = probability
        self.value = value
        if value is not None:
            self.values = [value]
        else:
            self.values = values
