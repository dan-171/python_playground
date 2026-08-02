class Category:
    def __init__(self, name) -> None:
        self.name = name
        self.ledger = []

    def deposit(self, amount: float, desc:str = "") -> None:
        self.ledger.append({'amount': amount, 'description': desc})

    def withdraw(self, amount: float, desc:str = "") -> bool:
        if not self.check_funds(amount):
            return False
        self.ledger.append({'amount': -amount, 'description': desc})
        return True

    def get_balance(self) -> float:
        balance = 0
        for ledger_entry in self.ledger:
            balance += ledger_entry['amount']
        return balance

    def transfer(self, amount:float, cat:"Category") -> bool:
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f'Transfer to {cat.name}')
        cat.deposit(amount, f'Transfer from {self.name}')
        return True

    def check_funds(self, amount:float) -> bool:
        if amount > self.get_balance():
            return False
        return True

    def __str__(self) -> str:
        output = f"{self.name.center(30, '*')}\n"
        for ledger_entry in self.ledger:
            output += f"{ledger_entry['description'][:23]:<23}{ledger_entry['amount']:>7.2f}\n"
        output += f'Total: {self.get_balance()}'
        return output

def create_spend_chart(categories):
    output = ""
    percentage_spent_by_cat = []
    output += 'Percentage spent by category\n'
    total_spent_by_all_cat = sum(-ledger_entry['amount'] for category in categories for ledger_entry in category.ledger if ledger_entry['amount'] < 0)
    print("total spent", total_spent_by_all_cat)
    for category in categories:
        total_spent = 0
        for ledger_entry in category.ledger:
            if ledger_entry['amount'] < 0:
                total_spent += -ledger_entry['amount']
        percentage_spent_by_cat.append((total_spent / total_spent_by_all_cat) * 100 // 10 * 10)

    for i in range (100, -10, -10):
        draw_dot = []
        for percentage in percentage_spent_by_cat:
            if i <= percentage:
                draw_dot.append(1)
            else:
                draw_dot.append(0)
        output += (f"{i:>3}| {'  '.join('o' if d == 1 else ' ' for d in draw_dot)}  \n")
    output += (f"    {'-'.join('--' for category in categories)}--\n")

    max_cat_name_length = max(len(category.name) for category in categories)
    for row in range(max_cat_name_length):
        output += (f"     {'  '.join(category.name[row] if row < len(category.name) else ' ' for category in categories)}  ")
        if row < max_cat_name_length - 1:
            output += "\n"
    return output

# test cases
food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(410.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)

drinks = Category('Drinks')
drinks.deposit(500, 'initial deposit')
drinks.withdraw(200, 'withdraw test')
print(create_spend_chart([food, drinks]))