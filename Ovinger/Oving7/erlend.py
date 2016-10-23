#!/usr/bin/python3

from sys import stdin
from collections import defaultdict
max_values = defaultdict(lambda: [None])
num_of_calls = 0

# def extend_table(row, column):
    # global max_values
    # max_values = map(lambda x: x + ([0] * (column - len(x))), max_values + ([[0] * column] * (row - len(max_values))))


def recursive_find_value(widths, heights, values, paper_width, paper_height):
    global num_of_calls
    highest_value = 0
    if max_values[paper_height][paper_width] != None:
        num_of_calls += 1
        return max_values[paper_height][paper_width]

    for i in range(len(widths)):
        #Test each orientation, with both vertical and horizontal cuts for all bills.
        if widths[i] <= paper_width and heights[i] <= paper_height:
            this_value = recursive_find_value(widths, heights, values, paper_width - widths[i], paper_height) \
                         + values[i] + recursive_find_value(widths, heights, values, widths[i], paper_height - heights[i])
            if this_value > highest_value:
                highest_value = this_value
        if widths[i] <= paper_height and heights[i] <= paper_width:
            this_value = recursive_find_value(widths, heights, values, paper_width - heights[i], paper_height) \
                         + values[i] + recursive_find_value(widths, heights, values, heights[i], paper_height - widths[i])
            if this_value > highest_value:
                highest_value = this_value
        if heights[i] <= paper_height and widths[i] <= paper_width:
            this_value = recursive_find_value(widths, heights, values, paper_width, paper_height - heights[i]) \
                         + values[i] + recursive_find_value(widths, heights, values, paper_width - widths[i], heights[i])
            if this_value > highest_value:
                highest_value = this_value
        if heights[i] <= paper_width and widths[i] <= paper_height:
            this_value = recursive_find_value(widths, heights, values, paper_width, paper_height - widths[i]) \
                         + values[i] + recursive_find_value(widths, heights, values, paper_width - heights[i], widths[i])
            if this_value > highest_value:
                highest_value = this_value
    max_values[paper_height][paper_width] = highest_value
    return highest_value


def max_value(widths, heights, values, paper_width, paper_height):
    # global max_values
    # max_values = None
    # # SKRIV DIN KODE HER
    # if max_values is None:
        # max_values = []
        # for i in range(paper_height + 1):
            # max_values.append([])
            # for j in range(paper_width + 1):
                # max_values[i].append(None)
    # if len(max_values) <= paper_height:
        # extend_table(paper_height+1, paper_width+1)
    # if len(max_values[0]) <= paper_width:
        # extend_table(paper_height+1, paper_width+1)

    return recursive_find_value(widths, heights, values, paper_width, paper_height)


def main():
    widths = []
    heights = []
    values = []
    for triple in stdin.readline().split():
        dim_value = triple.split(':', 1)
        dim = dim_value[0].split('x', 1)
        width = int(dim[0][1:])
        height = int(dim[1][:-1])
        value = int(dim_value[1])
        widths.append(int(width))
        heights.append(int(height))
        values.append(int(value))
    for line in stdin:
        paper_width, paper_height = [int(x) for x in line.split('x', 1)]

        print((max_value(widths, heights, values, paper_width, paper_height)))
        print(num_of_calls)


if __name__ == "__main__":
    main()