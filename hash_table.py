class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, string: str) -> int:
        hashed:int = 0
        for character in string:
            hashed += ord(character)
        return hashed
        
    def add(self, key: str, value) -> None:
        key_hash = self.hash(key)
        if key_hash not in self.collection:
            self.collection[key_hash] = {}
        self.collection[key_hash][key] = value

    def remove(self, key: str) -> None:
        key_hash = self.hash(key)
        if key_hash in self.collection and key in self.collection[key_hash]:
            del self.collection[key_hash][key]
            if not self.collection[key_hash]:
                del self.collection[key_hash]

    def lookup(self, key: str):
        key_hash = self.hash(key)
        if key_hash in self.collection and key in self.collection[key_hash]:
            return self.collection[key_hash][key]
        return None
