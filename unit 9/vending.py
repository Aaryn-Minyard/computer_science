class VendingMachine:
    def __init__(self):
        self.bottles = 20
        
    def purchase(self, amount):
        self.bottles = self.bottles - amount
      
    def restock(self, amount):
        self.bottles = self.bottles + amount
    
    def get_inventory(self):
        return self.bottles
        
    def report(self):
        print(f'Inventory: {self.bottles} bottles')

if __name__ == "__main__":
    vending_machine = VendingMachine()
    purchase_amount = int(input("Enter number of bottles to purchase: "))
    vending_machine.purchase(purchase_amount)
    restock_amount = int(input("Enter number of bottles to restock: "))
    vending_machine.restock(restock_amount)
    vending_machine.report()
    