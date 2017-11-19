#!/usr/bin/python
# -*- coding: utf-8 -*-

def check_line(line):
    for i in range(len(line) - 1):
        if line[i+1] == line[i]:
            return False
    return True
    
def check_grid(grid):
    for i in range(len(grid) - 1):
        if grid[i][0] == grid[i + 1][0]:
            return False
       
    for line in grid:
        if not check_line(line):
            return False
    return True
    
def golf(cube):
    for i in range(len(cube) - 1):
        if cube[i][0][0] == cube[i + 1][0][0]:
            return False
    
    for grid in cube:
        if not check_grid(grid):
            return False
    return True
# if __name__ == "__main__":
#     assert golf([[["X", "Z"],
#                   ["Z", "X"]],
#                  [["Z", "X"],
#                   ["X", "Z"]]]) == True, "1st example"
#   assert golf([[["X", "Z"],
#                   ["Z", "X"]],
#                  [["X", "Z"],
#                   ["Z", "X"]]]) == False, "2nd example"
#   print("All done? Earn rewards by using the 'Check' button!")

