"""
Date of Year Calculator Module.

Determines which day of the year a given date is, accounting for leap years.
"""

from datetime import datetime
from typing import Optional
from utils import validate_date


def get_day_of_year(date: datetime) -> int:
    """
    Get the day number in the year for a given date.
    
    Args:
        date: datetime object
        
    Returns:
        Day number (1-366)
    """
    year_start = datetime(date.year, 1, 1)
    day_of_year = (date - year_start).days + 1
    return day_of_year


def is_leap_year(year: int) -> bool:
    """
    Check if a year is a leap year.
    
    Args:
        year: Year to check
        
    Returns:
        True if leap year, False otherwise
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def get_days_in_year(year: int) -> int:
    """
    Get total days in a year.
    
    Args:
        year: Year to check
        
    Returns:
        365 or 366 for leap years
    """
    return 366 if is_leap_year(year) else 365


def display_date_info(date: datetime, day_of_year: int) -> None:
    """
    Display date information in formatted way.
    
    Args:
        date: datetime object
        day_of_year: Day number in year
    """
    total_days = get_days_in_year(date.year)
    remaining_days = total_days - day_of_year
    leap_status = "leap year" if is_leap_year(date.year) else "regular year"
    
    print(f"\n--- Date Information ---")
    print(f"Date: {date.strftime('%d/%m/%Y (%A)')}")
    print(f"Day of year: {day_of_year} of {total_days}")
    print(f"Remaining days: {remaining_days}")
    print(f"Year type: {leap_status}")
    print(f"Progress: {(day_of_year / total_days * 100):.1f}%\n")


def main() -> None:
    """Main function to run the date of year calculator."""
    print("=== Date of Year Calculator ===\n")
    
    while True:
        date_input = input("Enter a date (DD/MM/YYYY) or 'q' to quit: ").strip()
        
        if date_input.lower() == 'q':
            print("Goodbye!")
            break
        
        date = validate_date(date_input)
        
        if date is None:
            print("Error: Invalid date format. Please use DD/MM/YYYY\n")
            continue
        
        day_of_year = get_day_of_year(date)
        display_date_info(date, day_of_year)


if __name__ == "__main__":
    main()