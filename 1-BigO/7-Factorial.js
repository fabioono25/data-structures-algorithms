// examples of a Factorial Time Complexity O(n!)

// O(n!) - Factorial Time Complexity

// example 1: generating permutations in O(n!)
// O(n!) + O(n!) = O(n!)
const example1 = (arr) => {
  if (!arr.length) return [[]];
  const first = arr.shift();
  const perms = example1(arr);
  const totalPerms = [];
  perms.forEach((perm) => {
    for (let i = 0; i <= perm.length; i++) {
      const newPerm = [...perm.slice(0, i), first, ...perm.slice(i)];
      totalPerms.push(newPerm);
    }
  });
  return totalPerms;
};

// example 2: generating subsets in O(n!)
// O(n!) + O(n!) = O(n!)
const example2 = (arr) => {
  if (!arr.length) return [[]];
  const first = arr.shift();
  const subsets = example2(arr);
  const newSubsets = subsets.map((subset) => [first, ...subset]);
  return [...subsets, ...newSubsets];
};

// example 3: brute-force for Traveling Salesman Problem in O(n!)
// O(n!) + O(n!) = O(n!)
function calculateTotalDistance(path, graph) {
  // Calculate total distance for the given path using graph information
}

function generateAllPermutations(cities) {
  // Generate all permutations of cities
}

function bruteForceTSP(cities, graph) {
  const permutations = generateAllPermutations(cities);
  let minDistance = Infinity;
  let optimalPath = [];

  for (const permutation of permutations) {
      const distance = calculateTotalDistance(permutation, graph);
      if (distance < minDistance) {
          minDistance = distance;
          optimalPath = permutation;
      }
  }

  return { path: optimalPath, distance: minDistance };
}

// example 4: Brute-Force Algorithm for Subset Sum Problem
function isSubsetSum(set, n, target) {
  if (target === 0) {
      return true;
  }
  if (n === 0 && target !== 0) {
      return false;
  }
  if (set[n - 1] > target) {
      return isSubsetSum(set, n - 1, target);
  }
  return isSubsetSum(set, n - 1, target) || isSubsetSum(set, n - 1, target - set[n - 1]);
}

console.log("example1([1, 2, 3]): ", example1([1, 2, 3]));
console.log("example2([1, 2, 3]): ", example2([1, 2, 3]));
console.log("bruteForceTSP([1, 2, 3]): ", bruteForceTSP([1, 2, 3]));

const cities = [1, 2, 3];
const graph = {
    1: { 2: 10, 3: 15 },
    2: { 1: 10, 3: 20 },
    3: { 1: 15, 2: 20 }
};
const result = bruteForceTSP(cities, graph);
console.log("Optimal TSP Path:", result.path);
console.log("Total Distance:", result.distance);

console.log("isSubsetSum([1, 2, 3]): ", isSubsetSum([1, 2, 3]));
const inputSet = [3, 34, 4, 12, 5, 2];
const targetSum = 9;
const isSubsetPossible = isSubsetSum(inputSet, inputSet.length, targetSum);
console.log(`Subset with sum ${targetSum} exists: ${isSubsetPossible}`);