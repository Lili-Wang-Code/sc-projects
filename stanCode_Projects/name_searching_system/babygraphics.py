"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

This file will let the user to find out the rank of baby
names from 1900-2010 on a canvas, by drawing the trend line
and the name with the rank.
If the rank of the baby name is out of the 1000th, it will
show '*' on the canvas.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue', 'magenta']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    draw_area = width-GRAPH_MARGIN_SIZE*2
    num_year = len(YEARS)
    avg_area = draw_area // num_year
    x_coordinate = GRAPH_MARGIN_SIZE + avg_area * year_index
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    # the upper line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       (CANVAS_WIDTH-GRAPH_MARGIN_SIZE), GRAPH_MARGIN_SIZE,
                       fill='black', width=LINE_WIDTH)
    # the lower line
    canvas.create_line(GRAPH_MARGIN_SIZE, (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE),
                       (CANVAS_WIDTH-GRAPH_MARGIN_SIZE), (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE),
                       fill='black', width=LINE_WIDTH)
    # the vertical line and word(year)
    for i in range(len(YEARS)):
        x_coordinate = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x_coordinate, 0, x_coordinate, CANVAS_HEIGHT, fill='black', width=LINE_WIDTH)
        canvas.create_text((x_coordinate+TEXT_DX), (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE+TEXT_DX),
                           text=YEARS[i], anchor=tkinter.NW, fill='black')


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    avg_y = (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2) / MAX_RANK  # the average area of 1 rank in vertical
    previous_x = 0
    previous_y = 0
    count = 0  # count for the color
    for name in lookup_names:
        # set the color for word and line
        color = COLORS[count]
        count += 1
        if count == len(COLORS):  # go back to the first color
            count = 0
        target_year_rank = name_data[name]  # dict(year:rank)
        for i in range(len(YEARS)):  # find the rank from 1900-2010
            year = str(YEARS[i])
            x = get_x_coordinate(CANVAS_WIDTH, i)
            if year in target_year_rank:  # find the rank to set the vertical position on the canvas
                rank = int(target_year_rank[year])
                if rank == 1:  # the first rank
                    y = GRAPH_MARGIN_SIZE
                else:  # the second - 1000th rank
                    y = GRAPH_MARGIN_SIZE + rank * avg_y
            else:  # >1000th rank represents '*'
                rank = '*'
                y = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
            canvas.create_text(x+TEXT_DX, y, anchor=tkinter.SW, text=name + ' ' + str(rank), fill=color)
            if i == 0:
                previous_x = x
                previous_y = y
            else:  # draw the line between the current and previous year
                canvas.create_line(previous_x, previous_y, x, y, fill=color, width=LINE_WIDTH)
                previous_x = x
                previous_y = y


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
