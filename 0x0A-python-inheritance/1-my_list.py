#!/usr/bin/python3

"""
print_sorted module
"""
class MyList(list):
    """A class that inherits from list"""
    pass

    def print_sorted(self):
        """Prints the list in sorted order (ascending sort)."""
        print(sorted(self))
