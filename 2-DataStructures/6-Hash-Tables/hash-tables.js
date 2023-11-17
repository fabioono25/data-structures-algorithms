// Hash Tables - Definition: A data structure that stores values by key, unlike an array that stores values by index.
// What more: Hash tables are fast for all of the following operations: finding values, adding new values, and removing values!
//  - Hash tables are collections of key-value pairs
//  - Hash tables can find values quickly given a key
//  - Hash tables can add new key-values quickly

let user = {
  age: 54,
  name: "Kylie",
  magic: true,
  scream: function () {
    console.log("ahhhhh!");
  },
};

user.age; // O(1)
user.spell = "abra kadabra"; // O(1)
user.scream(); // O(1)

// implementing hash tables:
class HashTable {
  constructor(size) {
    this.data = new Array(size);
  }

  _hash(key) {
    let hash = 0;
    for (let i = 0; i < key.length; i++) {
      hash = (hash + key.charCodeAt(i) * i) % this.data.length;
    }
    return hash;
  }

  set(key, value) {
    let address = this._hash(key);
    if (!this.data[address]) {
      this.data[address] = [];
    }
    this.data[address].push([key, value]);
    return this.data;
  }

  get(key) {
    let address = this._hash(key);
    const currentBucket = this.data[address];
    console.log(currentBucket);

    if (currentBucket.length) {
      for (let i = 0; i < currentBucket.length; i++) {
        if (currentBucket[i][0] === key) {
          return currentBucket[i][1];
        }
      }
    }
    return undefined;
  }
}

const myHashTable = new HashTable(10);
myHashTable.set("grapes", 1000); // [['grapes', 1000]]
myHashTable.set("bananas", 20);
myHashTable.set("apples", 2);
console.log(myHashTable);
console.log(myHashTable.get("grapes"));
