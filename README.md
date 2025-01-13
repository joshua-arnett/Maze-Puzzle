# Maze-Puzzle
Solve Maze Puzzle using Backtracking and BFS Graph Traversal

This program takes a 2D puzzle of size MxN, that has M rows and N columns (M and N can be different). Each cell is either empty or has a barrier. An empty cell is marked by '-' (hyphen) and the one with a barrier is marked by '#'. You are given two coordinates from the puzzle (a,b) and (x,y). You can move only in the following directions:
L: move to left cell from the current cell
R: move to right cell from the current cell
U: move to upper cell from the current cell
D: move to lower cell from the current cell

You can only move to an empty cell and cannot move to a cell with a barrier in it. Your goal is to reach the destination cell, covering the **minimum number of cells** as you travel from the start cell.

<img width="389" alt="image" src="https://github.com/user-attachments/assets/3c0a842a-b146-4958-b426-7e860fb57ff6" />

This program takes three inputs: (Puzzle, Source, Destination)
To call this program and solve the problem, simply call __solve_puzzle(Puzzle, Source, Destination)__
The function will return a tuple containing the path, as well as the directions, taken to reach the destination tile. If no path exists, the program return None.

Example function call:
Maze = [
  ['-', '-', '-', '-', '-'],
  ['-', '-', '#', '-', '-'],
  ['-', '-', '-', '-', '-'],
  ['#', '-', '#', '#', '-'],
  ['-', '#', '-', '-', '-']
]
print(solve_puzzle(Maze, (0,2), (2,2)))

Output: ([(0,2), (0,1), (1,1), (2,1), (2,2)], 'LDDR')
