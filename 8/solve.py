from math import lcm

def find_path(sequence, nodes_hash, node = 'AAA'):
    steps = 0
    while True:
        sequence_direction = sequence[steps % len(sequence)]
        if node[2] == 'Z' and steps != 0:
            break
        steps += 1
        direction = (0 if sequence_direction == 'L' else 1)
        node = nodes_hash[node][direction]

    return steps


def solve():
    f = open("input", "r")
    sequence = ''
    nodes_hash = {}
    for i, line in enumerate(f.readlines()):
        line = line.rstrip()
        if i == 0:
            sequence = line
        elif line == '':
            continue
        else:
            node_key, left_node, right_node = line[0:3], line[7:10], line[12:15]
            nodes_hash[node_key] = (left_node, right_node) 
    # path_total_part_1 = find_path(sequence, nodes_hash)

    paths = []

    for node in nodes_hash:
        if node[2] == 'A':
            paths.append(find_path(sequence, nodes_hash, node))

    return paths[0], lcm(*paths)
 
print('Results', solve())