"""
Profitability Analysis Module.

Analyzes project profitability with financial calculations and reporting.
"""

from typing import List, Dict
from utils import get_valid_input


class ProjectAnalysis:
    """Analyzes project financial metrics."""
    
    def __init__(self, name: str, investment: float) -> None:
        """
        Initialize project analysis.
        
        Args:
            name: Project name
            investment: Initial investment amount
        """
        self.name = name
        self.investment = investment
        self.revenues: List[float] = []
        self.costs: List[float] = []
    
    def add_revenue(self, amount: float, period: int = 1) -> bool:
        """
        Add revenue for a period.
        
        Args:
            amount: Revenue amount
            period: Period number
            
        Returns:
            True if added successfully
        """
        if amount < 0:
            print("Error: Revenue cannot be negative")
            return False
        
        self.revenues.append(amount)
        print(f"Added revenue: ${amount:.2f}")
        return True
    
    def add_cost(self, amount: float) -> bool:
        """
        Add operating cost.
        
        Args:
            amount: Cost amount
            
        Returns:
            True if added successfully
        """
        if amount < 0:
            print("Error: Cost cannot be negative")
            return False
        
        self.costs.append(amount)
        print(f"Added cost: ${amount:.2f}")
        return True
    
    def calculate_total_revenue(self) -> float:
        """Calculate total revenue."""
        return sum(self.revenues)
    
    def calculate_total_costs(self) -> float:
        """Calculate total costs."""
        return sum(self.costs)
    
    def calculate_net_profit(self) -> float:
        """Calculate net profit."""
        return self.calculate_total_revenue() - self.calculate_total_costs() - self.investment
    
    def calculate_roi(self) -> float:
        """
        Calculate Return on Investment (ROI).
        
        Returns:
            ROI percentage
        """
        if self.investment == 0:
            return 0
        return (self.calculate_net_profit() / self.investment) * 100
    
    def calculate_payback_period(self) -> float:
        """
        Calculate payback period in periods.
        
        Returns:
            Number of periods to recover investment
        """
        cumulative = 0
        for i, revenue in enumerate(self.revenues):
            cumulative += revenue - (self.calculate_total_costs() / len(self.revenues) if self.revenues else 0)
            if cumulative >= self.investment:
                return i + 1
        return -1
    
    def generate_report(self) -> None:
        """Generate profitability report."""
        print(f"\n=== Profitability Report: {self.name} ===")
        print(f"Initial Investment: ${self.investment:.2f}")
        print(f"Total Revenue: ${self.calculate_total_revenue():.2f}")
        print(f"Total Costs: ${self.calculate_total_costs():.2f}")
        print(f"Net Profit: ${self.calculate_net_profit():.2f}")
        print(f"ROI: {self.calculate_roi():.2f}%")
        
        payback = self.calculate_payback_period()
        if payback > 0:
            print(f"Payback Period: {payback:.1f} periods")
        else:
            print("Payback Period: Not achieved")
        
        if self.calculate_net_profit() > 0:
            print("Status: ✓ PROFITABLE")
        else:
            print("Status: ✗ NOT PROFITABLE")
        print()


def main() -> None:
    """Main function to run profitability analysis."""
    print("=== Profitability Analysis Tool ===\n")
    
    project_name = input("Project name: ").strip()
    investment = get_valid_input("Initial investment: $", float)
    
    if investment is None or investment < 0:
        print("Error: Invalid investment amount")
        return
    
    project = ProjectAnalysis(project_name, investment)
    
    while True:
        print("\nMenu:")
        print("1. Add revenue")
        print("2. Add cost")
        print("3. Generate report")
        print("4. Exit")
        
        choice = input("\nSelect an option (1-4): ").strip()
        
        if choice == '1':
            amount = get_valid_input("Revenue amount: $", float)
            if amount is not None:
                project.add_revenue(amount)
        
        elif choice == '2':
            amount = get_valid_input("Cost amount: $", float)
            if amount is not None:
                project.add_cost(amount)
        
        elif choice == '3':
            project.generate_report()
        
        elif choice == '4':
            print("Goodbye!")
            break
        
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()