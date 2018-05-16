"""
In the classic problem of the Towers of Hanoi, you have 3 towers and N disks 
of different sizes which can slide onto any tower. The puzzle starts with disks 
sorted in ascending order of size from top to bottom (i.e., each disk sits on 
top of an even larger one). You have the following constraints:

1. Only one disk can be moved at a time.
2. A disk is slid off the top of one tower onto the next rod.
3. A disk can only be placed on top of a larger disk.

Write a program to move the disks from the first tower to the last using stacks.
"""


class Stack:
    def __init__(self):
        self.contents = []

    def is_empty(self):
        return self.contents == []

    def push(self, value):
        self.contents.append(value)

    def pop(self):
        return self.contents.pop()

    def peek(self):
        return self.contents[-1]

    def __str__(self):
        return str(self.contents)

    def __repr__(self):
        return str(self.contents)


class Tower:
    def __init__(self, index):
        self.disks = Stack()
        self.index = index

    def add(self, value):
        if not self.disks.is_empty() and self.disks.peek() <= value:
            print("Error placing disk: " + str(value))
        else:
            self.disks.push(value)

    def move_top_to(self, tower):
        top = self.disks.pop()
        tower.add(top)
        print("Move disk " + str(top) + " from " + str(self.index) + " to " + str(tower.index))

    def move_disks(self, n, destination, buffer):
        if n > 0:
            self.move_disks(n - 1, buffer, destination)
            self.move_top_to(destination)
            buffer.move_disks(n - 1, destination, self)

    def __repr__(self):
        return str(self.disks)

    def __str__(self):
        return str(self.disks)


# @param n integer representing the number of disks in the starting tower
def solve_tower_moves(n):
    towers = [Tower(i) for i in range(0, 3)]
    for i in range(n, 0, -1):
        towers[0].add(i)

    towers[0].move_disks(n, towers[2], towers[1])

    print(towers)


solve_tower_moves(3)
