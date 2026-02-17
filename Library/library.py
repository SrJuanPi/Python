"""
Library Management System Module.

A comprehensive system for managing books in a library with features like
adding books, searching, borrowing, and returning.
"""

import json
from pathlib import Path
from typing import List, Dict, Optional
from datetime import datetime
import sys

sys.path.insert(0, '..')
from utils import load_json, save_json, get_valid_input


class Library:
    """Manages library operations and book catalog."""
    
    def __init__(self, data_file: str = "Library/books.json") -> None:
        """
        Initialize the library system.
        
        Args:
            data_file: Path to the JSON file storing books
        """
        self.data_file = data_file
        self.books: List[Dict] = load_json(data_file)
    
    def add_book(self, title: str, author: str, isbn: str, year: int) -> bool:
        """
        Add a new book to the library.
        
        Args:
            title: Book title
            author: Author name
            isbn: ISBN number
            year: Publication year
            
        Returns:
            True if added successfully, False if duplicate
        """
        if self._book_exists(isbn):
            print(f"Error: Book with ISBN {isbn} already exists")
            return False
        
        book = {
            'id': len(self.books) + 1,
            'title': title,
            'author': author,
            'isbn': isbn,
            'year': year,
            'available': True,
            'borrowed_by': None,
            'borrow_date': None
        }
        
        self.books.append(book)
        self._save_books()
        print(f"Book '{title}' added successfully")
        return True
    
    def remove_book(self, isbn: str) -> bool:
        """
        Remove a book from the library.
        
        Args:
            isbn: ISBN of the book to remove
            
        Returns:
            True if removed, False if not found
        """
        initial_count = len(self.books)
        self.books = [book for book in self.books if book['isbn'] != isbn]
        
        if len(self.books) < initial_count:
            self._save_books()
            print("Book removed successfully")
            return True
        
        print(f"Book with ISBN {isbn} not found")
        return False
    
    def search_books(self, query: str, search_type: str = "title") -> List[Dict]:
        """
        Search for books by title, author, or ISBN.
        
        Args:
            query: Search term
            search_type: 'title', 'author', or 'isbn'
            
        Returns:
            List of matching books
        """
        query_lower = query.lower()
        results = []
        
        for book in self.books:
            if search_type == "title" and query_lower in book['title'].lower():
                results.append(book)
            elif search_type == "author" and query_lower in book['author'].lower():
                results.append(book)
            elif search_type == "isbn" and query == book['isbn']:
                results.append(book)
        
        return results
    
    def borrow_book(self, isbn: str, borrower_name: str) -> bool:
        """
        Mark a book as borrowed.
        
        Args:
            isbn: ISBN of the book
            borrower_name: Name of the borrower
            
        Returns:
            True if successful, False otherwise
        """
        book = self._find_book(isbn)
        
        if not book:
            print(f"Book with ISBN {isbn} not found")
            return False
        
        if not book['available']:
            print(f"Book '{book['title']}' is already borrowed by {book['borrowed_by']}")
            return False
        
        book['available'] = False
        book['borrowed_by'] = borrower_name
        book['borrow_date'] = datetime.now().strftime("%d/%m/%Y")
        self._save_books()
        print(f"Book '{book['title']}' borrowed by {borrower_name}")
        return True
    
    def return_book(self, isbn: str) -> bool:
        """
        Mark a book as returned.
        
        Args:
            isbn: ISBN of the book
            
        Returns:
            True if successful, False otherwise
        """
        book = self._find_book(isbn)
        
        if not book:
            print(f"Book with ISBN {isbn} not found")
            return False
        
        if book['available']:
            print(f"Book '{book['title']}' was not borrowed")
            return False
        
        borrower = book['borrowed_by']
        book['available'] = True
        book['borrowed_by'] = None
        book['borrow_date'] = None
        self._save_books()
        print(f"Book '{book['title']}' returned by {borrower}")
        return True
    
    def list_all_books(self) -> None:
        """Display all books in the library."""
        if not self.books:
            print("\nLibrary is empty\n")
            return
        
        print("\n--- Library Catalog ---")
        print(f"{'ID':<4} {'Title':<30} {'Author':<20} {'ISBN':<13} {'Status':<10}")
        print("-" * 77)
        
        for book in self.books:
            status = "Available" if book['available'] else f"Borrowed by {book['borrowed_by']}"
            print(f"{book['id']:<4} {book['title']:<30} {book['author']:<20} {book['isbn']:<13} {status:<10}")
        
        print()
    
    def _find_book(self, isbn: str) -> Optional[Dict]:
        """Find a book by ISBN."""
        return next((book for book in self.books if book['isbn'] == isbn), None)
    
    def _book_exists(self, isbn: str) -> bool:
        """Check if a book exists by ISBN."""
        return self._find_book(isbn) is not None
    
    def _save_books(self) -> None:
        """Save books to JSON file."""
        save_json(self.data_file, self.books)


def main() -> None:
    """Main function to run the library management system."""
    library = Library()
    
    print("=== Library Management System ===\n")
    
    while True:
        print("Menu:")
        print("1. Add book")
        print("2. Remove book")
        print("3. Search books")
        print("4. Borrow book")
        print("5. Return book")
        print("6. View all books")
        print("7. Exit")
        
        choice = input("\nSelect an option (1-7): ").strip()
        
        if choice == '1':
            title = input("Book title: ").strip()
            author = input("Author: ").strip()
            isbn = input("ISBN: ").strip()
            year = get_valid_input("Publication year: ", int)
            if year is not None:
                library.add_book(title, author, isbn, year)
        
        elif choice == '2':
            isbn = input("ISBN of book to remove: ").strip()
            library.remove_book(isbn)
        
        elif choice == '3':
            query = input("Search term: ").strip()
            search_type = input("Search by (title/author/isbn) [default: title]: ").strip() or "title"
            results = library.search_books(query, search_type)
            
            if results:
                print(f"\nFound {len(results)} result(s):")
                for book in results:
                    status = "Available" if book['available'] else f"Borrowed"
                    print(f"  - {book['title']} by {book['author']} ({status})")
                print()
            else:
                print("No results found\n")
        
        elif choice == '4':
            isbn = input("ISBN: ").strip()
            borrower = input("Borrower name: ").strip()
            library.borrow_book(isbn, borrower)
        
        elif choice == '5':
            isbn = input("ISBN: ").strip()
            library.return_book(isbn)
        
        elif choice == '6':
            library.list_all_books()
        
        elif choice == '7':
            print("Goodbye!")
            break
        
        else:
            print("Invalid option. Please try again.\n")


if __name__ == "__main__":
    main()