"""
To-Do List Management System.

A task management application with features to add, complete, delete,
and persist tasks to a JSON file.
"""

from typing import List, Dict
from datetime import datetime
import sys

sys.path.insert(0, '..')
from utils import load_json, save_json, get_valid_input


class TodoList:
    """Manages to-do list operations."""
    
    def __init__(self, data_file: str = "todo_list/todo.json") -> None:
        """
        Initialize the to-do list.
        
        Args:
            data_file: Path to the JSON file storing tasks
        """
        self.data_file = data_file
        self.tasks: List[Dict] = load_json(data_file)
    
    def add_task(self, title: str, description: str = "", priority: str = "medium") -> bool:
        """
        Add a new task.
        
        Args:
            title: Task title
            description: Task description
            priority: Priority level (low, medium, high)
            
        Returns:
            True if added successfully
        """
        if not title.strip():
            print("Error: Task title cannot be empty")
            return False
        
        if priority.lower() not in ["low", "medium", "high"]:
            print("Error: Priority must be low, medium, or high")
            return False
        
        task = {
            'id': len(self.tasks) + 1,
            'title': title,
            'description': description,
            'priority': priority.lower(),
            'completed': False,
            'created_date': datetime.now().strftime("%d/%m/%Y %H:%M"),
            'completed_date': None
        }
        
        self.tasks.append(task)
        self._save_tasks()
        print(f"Task '{title}' added successfully")
        return True
    
    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by ID.
        
        Args:
            task_id: ID of the task to delete
            
        Returns:
            True if deleted, False if not found
        """
        initial_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if task['id'] != task_id]
        
        if len(self.tasks) < initial_count:
            self._save_tasks()
            print("Task deleted successfully")
            return True
        
        print(f"Task with ID {task_id} not found")
        return False
    
    def complete_task(self, task_id: int) -> bool:
        """
        Mark a task as completed.
        
        Args:
            task_id: ID of the task to complete
            
        Returns:
            True if successful, False otherwise
        """
        task = self._find_task(task_id)
        
        if not task:
            print(f"Task with ID {task_id} not found")
            return False
        
        if task['completed']:
            print(f"Task '{task['title']}' is already completed")
            return False
        
        task['completed'] = True
        task['completed_date'] = datetime.now().strftime("%d/%m/%Y %H:%M")
        self._save_tasks()
        print(f"Task '{task['title']}' completed")
        return True
    
    def get_pending_tasks(self) -> List[Dict]:
        """Get all pending tasks."""
        return [task for task in self.tasks if not task['completed']]
    
    def get_completed_tasks(self) -> List[Dict]:
        """Get all completed tasks."""
        return [task for task in self.tasks if task['completed']]
    
    def get_tasks_by_priority(self, priority: str) -> List[Dict]:
        """
        Get tasks filtered by priority.
        
        Args:
            priority: Priority level (low, medium, high)
            
        Returns:
            List of tasks with specified priority
        """
        return [task for task in self.tasks if task['priority'] == priority.lower()]
    
    def list_tasks(self, filter_type: str = "all") -> None:
        """
        Display tasks filtered by type.
        
        Args:
            filter_type: 'all', 'pending', or 'completed'
        """
        if filter_type == "pending":
            tasks = self.get_pending_tasks()
        elif filter_type == "completed":
            tasks = self.get_completed_tasks()
        else:
            tasks = self.tasks
        
        if not tasks:
            print(f"\nNo {filter_type} tasks\n")
            return
        
        print(f"\n--- {filter_type.capitalize()} Tasks ---")
        print(f"{'ID':<4} {'Status':<10} {'Priority':<10} {'Title':<30} {'Created':<16}")
        print("-" * 70)
        
        for task in tasks:
            status = "✓ Done" if task['completed'] else "○ Pending"
            print(f"{task['id']:<4} {status:<10} {task['priority']:<10} {task['title']:<30} {task['created_date']:<16}")
        
        print()
    
    def _find_task(self, task_id: int) -> Dict | None:
        """Find a task by ID."""
        return next((task for task in self.tasks if task['id'] == task_id), None)
    
    def _save_tasks(self) -> None:
        """Save tasks to JSON file."""
        save_json(self.data_file, self.tasks)


def main() -> None:
    """Main function to run the to-do list system."""
    todo_list = TodoList()
    
    print("=== To-Do List Manager ===\n")
    
    while True:
        print("Menu:")
        print("1. View all tasks")
        print("2. View pending tasks")
        print("3. View completed tasks")
        print("4. Add task")
        print("5. Complete task")
        print("6. Delete task")
        print("7. Filter by priority")
        print("8. Exit")
        
        choice = input("\nSelect an option (1-8): ").strip()
        
        if choice == '1':
            todo_list.list_tasks("all")
        
        elif choice == '2':
            todo_list.list_tasks("pending")
        
        elif choice == '3':
            todo_list.list_tasks("completed")
        
        elif choice == '4':
            title = input("Task title: ").strip()
            description = input("Description (optional): ").strip()
            priority = input("Priority (low/medium/high) [default: medium]: ").strip() or "medium"
            todo_list.add_task(title, description, priority)
        
        elif choice == '5':
            todo_list.list_tasks("pending")
            task_id = get_valid_input("Task ID to complete: ", int)
            if task_id is not None:
                todo_list.complete_task(task_id)
        
        elif choice == '6':
            todo_list.list_tasks("all")
            task_id = get_valid_input("Task ID to delete: ", int)
            if task_id is not None:
                todo_list.delete_task(task_id)
        
        elif choice == '7':
            priority = input("Filter by (low/medium/high): ").strip().lower()
            tasks = todo_list.get_tasks_by_priority(priority)
            if tasks:
                print(f"\n--- {priority.capitalize()} Priority Tasks ---")
                for task in tasks:
                    status = "✓" if task['completed'] else "○"
                    print(f"  [{status}] {task['title']}")
                print()
            else:
                print(f"\nNo tasks with {priority} priority\n")
        
        elif choice == '8':
            print("Goodbye!")
            break
        
        else:
            print("Invalid option. Please try again.\n")


if __name__ == "__main__":
    main()