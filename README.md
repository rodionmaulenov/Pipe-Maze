# Pipe Maze Solver

This Python script solves a maze represented as a grid of pipes. The objective is to find the furthest point from the starting position within the maze.

## How It Works

The code can be broken down into several key components:

### Reading the Grid

The `read_grid` function converts the input text into a 2D array, with each element representing a cell in the grid.

### Defining Pipe Connections

`connections` is a dictionary that details how the different pipe symbols connect to each other within the grid.

### Finding the Start

`find_start` locates the 'S' character in the grid, which represents the starting position for the maze traversal.

### Inferring Pipe Type

`infer_type` deduces the type of pipe at the start position by examining the neighboring cells and determining the possible connections.

### Traversing the Maze

The `bfs` (Breadth-First Search) function traverses the maze from the starting position. It uses a queue to keep track of the next positions to visit and the distance from the start.

### Utility Functions

- `get_directions` translates a pipe type into potential movement directions.
- `is_valid` checks if the given coordinates are within the bounds of the grid.

### Main Execution

When the `main` function is called, it puts all pieces together to read the input, start the maze traversal, and output the furthest distance from the starting point.

