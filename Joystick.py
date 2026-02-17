"""
Joystick Controller Simulator Module.

Simulates joystick input with movement detection and control mapping.
"""

from typing import Tuple, Dict
from utils import get_valid_input


class JoystickController:
    """Simulates a joystick controller."""
    
    def __init__(self, center_x: float = 0.0, center_y: float = 0.0) -> None:
        """
        Initialize joystick controller.
        
        Args:
            center_x: X coordinate of center position
            center_y: Y coordinate of center position
        """
        self.center_x = center_x
        self.center_y = center_y
        self.current_x = center_x
        self.current_y = center_y
        self.max_range = 100
    
    def move(self, x: float, y: float) -> bool:
        """
        Move joystick to specified position.
        
        Args:
            x: X coordinate (-100 to 100)
            y: Y coordinate (-100 to 100)
            
        Returns:
            True if move was valid
        """
        if abs(x) > self.max_range or abs(y) > self.max_range:
            print(f"Error: Coordinates must be between -{self.max_range} and {self.max_range}")
            return False
        
        self.current_x = x
        self.current_y = y
        return True
    
    def get_direction(self) -> str:
        """
        Get the current direction of the joystick.
        
        Returns:
            Direction string (Up, Down, Left, Right, etc.)
        """
        if self.current_x == 0 and self.current_y == 0:
            return "Center"
        
        directions = []
        
        if self.current_y > 20:
            directions.append("Up")
        elif self.current_y < -20:
            directions.append("Down")
        
        if self.current_x > 20:
            directions.append("Right")
        elif self.current_x < -20:
            directions.append("Left")
        
        return " ".join(directions) if directions else "Center"
    
    def reset(self) -> None:
        """Reset joystick to center position."""
        self.current_x = self.center_x
        self.current_y = self.center_y
    
    def get_position(self) -> Tuple[float, float]:
        """Get current position."""
        return (self.current_x, self.current_y)
    
    def display_status(self) -> None:
        """Display joystick status."""
        print(f"\n--- Joystick Status ---")
        print(f"Position: X={self.current_x}, Y={self.current_y}")
        print(f"Direction: {self.get_direction()}")
        print(f"Distance from center: {((self.current_x**2 + self.current_y**2)**0.5):.2f}\n")


def main() -> None:
    """Main function to run the joystick simulator."""
    joystick = JoystickController()
    
    print("=== Joystick Controller Simulator ===\n")
    
    while True:
        print("Menu:")
        print("1. Move joystick")
        print("2. View status")
        print("3. Reset to center")
        print("4. Exit")
        
        choice = input("\nSelect an option (1-4): ").strip()
        
        if choice == '1':
            x = get_valid_input("X coordinate (-100 to 100): ", float)
            if x is not None:
                y = get_valid_input("Y coordinate (-100 to 100): ", float)
                if y is not None:
                    if joystick.move(x, y):
                        joystick.display_status()
        
        elif choice == '2':
            joystick.display_status()
        
        elif choice == '3':
            joystick.reset()
            print("Joystick reset to center\n")
        
        elif choice == '4':
            print("Goodbye!")
            break
        
        else:
            print("Invalid option. Please try again.\n")


if __name__ == "__main__":
    main()

