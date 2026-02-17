"""
Maze Solver Module.

A pathfinding system that generates and solves mazes using BFS algorithm.
Supports multiple maze files and visualizes solutions.
"""

from collections import deque
from typing import List, Tuple, Optional, Set
from pathlib import Path


class Maze:
    """Represents and solves a maze."""
    
    def __init__(self, filename: str) -> None:
        """
        Initialize maze from a file.
        
        Args:
            filename: Path to the maze file
            
        Raises:
            FileNotFoundError: If maze file doesn't exist
            ValueError: If maze format is invalid
        """
        self.filename = filename
        self.grid: List[List[str]] = []
        self.start: Optional[Tuple[int, int]] = None
        self.end: Optional[Tuple[int, int]] = None
        self.solution_path: List[Tuple[int, int]] = []
        
        self._load_maze()
        self._find_start_end()
    
    def _load_maze(self) -> None:
        """Load maze from file."""
        try:
            with open(self.filename, 'r') as f:
                self.grid = [list(line.rstrip('\n')) for line in f.readlines()]
            
            if not self.grid:
                raise ValueError("Maze file is empty")
        
        except FileNotFoundError:
            raise FileNotFoundError(f"Maze file '{self.filename}' not found")
    
    def _find_start_end(self) -> None:
        """Find start (S) and end (E) positions in the maze."""
        for row in range(len(self.grid)):
            for col in range(len(self.grid[row])):
                if self.grid[row][col] == 'S':
                    self.start = (row, col)
                elif self.grid[row][col] == 'E':
                    self.end = (row, col)
        
        if not self.start or not self.end:
            raise ValueError("Maze must contain 'S' (start) and 'E' (end) markers")
    
    def solve(self) -> bool:
        """
        Solve the maze using BFS algorithm.
        
        Returns:
            True if solution found, False otherwise
        """
        if not self.start or not self.end:
            return False
        
        queue = deque([(self.start, [self.start])])
        visited: Set[Tuple[int, int]] = {self.start}
        
        while queue:
            (row, col), path = queue.popleft()
            
            if (row, col) == self.end:
                self.solution_path = path
                return True
            
            for next_row, next_col in self._get_neighbors(row, col):
                if (next_row, next_col) not in visited:
                    visited.add((next_row, next_col))
                    queue.append(((next_row, next_col), path + [(next_row, next_col)]))
        
        return False
    
    def _get_neighbors(self, row: int, col: int) -> List[Tuple[int, int]]:
        """Get valid neighbors (not walls) for a position."""
        neighbors = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if self._is_valid_position(new_row, new_col):
                neighbors.append((new_row, new_col))
        
        return neighbors
    
    def _is_valid_position(self, row: int, col: int) -> bool:
        """Check if a position is valid and not a wall."""
        if row < 0 or row >= len(self.grid):
            return False
        if col < 0 or col >= len(self.grid[row]):
            return False
        
        cell = self.grid[row][col]
        return cell != '#'  # '#' represents walls
    
    def display(self, show_solution: bool = False) -> None:
        """
        Display the maze and optionally the solution.
        
        Args:
            show_solution: If True, mark the solution path
        """
        grid_copy = [row[:] for row in self.grid]
        
        if show_solution and self.solution_path:
            for row, col in self.solution_path[1:-1]:
                if grid_copy[row][col] not in ['S', 'E']:
                    grid_copy[row][col] = '*'
        
        print("\n--- Maze ---")
        for row in grid_copy:
            print(''.join(row))
        print()
    
    def get_solution_length(self) -> int:
        """Get the number of steps in the solution."""
        return len(self.solution_path) - 1


def main() -> None:
    """Main function to run the maze solver."""
    print("=== Maze Solver ===\n")
    
    maze_files = [f for f in Path('.').glob('*.txt')]
    
    if not maze_files:
        print("Error: No maze files (.txt) found in current directory")
        return
    
    print(f"Available mazes: {[f.name for f in maze_files]}\n")
    
    while True:
        filename = input("Enter maze filename (or 'q' to quit): ").strip()
        
        if filename.lower() == 'q':
            print("Goodbye!")
            break
        
        try:
            maze = Maze(filename)
            print(f"\nLoaded maze: {filename}")
            maze.display()
            
            print("Solving maze...")
            if maze.solve():
                print(f"Solution found! Steps: {maze.get_solution_length()}\n")
                maze.display(show_solution=True)
            else:
                print("No solution found!\n")
        
        except (FileNotFoundError, ValueError) as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    main()
