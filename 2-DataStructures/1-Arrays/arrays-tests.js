// 4 items in a 32 bits system = 16 bytes of storage
const arr1 = [1, 'b', 'c', 3]

arr1.push('dd'); // O(1) - adding at the end of the array

arr1.pop(); // O(1) - removing at the end of the array
arr1.pop();

arr1.unshift('aa'); // O(n) - adding at the beginning of the array
arr1.unshift('bb');
arr1.shift(); // O(n) - removing at the beginning of the array

arr1.splice(2, 0, 'cc'); // O(n) - inserting at a specific index

console.log('arr1: ', arr1);
console.log('arr1[2]: ', arr1[2]); // O(1) - accessing an element by index

// JS, Python (lists), Java (ArrayLists) - Dynamic Arrays
// C, C++ - Static Arrays
// Dynamic arrays expand as you add more elements
// Static arrays have a fixed size

// implementing an array
class CustomizedArray {
  constructor() {
    this.length = 0;
    this.data = {};
  }

  get(index) {
    return this.data[index]
  }

  push(item) {
    this.data[this.length] = item;
    this.length++;
    return this.length;
  }

  pop() {
    delete this.data[this.length - 1];
    this.length--;
    return this.length;
  }

  delete(index) {
    this.removeItem(index);
    return this.data;
  }

  removeItem(index) {
    for (let i = index; i < this.length - 1; i++) {
      this.data[i] = this.data[i + 1]
    }
    delete this.data[this.length - 1];
    this.length--;
  }

  shiftItems(index) {
    for (let i = index; i < this.length - 1; i++) {
      this.data[i] = this.data[i + 1]
    }
  }
}

const arr2 = new CustomizedArray();
arr2.push('aaa');
arr2.push('bbb');
arr2.push('ccc');
arr2.push('ddd');
arr2.push('eee');
console.log('arr2: ', arr2);
console.log('arr2[1]: ', arr2.get(1));
arr2.pop();
console.log('arr2: ', arr2);
arr2.delete(1);
console.log('arr2: ', arr2);
arr2.shiftItems(1);
console.log('arr2: ', arr2);