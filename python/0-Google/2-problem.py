""" 
!   Design a class:
!       1. Inserting a value (no duplicates)
!       2. Removing a value
!       3. GetRandom a value that is already inserted (with equal probability)
!           a. random.choice(list)
"""

import random


class Store:
    def __init__(self):
        self.values = []
        self.map = {}

    def insert(self, value):
        if value in self.map:
            return

        self.values.append(value)
        self.map[value] = len(self.value)-1

    def remove(self, value):
        if value not in self.map:
            return

        index = self.map[value]

        # Swapping
        last_val = self.values[-1]
        self.values[value] = len(self.values)-1
        self.map[last_val] = index

        self.values.pop()
        del self.map[value]

    def get_random(self):
        return random.choice(list(self.values))


if __name__ == "__main__":
    obj = Store()
    obj.insert(3)
    obj.insert(4)

    print(obj)
