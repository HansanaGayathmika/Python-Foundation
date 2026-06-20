class Expenses:
    def __init__(self, category: str, price: float):
        self.category = category
        self.price = price

class Expenses_tracker:
    def __init__(self):
        self.tracker_lists =[]


    def add_category(self, expence: str ):
        self.add_category.append(expence)
        print(f"added {expence} ${self.price}")

    def total(self):
        return sum(item.price for item in self.tracker_lists)
    
    def show_expenses(self):
        if not self.tracker_lists:
            print("Not any expenses")
            return
        print("\n ---your expenses--- ")
        for i , item in enumerate(self.tracker_lists, 1):
            print(f"{i}. {item.name} -${item.price}")
                   