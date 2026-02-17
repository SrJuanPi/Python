"""
Birthday Calculator Module.

This module calculates the exact age (years, months, and days) of a person
based on their birth date.
"""

from datetime import datetime, timedelta
from typing import Dict, Optional
from utils import validate_date, get_valid_input


def calculate_age(birth_date: datetime) -> Dict[str, int]:
    """
    Calculate exact age from a birth date.
    
    Args:
        birth_date: datetime object of birth date
        
    Returns:
        Dictionary with keys: years, months, days
        
    Raises:
        ValueError: If birth date is in the future
    """
    today = datetime.now()
    
    if birth_date > today:
        raise ValueError("Birth date cannot be in the future")
    
    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day
    
    if days < 0:
        months -= 1
        days += 30
    
    if months < 0:
        years -= 1
        months += 12
    
    return {"years": years, "months": months, "days": days}


def display_age_info(age: Dict[str, int], name: Optional[str] = None) -> None:
    """
    Display age information in a formatted way.
    
    Args:
        age: Dictionary with years, months, days
        name: Optional person's name
    """
    person = f"{name}'s " if name else ""
    print(f"\n{person}Age:")
    print(f"  Years: {age['years']}")
    print(f"  Months: {age['months']}")
    print(f"  Days: {age['days']}")
    print(f"  Total months: {age['years'] * 12 + age['months']}")
    print(f"  Total days: {age['years'] * 365 + age['months'] * 30 + age['days']}\n")


def main() -> None:
    """Main function to run the birthday calculator."""
    print("=== Birthday Calculator ===\n")
    
    while True:
        date_input = input("Enter your birth date (DD/MM/YYYY) or 'q' to quit: ").strip()
        
        if date_input.lower() == 'q':
            print("Goodbye!")
            break
        
        birth_date = validate_date(date_input)
        
        if birth_date is None:
            print("Error: Invalid date format. Please use DD/MM/YYYY\n")
            continue
        
        try:
            age = calculate_age(birth_date)
            display_age_info(age)
        except ValueError as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    main()