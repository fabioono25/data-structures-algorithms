// linear search definition: go through each element in the array and check if it's the element we're looking for
// time complexity: O(n) - linear time
// space complexity: O(1) - constant space

var beasts = ['Centaur', 'Godzilla', 'Mosura', 'Minotaur', 'Hydra', 'Nessie'];

beasts.indexOf('Godzilla'); // 1 - using linear search

beasts.findIndex(function(item){
  return item === 'Godzilla';
}); // 1 - using findIndex

beasts.find(function(item){
  return item === 'Godzilla';
}); // 'Godzilla' - using find

beasts.includes('Godzilla'); // true - using includes

function linearSearch(array, item) {
  for (let i = 0; i < array.length; i++) {
    if (array[i] === item) return i;
  }
  return null;
}

console.log('linear search: ', beasts);
console.log(linearSearch(beasts, 'Godzilla'));
console.log(linearSearch(beasts, 'Hydra'));
console.log(linearSearch(beasts, 'Mothra'));
