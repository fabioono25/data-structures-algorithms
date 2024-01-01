# Hash Tables: are used to store key-value pairs.
# Hash Tables are fast for finding, adding and removing values.
# Hash Tables are unordered.
# Hash Tables are called Dictionaries in Python.
# Operations: Insert, Lookup, Delete, Search

class HashTable:
    def __init__(self, size):
        self.data = [None] * size

    def _hash(self, key):
        hash_value = 0
        for i in range(len(key)):
            hash_value = (hash_value + ord(key[i]) * i) % len(self.data)
        return hash_value

    def set(self, key, value):
        address = self._hash(key)
        if not self.data[address]:
            self.data[address] = []
        self.data[address].append([key, value])
        return self.data

    def get(self, key):
        address = self._hash(key)
        current_bucket = self.data[address]
        print(current_bucket)

        if current_bucket:
            for i in range(len(current_bucket)):
                if current_bucket[i][0] == key:
                    return current_bucket[i][1]
        return None

    def keys(self):
        if not self.data:
            return None
        result = []
        for i in range(len(self.data)):
            if self.data[i] and len(self.data[i]) > 0:
                if len(self.data[i]) > 1:
                    for j in range(len(self.data[i])):
                        result.append(self.data[i][j][0])
                else:
                    result.append(self.data[i][0][0])
        return result


myHashTable = HashTable(10)
myHashTable.set("grapes", 1000)  # [['grapes', 1000]]
myHashTable.set("bananas", 20)
myHashTable.set("apples", 2)
print(myHashTable.data)
print(myHashTable.get("grapes"))
print(myHashTable.keys())
