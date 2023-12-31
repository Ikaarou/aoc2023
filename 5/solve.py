def find_lowest_location(seeds, almanac):
    lowest_location = None
    for seed in seeds:
        current_value = seed
        for i in range(7):
            for source_range in almanac[i]:
                source_start, destination_start, range_length = source_range
                if (current_value >= source_start and current_value < (source_start + range_length)):
                    current_value = destination_start + (current_value - source_start)
                    break
        if (lowest_location is None or current_value < lowest_location):
            lowest_location = current_value
    return lowest_location

def find_lowest_location_with_range(seeds_with_range, almanac):
    current_step_values = []
    for seed_start, seed_range in seeds_with_range:
        current_step_values.append((seed_start, seed_start + seed_range - 1))
    
    next_values = []
  
    for step in almanac:
        current_step_values = next_values + current_step_values
        next_values = []
        for transform in almanac[step]:
            source_start, destination_start, range_length = transform
            source_end = source_start + range_length
            transformation = destination_start - source_start
            no_transformations = []

            for start, end in current_step_values:                    
                # Intersection start
                if (source_start >= start and source_start <= end and source_end > end):
                    next_values.append((source_start + transformation, end + transformation))
                    no_transformations.append((start, source_start - 1))
                    continue
                # Intersection end
                if (source_start <= start and source_end > start and end > source_end):
                    next_values.append((start + transformation, source_end + transformation))
                    no_transformations.append((source_end +1 , end))
                    continue
                # Contained inside target
                if (start >= source_start and source_end > end):
                    next_values.append((start + transformation, end + transformation))
                    continue
                # target contained inside source
                if (start <= source_start and source_end < end):
                    no_transformations.append((start, source_start - 1))
                    no_transformations.append((source_end, end))
                    next_values.append((source_start + transformation, source_end + transformation))
                    continue
                no_transformations.append((start, end))
            current_step_values = no_transformations

    current_step_values = next_values + current_step_values
    return min(list(map(lambda csv: csv[0], current_step_values)))

def solve():
    f = open("input", "r")
    almanac = {}
    step = -1
    seeds = []
    for i, line in enumerate(f.readlines()):
        line = line.rstrip()
        if (line == ''):
            continue
        if (i == 0):
            seeds = list(map(lambda n: int(n),line.split()[1::]))
        elif ':' in line:
            step += 1
        else:
            destination_start, source_start, range_length = list(map(lambda n: int(n), line.split()))
            if step not in almanac:
                almanac[step] = []
            almanac[step].append([source_start, destination_start, range_length])
    seeds_with_range = [seeds[i:i + 2] for i in range(0, len(seeds), 2)]

    return find_lowest_location(seeds, almanac), find_lowest_location_with_range(seeds_with_range, almanac)

print('Results', solve())