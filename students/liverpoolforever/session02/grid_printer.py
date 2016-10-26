"""
grid_printer
"""
import sys
print("=============== PRINT A GRID =================================")

# Default no of rows and cols - corresponds to 3 rows and 3 cols
# no_of_rows = 11
# no_of_cols = 11

# Get rows and cols from the user -- other ways to do thi
no_of_rows = sys.argv[1]
no_of_cols = sys.argv[2]

# Convert to int
no_of_rows = int(no_of_rows)
no_of_cols = int(no_of_cols)

# declare the constants
PLUS_SYMBOL = '+'
HORIZONTAL_DASH = '-'
VERTICAL_DASH = '|'
BLANK_SPACE = " "
SPACING = 5

# returns the line with plus symbols
def get_plus_line(cols,line):

    for j in range(0,cols):
        if j % SPACING == 0:
            line = line + PLUS_SYMBOL
        else:
            line = line + HORIZONTAL_DASH
    return line

# returns the line without plus symbols
def get_blank_line(cols,line):

      for j in range(0,cols):
        if j % SPACING == 0:
            line = line + VERTICAL_DASH
        else:
            line = line + BLANK_SPACE
      return line

# main method which iterates the rows
def draw_a_grid(rows,cols):

    for i in range(0,rows):
        main_line = ""
        if i % SPACING == 0:
            main_line = get_plus_line(cols,main_line)
            print(main_line)
        else:
            main_line = get_blank_line(cols,main_line)
            print(main_line)


# Pass the number of rows and cols
draw_a_grid(no_of_rows,no_of_cols)