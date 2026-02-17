"""
Shared utilities for all projects.

This module provides common functions used across multiple projects
including JSON file handling, input validation, and date operations.
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional


def load_json(filepath: str) -> Dict[str, Any]:
    """
    Load data from a JSON file.
    
    Args:
        filepath: Path to the JSON file
        
    Returns:
        Dictionary with loaded data or empty dict if file doesn't exist
        
    Raises:
        json.JSONDecodeError: If JSON format is invalid
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in {filepath}: {e}")
        return {}


def save_json(filepath: str, data: Dict[str, Any]) -> bool:
    """
    Save data to a JSON file.
    
    Args:
        filepath: Path to save the JSON file
        data: Dictionary to save
        
    Returns:
        True if successful, False otherwise
    """
    try:
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return True
    except IOError as e:
        print(f"Error saving {filepath}: {e}")
        return False


def validate_date(date_string: str, date_format: str = "%d/%m/%Y") -> Optional[datetime]:
    """
    Validate a date string in a specific format.
    
    Args:
        date_string: Date to validate
        date_format: Expected format (default: DD/MM/YYYY)
        
    Returns:
        datetime object if valid, None otherwise
    """
    try:
        return datetime.strptime(date_string, date_format)
    except ValueError:
        return None


def get_valid_input(prompt: str, input_type: type = str, max_attempts: int = 3) -> Optional[Any]:
    """
    Get user input with type validation and retry logic.
    
    Args:
        prompt: Message to display
        input_type: Expected type (str, int, float)
        max_attempts: Maximum retry attempts
        
    Returns:
        Converted value or None if max attempts exceeded
    """
    attempts = 0
    while attempts < max_attempts:
        try:
            user_input = input(prompt)
            return input_type(user_input)
        except ValueError:
            attempts += 1
            print(f"Error: Enter a valid {input_type.__name__} value. Attempts left: {max_attempts - attempts}")
        except KeyboardInterrupt:
            print("\nOperation cancelled")
            return None
    
    print(f"Maximum attempts ({max_attempts}) exceeded")
    return None


def clear_screen() -> None:
    """Clear the console screen."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')