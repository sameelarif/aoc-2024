input_data = open('5/input.txt').read()

split_data = input_data.split('\n\n')

ordering = split_data[0].split('\n')
pages = split_data[1].split('\n')

order_map = {}
all_involved_pages = set()

for order in ordering:
    x, y = [int(i) for i in order.split('|')]

    if x in order_map:
        order_map[x].add(y)
    else:
        order_map[x] = set([y])

    all_involved_pages.add(x)
    all_involved_pages.add(y)

def is_valid_update(numbers):
    pos = {n: i for i, n in enumerate(numbers)}

    for x in numbers:
        if x in order_map:
            for y in order_map[x]:
                if y in pos and x in pos:
                    if pos[x] > pos[y]:
                        return False
    return True

def toposort(numbers):
    nums_set = set(numbers)

    graph = {n: set() for n in numbers} 
    in_degree = {n: 0 for n in numbers}

    for x in numbers:
        if x in order_map:
            for y in order_map[x]:
                if y in nums_set:
                    graph[x].add(y)

    in_degree = {n: 0 for n in numbers}

    for x in graph:
        for y in graph[x]:
            in_degree[y] += 1

    queue = [n for n in numbers if in_degree[n] == 0]
    topo_order = []

    while queue:
        node = queue.pop()
        topo_order.append(node)

        for conn in graph[node]:
            in_degree[conn] -= 1

            if in_degree[conn] == 0:
                queue.append(conn)

    return topo_order

total = 0
for page_line in pages:
    numbers = [int(i) for i in page_line.split(',')]
    if not is_valid_update(numbers):
        corrected = toposort(numbers)
        total += corrected[len(corrected) // 2]

print(total)
