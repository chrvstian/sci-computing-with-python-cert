"""
@name: budget.py
@date: 07/11/2023 (dd/mm/yy)
@author: github.com/chrvstian
"""


class Category:
    def __init__(self, category):
        """Initialize a budget category with a given name."""
        self.category = category
        self.ledger = []

    def deposit(self, amount, description=""):
        """Record a deposit in the ledger."""
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        """Record a withdrawal in the ledger if sufficient funds are available."""
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        """Calculate and return the current balance of the budget category."""
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, budget_category):
        """Transfer funds to another budget category if sufficient funds are available."""
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {budget_category.category}")
            budget_category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False

    def check_funds(self, amount):
        """Check if there are sufficient funds for a given amount."""
        return amount <= self.get_balance()

    def __str__(self):
        """Return a formatted string representation of the budget category."""
        output = f"{self.category:*^30}\n"
        for item in self.ledger:
            description = item["description"][:23]
            amount = format(item["amount"], ".2f")
            output += f"{description}{amount.rjust(30 - len(description))}\n"
        total = format(self.get_balance(), ".2f")
        output += f"Total: {total}"
        return output


def create_spend_chart(categories: list) -> str:
    # Calculate total spending and percentage spent for each category
    spend = [
        sum(
        abs(item['amount']) for item in category.ledger if item['amount'] < 0
        ) for category in categories
        ]
    total = sum(spend)
    percentage = [i / total * 100 for i in spend]

    # Initialize the chart with the title
    spaces = "Percentage spent by category"

    # Generate the vertical bars in the chart
    for i in range(100, -1, -10):
        spaces += "\n" + str(i).rjust(3) + "|"
        for j in percentage:
            # Add "o" if percentage is greater than the current value
            spaces += " o " if j > i else "   "
        spaces += " "

    spaces += "\n    ----------"

    # Generate the category labels at the bottom of the chart
    category_length = [len(category.category) for category in categories]
    max_length = max(category_length)
    for i in range(max_length):
        spaces += "\n    "
        for j in range(len(categories)):
            # Add category label or spaces if category name is shorter
            spaces += " " + categories[j].category[i] + " " if i < category_length[j] else "   "

        spaces += " "

    return spaces
