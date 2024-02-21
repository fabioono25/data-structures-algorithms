# Example 1: Generating permutations
def example1(arr):
    if not arr:
        return [[]]
    first = arr.pop(0)
    perms = example1(arr)
    total_perms = []
    for perm in perms:
        for i in range(len(perm) + 1):
            new_perm = perm[:i] + [first] + perm[i:]
            total_perms.append(new_perm)
    return total_perms

# Example 2: Generating subsets
def example2(arr):
    if not arr:
        return [[]]
    first = arr.pop(0)
    subsets = example2(arr)
    new_subsets = [([first] + subset) for subset in subsets]
    return subsets + new_subsets

# Example 3: Brute-force for Traveling Salesman Problem
def calculate_total_distance(path, graph):
    # Calculate total distance for the given path using graph information
    pass

def generate_all_permutations(cities):
    # Generate all permutations of cities
    pass

def brute_force_tsp(cities, graph):
    permutations = generate_all_permutations(cities)
    min_distance = float('inf')
    optimal_path = []

    for permutation in permutations:
        distance = calculate_total_distance(permutation, graph)
        if distance < min_distance:
            min_distance = distance
            optimal_path = permutation

    return {'path': optimal_path, 'distance': min_distance}

# Example 4: Brute-force algorithm for Subset Sum Problem
def is_subset_sum(set, n, target):
    if target == 0:
        return True
    if n == 0 and target != 0:
        return False
    if set[n - 1] > target:
        return is_subset_sum(set, n - 1, target)
    return is_subset_sum(set, n - 1, target) or is_subset_sum(set, n - 1, target - set[n - 1])

print("example1([1, 2, 3]): ", example1([1, 2, 3]))
print("example2([1, 2, 3]): ", example2([1, 2, 3]))
print("brute_force_tsp([1, 2, 3]): ", brute_force_tsp([1, 2, 3]))

cities = [1, 2, 3]
graph = {
    1: {2: 10, 3: 15},
    2: {1: 10, 3: 20},
    3: {1: 15, 2: 20}
}
result = brute_force_tsp(cities, graph)
print("Optimal TSP Path:", result['path'])
print("Total Distance:", result['distance'])

print("is_subset_sum([1, 2, 3]): ", is_subset_sum([1, 2, 3], 3, 9))
input_set = [3, 34, 4, 12, 5, 2]
target_sum = 9
is_subset_possible = is_subset_sum(input_set, len(input_set), target_sum)
print(f"Subset with sum {target_sum} exists: {is_subset_possible}")
