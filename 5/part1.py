input_data = open('5/input.txt').read()

split_data = input_data.split('\n\n')

ordering = split_data[0].split('\n')
pages = split_data[1].split('\n')

order_map = {}

for order in ordering:
    x, y = [int(i) for i in order.split('|')]

    if x in order_map:
        order_map[x].add(y)
    else:
        order_map[x] = set([y])

total = 0

for page in pages:
    numbers = [int(i) for i in page.split(',')]

    valid = True

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[j] not in order_map.get(numbers[i], set()):
                valid = False
                break
        
        if not valid:
            break
    
    if valid:
        total += numbers[len(numbers) // 2]

print(total)
