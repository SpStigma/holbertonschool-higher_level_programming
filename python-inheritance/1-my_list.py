#!/usr/bin/python3

""" module 1-my_list """


class MyList(list):
    def print_sorted(self):
        """
        Print the elements of the list in sorted order.

        This method sorts the elements of the list in
        ascending order and prints them.

        Parameters:
            None

        Returns:
            None
        """
        print(sorted(self))
