# Connor Robinson 6/2/2019
# Faculty mentor - David Brown
# Ithaca College Summer Scholars Program
import itertools
import matplotlib.pyplot as plt
import math

"""
This function generates a list of all possible L‐tuples of elements from list, named alphabet.
"""


def make_tuples(alphabet, L):
    all_tuples = []
    for i in range(L):
        one_size_tuple = list(itertools.product(alphabet, repeat=i+1))
        for j in range(len(one_size_tuple)):
            all_tuples.append(one_size_tuple[j])
    return all_tuples


"""
This function creates  a pruned list of all tuples with a given alphabet, up to a given length L, 
that do not contain the forbidden substring
currently, this function makes a list of all possible combinations, stored as lists of strings
"""


def make_pruned_list(alphabet, L, forbidden):
    all_tuples = make_tuples(alphabet, L)
    all_tuples_strings = []
    pruned_tuples_strings = []
    pruned_tuples_as_lists = []
    forbidden_str = str(forbidden)
    # converts all tuples to strings
    for i in range(len(all_tuples)):
        single_tuple_string = ''.join(map(str, all_tuples[i]))
        all_tuples_strings.append(single_tuple_string)

    # removes all tuples/strings with the forbidden sequence
    for i in range(len(all_tuples_strings)):
        if forbidden_str not in all_tuples_strings[i]:
            pruned_tuples_strings.append(all_tuples_strings[i])

    # converts all strings to tuples
    for i in range(len(pruned_tuples_strings)):
        single_tuple_list = list(pruned_tuples_strings[i])
        pruned_tuples_as_lists.append(single_tuple_list)
    return pruned_tuples_as_lists


"""
this function returns the x,y position of a unique fractal address given the angle, ratio, and address
"""


def get_x_y_position(theta, r, fractal_address, alphabet):
    x_position = 0
    y_position = 1
    num_squared = 1
    d = 0
    for i in range(len(fractal_address)):

        ratio = r**num_squared
        if fractal_address[i] == alphabet[0]:
            d += 1
            x_position += ratio * math.sin(theta * d)
        else:
            d -= 1
            x_position += ratio * math.sin( theta * d)
        y_position += ratio * math.cos(theta * d)
        num_squared += 1

    return x_position, y_position

"""
This function draws the line leading to the point described in the fractal address, given the angle, ratio, and address
"""


def draw_root_line(theta, r, fractal_address, alphabet):
    x_tip, y_tip = get_x_y_position(theta, r, fractal_address, alphabet)
    root_list_size = len(fractal_address)-1
    x_root, y_root = get_x_y_position(theta, r, fractal_address[:root_list_size], alphabet)
    return x_root, x_tip, y_root, y_tip


"""
This function creates pruned fractal trees with two branches with a given angle, ratio,
number of iterations, and forbidden sequence.

This does this with the following steps:
    -Create all combinations of lists from size 1 to the given size with a given two character alphabet
    -Remove all combinations with the forbidden sequence
    -For each combination, generate the two points that create the line leading up to that point
        -This is done by finding the coordinate for the combination, as well as the coordinate
            for the combination without the last element, and drawing a line between the two coordinates
    This draws the tree
    
    To draw the canopy, we display all of the coordinate points that have the maximum size. 
"""


def generate_two_branch_fractal_tree(alphabet, forbidden, size, theta, r):

    allowed_addresses = make_pruned_list(alphabet, size, forbidden)
    for i in range(len(allowed_addresses)):
        x1, x2, y1, y2 = draw_root_line(theta, r, allowed_addresses[i], alphabet)
        plt.plot([x1, x2], [y1, y2], 'k')
        # plt.plot(x2, y2, "ro")
    plt.plot([0, 0], [1, 0], 'k')
    plt.show()


"""
This function does the same thing as the previous function, except only returns the fractal (tips of the tree)
"""


def generate_two_branch_fractal_tips(alphabet, forbidden, size, theta, r):
    allowed_addresses = make_pruned_list(alphabet, size, forbidden)
    for i in range(len(allowed_addresses)):
        if len(allowed_addresses[i]) == size:
            x1, x2, y1, y2 = draw_root_line(theta, r, allowed_addresses[i], alphabet)
            plt.plot(x2, y2, ",k")
    plt.show()


def main():
    alphabet = ['1', '2']
    forbidden = 112
    size =11
    theta = math.pi / 2
    r = .7071
    generate_two_branch_fractal_tips(alphabet, forbidden, size, theta, r)
    generate_two_branch_fractal_tree(alphabet, forbidden, size, theta, r)


main()

#end of code