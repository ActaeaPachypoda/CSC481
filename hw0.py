"""
Sarah Fondots
8/29/2018
hw0.py
CSC 481
"""

# Function declarations
def my_rotate(the_list):
    """Takes a list, pops off the first element and adds it to the end of the list
    returning the resulting list."""

    # CODE GOES HERE

def my_rotate_n(n, the_list):
    """Takes a number n and a list and performs the my_rotate function n times"""

    #CODE GOES HERE

def first_sat(first_list, second_list, foo):
    """Takes two lists and a function foo as arguments.
     Function foo should take two arguments and return a boolean.
     The result of a call to first_sat should be a list containing the first pair of
    arguments that satisfies (returns True) from foo."""
    # YOU FILL THIS IN
def my_remove(the_char, the_list):
    """Takes a character and a list as input and returns a list with all instances
     of the character removed (including recursive instances)."""
    # YOU FILL THIS IN

def palindromep(the_list):
    """Takes a list as input and returns True if the list is a palindrome and False
   otherwise."""
    # YOU FILL THIS IN
    return True
def main():
    """ Calling the functions. """
    print(my_rotate(['a', 'b', 'c']))
    print(my_rotate_n(3,['a', 'b', 'c', 'd']))
    print(first_sat([1, 4, 3, 5], [2, 5, 1, 4]), (lambda  x, y: x>y))
    print(my_remove('b', ['a', 'b', 'c', 'd']))
    print(palindromep(['b', 'c', 'c', 'b']))

if __name__ == '__main__':
    main()
