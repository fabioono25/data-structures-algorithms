// Understando how the built-in algorithm is implemented in each language:

// sorting wrong in JS:

const basket = [1, 65, 34, 2, 1, 4, 8, 7];

// because it sorts by converting the elements to strings and comparing their UTF-16 code units values
console.log(basket.sort()); // [ 1, 1, 2, 34, 4, 65, 7, 8 ]

console.log('34'.charCodeAt(0)); // 51
console.log('7'.charCodeAt(0));  // 55

// using sorting in the correct way
console.log(basket.sort((a, b) => a - b)); // [ 1, 1, 2, 4, 7, 8, 34, 65 ]

const spanishWords = ['único', 'árbol', 'cosas', 'fútbol'];
console.log(spanishWords.sort()); // [ 'cosas', 'fútbol', 'árbol', 'único' ]

// using sorting in the correct way
console.log(spanishWords.sort((a, b) => a.localeCompare(b))); // [ 'árbol', 'cosas', 'fútbol', 'único' ]