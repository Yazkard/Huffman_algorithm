from coder import *

with open('file.txt') as file:
    nodes_list = create_probability_list(file)

tree = create_tree(nodes=nodes_list)

with open('file.txt') as file:
    encoded = encode(file, tree)

with open('encoded_file.txt', 'wb') as file:
    file.write(encoded)

with open('encoded_file.txt', 'rb') as file:
    decoded = decode(file, tree)

with open('decoded_file.txt', 'w') as file:
    file.write(decoded)



